# Импорты
import sqlite3
# Создание базы даных и курсор
base1 = sqlite3.connect('students.db')
cursor = base1.cursor()
# Подаём запрос на базу данных, Создание таблицы
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    student_name TEXT,
    class TEXT,
    avr_score INT,
    parents_name TEXT
)''')
# cursor.execute(''' INSERT INTO students VALUES(
#                "Саша",
#                "10-Д",
#                5,
#                "Андрей Александрович"
# )''')



# cursor.execute('''SELECT * FROM students''')
# stud = cursor.fetchall()
# for s in stud:
#     print(s[4])
# base1.commit()