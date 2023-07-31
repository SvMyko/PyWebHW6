# Homework 6

This package contains a set of Python scripts to generate a university database and fake data for it. It also contains a bunch of examples which could be used **only** with the UNIVERSITY.db file included in this package.

## Package contains:

**Tools to create a new database:**
1. create_tables.py - create a new database
2. fake_data.py - generate random names and other data for students, groups, teachers, subjects, and grades.

**Tools for working with the previously created database:**
1. UNIVERSITY.db - completed database
2. query_CALL.py - Execute the queries using the query_CALL.py script. When prompted, enter the name of the .sql file you want to execute.
   2.1 query_1.sql - Find the 5 students with the highest average grade across all subjects.
   2.2 query_2.sql - Find the student with the highest average grade in a specific subject.
   2.3 query_3.sql - Calculate the average grade for each group in a specific subject.
   2.4 query_4.sql - Calculate the overall average grade across all grades.
   2.5 query_5.sql - List the subjects taught by a specific teacher.
   2.6 query_6.sql - Find the list of students in a specific group.
   2.7 query_7.sql - Get the grades of students in a particular group for a specific subject.
   2.8 query_8.sql - Calculate the average grade given by a specific teacher across all their subjects.
   2.9 query_9.sql - Find the list of courses attended by a specific student.
   2.10 query_10.sql - Find the list of courses a specific teacher teaches to a particular student.

**Installation:**
Clone the repository to your local machine:

		_git clone https://github.com/your_username/fake_data_generation.git_

	Install the required libraries:
		_pip install faker_

**License**
	This project is licensed under the MIT License.
