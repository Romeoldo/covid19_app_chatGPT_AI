import requests
import openai
import json
import os
from flask import Flask, request, render_template, jsonify
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)
openai.api_key = os.getenv('OPENAI_API_KEY')

def get_covid_data(country):
    url = f"https://disease.sh/v3/covid-19/countries/{country}"
    response = requests.get(url)
    data = response.json()
    return data

def generate_response(messages):
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
    except openai.error.RateLimitError:
        return "Error: You have exceeded your API quota. Please check your plan and billing details."
    except Exception as e:
        return f"An unexpected error occurred: {e}"
    
    chat_response = response['choices'][0]['message']['content']
    formatted_response = chat_response.replace('\n', '<br>')  # Reemplazar saltos de línea con etiquetas <br>
    return formatted_response

def save_conversation(conversation, filename='conversation_log.json'):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            data = json.load(file)
    else:
        data = []

    data.append(conversation)

    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_conversation', methods=['POST'])
def start_conversation():
    country = request.json.get('country')
    data = get_covid_data(country)

    cases = data['cases']
    deaths = data['deaths']
    recovered = data['recovered']
    active = data['active']
    critical = data['critical']
    tests = data['tests']
    population = data['population']

    messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": (f"Provide detailed COVID-19 information for {country} based on the following data:\n"
                                     f"{cases} confirmed cases,\n"
                                     f"{deaths} deaths,\n"
                                     f"{recovered} recovered individuals,\n"
                                     f"{active} active cases,\n"
                                     f"{critical} critical cases,\n"
                                     f"{tests} tests conducted,\n"
                                     f"and a population of {population}.\n"
                                     "What other specific COVID-19 information would you like to know?")}
    ]

    response = generate_response(messages)
    save_conversation({"user": messages[1]['content'], "assistant": response})
    return jsonify({"response": response})

@app.route('/ask_follow_up', methods=['POST'])
def ask_follow_up():
    follow_up = request.json.get('follow_up')
    messages.append({"role": "user", "content": follow_up})
    response = generate_response(messages)
    save_conversation({"user": follow_up, "assistant": response})
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)




# import requests
# import openai
# import json
# import os
# from flask import Flask, request, render_template, jsonify
# from dotenv import load_dotenv

# # Load environment variables from .env file
# load_dotenv()

# app = Flask(__name__)
# openai.api_key = os.getenv('OPENAI_API_KEY')

# def get_covid_data(country):
#     url = f"https://disease.sh/v3/covid-19/countries/{country}"
#     response = requests.get(url)
#     data = response.json()
#     return data

# def generate_response(messages):
#     try:
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=messages
#         )
#     except openai.error.RateLimitError:
#         return "Error: You have exceeded your API quota. Please check your plan and billing details."
#     except Exception as e:
#         return f"An unexpected error occurred: {e}"
    
#     return response['choices'][0]['message']['content']

# def save_conversation(conversation, filename='conversation_log.json'):
#     if os.path.exists(filename):
#         with open(filename, 'r') as file:
#             data = json.load(file)
#     else:
#         data = []

#     data.append(conversation)

#     with open(filename, 'w') as file:
#         json.dump(data, file, indent=4)

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/start_conversation', methods=['POST'])
# def start_conversation():
#     country = request.json.get('country')
#     data = get_covid_data(country)

#     cases = data['cases']
#     deaths = data['deaths']
#     recovered = data['recovered']
#     active = data['active']
#     critical = data['critical']
#     tests = data['tests']
#     population = data['population']

#     messages = [
#         {"role": "system", "content": "You are a helpful assistant."},
#         {"role": "user", "content": (f"Provide detailed COVID-19 information for {country} based on the following data: "
#                                      f"{cases} confirmed cases, "
#                                      f"{deaths} deaths, "
#                                      f"{recovered} recovered individuals, "
#                                      f"{active} active cases, "
#                                      f"{critical} critical cases, "
#                                      f"{tests} tests conducted, "
#                                      f"and a population of {population}. "
#                                      "What other specific COVID-19 information would you like to know?")}
#     ]

#     response = generate_response(messages)
#     save_conversation({"user": messages[1]['content'], "assistant": response})
#     return jsonify({"response": response})

# @app.route('/ask_follow_up', methods=['POST'])
# def ask_follow_up():
#     follow_up = request.json.get('follow_up')
#     messages.append({"role": "user", "content": follow_up})
#     response = generate_response(messages)
#     save_conversation({"user": follow_up, "assistant": response})
#     return jsonify({"response": response})

# if __name__ == '__main__':
#     app.run(debug=True)
