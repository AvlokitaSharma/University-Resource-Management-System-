CREATE TABLE IF NOT EXISTS students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    major TEXT NOT NULL
);



INSERT INTO students (name, major) VALUES ('John Doe', 'Computer Science');


INSERT INTO students (name, major) VALUES 
('Alice Smith', 'Economics'), 
('Bob Johnson', 'Engineering'), 
('Carol White', 'Biology');



-- Assuming a simple table structure for courses and a joining table enrollments
CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT NOT NULL,
    instructor TEXT
);

CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students (id),
    FOREIGN KEY (course_id) REFERENCES courses (course_id)
);

-- Sample join query to find out which courses a student is enrolled in
SELECT s.name, c.course_name FROM students s
JOIN enrollments e ON s.id = e.student_id
JOIN courses c ON e.course_id = c.course_id
WHERE s.name = 'Alice Smith';
