import sqlite3

def create_database():
    conn = sqlite3.connect("employees.db")
    cursor = conn.cursor()

    # Creating Employees table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Employees (
        ID INTEGER PRIMARY KEY,
        Name TEXT,
        Department TEXT,
        Salary INTEGER,
        Hire_Date TEXT
    )''')

    # Creating Departments table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Departments (
        ID INTEGER PRIMARY KEY,
        Name TEXT,
        Manager TEXT
    )''')

    # Inserting sample data
    cursor.execute("INSERT OR IGNORE INTO Employees VALUES (1, 'Alice', 'Sales', 50000, '2021-01-15')")
    cursor.execute("INSERT OR IGNORE INTO Employees VALUES (2, 'Bob', 'Engineering', 70000, '2020-06-10')")
    cursor.execute("INSERT OR IGNORE INTO Employees VALUES (3, 'Charlie', 'Marketing', 60000, '2022-03-20')")

    cursor.execute("INSERT OR IGNORE INTO Departments VALUES (1, 'Sales', 'Alice')")
    cursor.execute("INSERT OR IGNORE INTO Departments VALUES (2, 'Engineering', 'Bob')")
    cursor.execute("INSERT OR IGNORE INTO Departments VALUES (3, 'Marketing', 'Charlie')")

    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    print("Database created successfully!")
