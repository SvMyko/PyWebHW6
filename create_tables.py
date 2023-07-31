import sqlite3
from sqlite3 import DatabaseError
from contextlib import contextmanager
from sql_creation_request import sql_table_request
'''
sql_table_request :
    students (student_id, name, group_id)
    groups (group_id, group_name)
    teachers (teacher_id, name)
    subjects (subject_id, subject_name, teacher_id)
    grades (grade_id, student_id, subject_id, grade, date_recieved)
'''

@contextmanager
def create_connection():
    connection = None
    try:
        connection = sqlite3.connect("UNIVERSITY.db")
        yield connection
    except Exception as error:
        print(error)
        connection.rollback()
    finally:
        connection.close()

def create_table(connect, sql_create_table):
    try:
        cursor = connect.cursor()
        cursor.executescript(sql_create_table)
    except DatabaseError as error:
        print(error)


if __name__ == "__main__":

    with create_connection() as connect:
         if connect is not None:
            create_table(connect, sql_table_request)
         else:
            print("connection lost")
