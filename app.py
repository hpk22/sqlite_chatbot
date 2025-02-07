import sqlite3
from flask import Flask, render_template, request, jsonify
import re

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/query", methods=["POST"])
def query_database():
    user_query = request.json.get("query", "").lower()
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()
    
    response = "I didn't understand your query. Please try again."

    if "highest salary" in user_query:
        cursor.execute("SELECT Name, Salary FROM Employees ORDER BY Salary DESC LIMIT 1")
        result = cursor.fetchone()
        response = f"{result[0]} has the highest salary of ${result[1]}." if result else "No data available."
    
    elif "between" in user_query:
        match = re.search(r"hired between (\d{4}-\d{2}-\d{2}) and (\d{4}-\d{2}-\d{2})", user_query)
        if match:
            start, end = match.groups()
            cursor.execute("SELECT Name FROM Employees WHERE Hire_Date BETWEEN ? AND ?", (start, end))
            result = cursor.fetchall()
            response = ", ".join([r[0] for r in result]) if result else "No employees found."
    
    elif "employees in" in user_query:
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
