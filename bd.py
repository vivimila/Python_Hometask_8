#создание базы данных

import sqlite3

connect = sqlite3.connect("studens.bd")
curcor = connect.cursor()

curcor.execute("""CREATE TABLE studens(
    id_student INTEGER,
    name_student TEXT,
    age_students INTEGER
)
""")

connect.commit()