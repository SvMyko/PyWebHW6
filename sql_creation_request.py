sql_table_request = """
    CREATE TABLE IF NOT EXISTS students (
        student_id INTEGER PRIMARY KEY,
        name VARCHAR(32),
        group_id INT
    );

    CREATE TABLE IF NOT EXISTS groups (
        group_id INTEGER PRIMARY KEY,
        group_name VARCHAR(32)  
    );  

    CREATE TABLE IF NOT EXISTS teachers (
        teacher_id INTEGER PRIMARY KEY,
        name VARCHAR(50)
    );

    CREATE TABLE subjects (
        subject_id INTEGER PRIMARY KEY,
        subject_name VARCHAR(32),
        teacher_id INT
    );

    CREATE TABLE grades (
        grade_id INTEGER PRIMARY KEY,
        student_id INT,
        subject_id INT,
        grade INT,
        date_received DATE
        )              
"""