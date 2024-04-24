import sqlite3

def create_connection(db_file):
    """Create a connection to the SQLite database."""
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)
    return conn

def create_table(conn):
    """Create a table for storing student information."""
    try:
        sql = '''CREATE TABLE IF NOT EXISTS students (
                 id integer PRIMARY KEY,
                 name text NOT NULL,
                 major text NOT NULL
             );'''
        cursor = conn.cursor()
        cursor.execute(sql)
    except Exception as e:
        print(e)

def add_student(conn, student):
    """Add a new student to the students table."""
    sql = '''INSERT INTO students(id, name, major)
             VALUES(?,?,?)'''
    cursor = conn.cursor()
    cursor.execute(sql, student)
    conn.commit()

def main():
    database = "university.db"

    # Create a database connection
    conn = create_connection(database)

    if conn is not connected:
        print("Error! cannot create the database connection.")
        return

    # Create table
    create_table(conn)

    # Add a student
    student = (1, 'John Doe', 'Computer Science')
    add_student(conn, student)

    # Close the connection
    conn.close()

if __name__ == '__main__':
    main()
