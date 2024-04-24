import sqlite3
from faker import Faker

fake = Faker()

def create_connection(db_file):
    """Create a connection to the SQLite database."""
    conn = sqlite3.connect(db_file)
    return conn

def create_students(conn, num_students=10000):
    """Generate and insert dummy student data into the database."""
    cursor = conn.cursor()
    majors = ['Computer Science', 'Biology', 'Economics', 'Engineering', 'History', 'Psychology']

    for _ in range(num_students):
        id = _  # Simple sequential ID, in practice you might want UUIDs or similar
        name = fake.name()
        major = fake.random.choice(majors)

        cursor.execute('INSERT INTO students (id, name, major) VALUES (?, ?, ?)', (id, name, major))

    conn.commit()

def main():
    database = "university.db"
    conn = create_connection(database)

    # Assuming the table has already been created as per previous Python example
    create_students(conn, 10000)  # Adjust the number as needed

    conn.close()

if __name__ == '__main__':
    main()
