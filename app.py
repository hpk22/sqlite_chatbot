import sqlite3
from flask import Flask, request, jsonify
import re

app = Flask(__name__)

@app.route("/query", methods=["POST"])
def query_database():
    user_query = request.json.get("query", "").lower()
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    response = "I didn't understand your query. Please try again."

    if "employees in" in user_query:
        match = re.search(r"employees in (\w+)", user_query)
        if match:
            department = match.group(1).capitalize()
            cursor.execute("SELECT Name FROM Employees WHERE Department=?", (department,))
            employees = cursor.fetchall()
            response = ", ".join(emp[0] for emp in employees) if employees else "No employees found in this department."

    elif "manager of" in user_query:
        match = re.search(r"manager of (\w+)", user_query)
        if match:
            department = match.group(1).capitalize()
            cursor.execute("SELECT Manager FROM Departments WHERE Name=?", (department,))
            manager = cursor.fetchone()
            response = manager[0] if manager else "No manager found for this department."

    elif "hired after" in user_query:
        match = re.search(r"hired after (\d{4}-\d{2}-\d{2})", user_query)
        if match:
            hire_date = match.group(1)
            cursor.execute("SELECT Name FROM Employees WHERE Hire_Date > ?", (hire_date,))
            employees = cursor.fetchall()
            response = ", ".join(emp[0] for emp in employees) if employees else "No employees hired after this date."

    elif "total salary expense" in user_query:
        match = re.search(r"total salary expense for (\w+)", user_query)
        if match:
            department = match.group(1).capitalize()
            cursor.execute("SELECT SUM(Salary) FROM Employees WHERE Department=?", (department,))
            total_salary = cursor.fetchone()[0]
            response = f"Total salary expense for {department} department is ${total_salary}" if total_salary else "No salary data found."

    conn.close()
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
