
# COVID-19 Intelligent Data Assistant

This project is an intelligent assistant for COVID-19 data, utilizing the OpenAI API and Flask to create an interactive web application. Users can input a country's name to receive detailed COVID-19 information and ask follow-up questions. The application uses the disease.sh API to fetch real-time COVID-19 data.

## Project Structure

```
covid19_app/
├── static/
│   ├── styles.css
└── templates/
    ├── index.html
├── app.py
└── conversation_log.json
```

## Installation Instructions

### Install Flask

If you don't have Flask installed, you can install it using pip:

```bash
pip install flask
```

### Install Other Required Libraries

Make sure you have Python installed along with the necessary libraries:

```bash
pip install requests openai
```

## Steps to Create the Web Application with Flask

### 1. Select an API

Choose an API that provides interesting and useful data. For this demo, we will use the COVID-19 data API from [disease.sh](https://disease.sh/).

### 2. Set Up the Environment

Ensure you have Python installed and the necessary libraries mentioned above.

### 3. Write the Backend Code (`app.py`)

This file contains the backend code using Flask and OpenAI. It handles requests from the frontend, fetches data from the COVID-19 API, and interacts with the OpenAI API to generate intelligent responses.


### 4. Create an Attractive Presentation

- **User Interface:** You can improve the presentation by creating a graphical user interface (GUI) using Tkinter or a simple web application with Flask.
- **Visualizations:** Incorporate graphs and visualizations with libraries such as Matplotlib or Plotly to display the data more attractively.

### 5. Practice and Preparation

- Rehearse your presentation multiple times to ensure it works smoothly.
- Prepare answers to possible technical questions about how the API and the ChatGPT model work.

### 6. Final Presentation

- **Introduction:** Briefly explain what ChatGPT is and how it works.
- **Live Demo:** Show the script in action by entering different countries and displaying the generated responses.
- **Conclusion:** Highlight practical applications and how this demo can be useful in a business environment.

## Additional Resources

- **OpenAI API Documentation:** [OpenAI API Documentation](https://beta.openai.com/docs/)
- **Disease.sh API Documentation:** [Disease.sh API Documentation](https://disease.sh/docs/)
