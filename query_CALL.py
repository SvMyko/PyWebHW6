import sqlite3


def execute_query(sql_query):
    connection = sqlite3.connect('UNIVERSITY.db')
    cursor = connection.cursor()
    cursor.execute(sql_query)
    result = cursor.fetchall()
    print(result)
    connection.commit()
    connection.close()


if __name__ == "__main__":
    try:
        input_query = input('Input sql query file name (ex. "query_1.sql"): ')
        with open(input_query, 'r') as file:
            sql_query = file.read()
        execute_query(sql_query)
    except FileNotFoundError:
        print("File not found")