#создание базы данных

import sqlite3

connect = sqlite3.connect("students.bd")
curcor = connect.cursor()

curcor.execute('''CREATE TABLE students(
    id_student INTEGER,
    name_student TEXT,
    age_students INTEGER
)
''')

connect.commit()

students_list = [1, "Vlad", 20]
curcor.execute('INSERT INTO students VALUES(?,?,?); students_list')
connect.commit()