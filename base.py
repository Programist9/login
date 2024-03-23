# Импорты
import sqlite3
# Создание базы даных и курсор
base1 = sqlite3.connect('students.db')
cursor = base1.cursor()
# Подаём запрос на базу данных, Создание таблицы
cursor.execute('''CREATE TABLE IF NOT EXISTS students (
    student_login TEXT RRIMARY KEY,
    student_name TEXT,
    class TEXT,
    avr_score INT,
    password_to_ofice INT
)''')

# cursor.execute(''' INSERT INTO students VALUES(
#                "sasha",
#                "Саша",
#                "10-Д",
#                5,
#                1234
# )''')
# cursor.execute(''' INSERT INTO students VALUES(
#                "anya",
#                "Аня",
#                "11-А",
#                10,
#                1111
# )''')
def get_data(insert_login):
    cursor.execute(''' SELECT * FROM students WHERE student_login = (?)''', [insert_login])
    return cursor.fetchall()
base1.commit()