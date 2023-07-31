import sqlite3
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

def generate_data(num_students=50, num_groups=3, num_teachers=3, num_subjects=5):
    students_data = [(fake.name(), random.randint(1, num_groups)) for _ in range(num_students)]
    groups_data = [(f"Group {group_id}",) for group_id in range(1, num_groups + 1)]
    teachers_data = [(fake.name(),) for _ in range(num_teachers)]
    subjects_data = [
        ("Chemistry", random.randint(1, num_teachers)),
        ("Physics", random.randint(1, num_teachers)),
        ("Mechatronics", random.randint(1, num_teachers)),
        ("Computer_science", random.randint(1, num_teachers)),
        ("Math", random.randint(1, num_teachers))
    ]
    grades_data = [(student_id, subject_id, random.randint(1, 100), fake.date_between(start_date='-1y', end_date='today').strftime('%Y-%m-%d')) for student_id in range(1, num_students + 1) for subject_id in range(1, num_subjects + 1)]

    return students_data, groups_data, teachers_data, subjects_data, grades_data

def insert_data():
    students_data, groups_data, teachers_data, subjects_data, grades_data = generate_data()

    connection = sqlite3.connect('UNIVERSITY.db')
    cursor = connection.cursor()

    cursor.executemany('INSERT INTO students(name, group_id) VALUES (?, ?)', students_data)
    cursor.executemany('INSERT INTO groups(group_name) VALUES (?)', groups_data)
    cursor.executemany('INSERT INTO teachers(name) VALUES (?)', teachers_data)
    cursor.executemany('INSERT INTO subjects(subject_name, teacher_id) VALUES (?, ?)', subjects_data)
    cursor.executemany('INSERT INTO grades(student_id, subject_id, grade, date_received) VALUES (?, ?, ?, ?)', grades_data)

    connection.commit()
    connection.close()

if __name__ == "__main__":
    insert_data()
