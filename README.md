AI Chat Assistant for SQLite Database

📌 Project Overview

This AI-powered chat assistant is designed to interact with an SQLite database and answer user queries in natural language. It supports various queries related to employees, departments, salaries, and hiring dates while ensuring robust error handling.

🚀 How It Works

The user submits a natural language query.

The assistant processes the query using regex-based text parsing.

The system translates the query into an SQL command.

The SQLite database is queried based on extracted information.

The assistant returns a structured response to the user.

✨ Supported Queries

Employee Listings: "Show me all employees in Engineering."

Manager Identification: "Who is the manager of Marketing?"

Hiring Date Filters: "List all employees hired after 2021-01-01."

Salary Calculations: "What is the total salary expense for Sales?"

Comparisons: "Who has the highest salary?"

Range Filters: "List all employees hired between 2020-01-01 and 2022-01-01."

🛠️ Installation & Running Locally

Prerequisites

Python 3.x

Flask

SQLite3

Step 1: Clone the Repository

git clone https://github.com/hpk22/sqlite_chatbot.git
cd sqlite_chatbot

Step 2: Set Up Virtual Environment (Optional but Recommended)

python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

Step 3: Install Dependencies

pip install -r requirements.txt

Step 4: Set Up the Database

python database_setup.py

Step 5: Run the Application

python app.py

The Flask server will start at: http://127.0.0.1:5000/

Step 6: Test API Requests

You can test API queries using Postman or cURL.
Example:

curl -X POST http://127.0.0.1:5000/query -H "Content-Type: application/json" -d '{"query": "Who has the highest salary?"}'

🔥 Deployment on Render

Push the project to GitHub

Create a new Web Service on Render

Set up build commands:

pip install -r requirements.txt

gunicorn app:app

Deploy and get a public API URL

❗ Known Limitations & Improvements

Limitations

❌ Limited NLP Capabilities – Uses regex matching instead of advanced NLP models.
❌ No User Context Memory – Each query is processed independently.
❌ Basic UI – Current UI is simple, and can be improved with better frontend interactivity.

Potential Improvements

✅ Enhance NLP Understanding – Use spaCy or an ML model for better query interpretation.
✅ Expand Query Handling – Support more flexible queries like employee comparisons.
✅ Improve UI – Add a chatbot-style frontend with better styling.
