import sqlite3
from contextlib import closing


def create_tables():
    with closing(sqlite3.connect("users.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute(
                '''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY,
                 title TEXT UNIQUE NOT NULL,
                 text TEXT NOT NULL
                 )
                 ''')
            connection.commit()


def insert_state(title, text):
    with closing(sqlite3.connect("users.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute('INSERT INTO users (title, text) VALUES (?, ?)', (title, text))
            connection.commit()


def select_state():
    with closing(sqlite3.connect("users.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute('SELECT * FROM users')
            return cursor.fetchall()


def remove_state(user_id):
    with closing(sqlite3.connect("users.db")) as connection:
        with closing(connection.cursor()) as cursor:
            cursor.execute('DELETE FROM users WHERE id = ?', (user_id,))
            connection.commit()


if __name__ == "__main__":
    with closing(sqlite3.connect("users.db")) as connection:

        create_tables()
        while True:
            print("Щоб додати статтю введіть + "
                  "Щоб переглянути статтю введіть * "
                  "Щоб видалити статтю введіть - ")
            command = input("Виберіть дію ")

            if command == "+":
                title = input("Назва статті: ")
                text = input("Вміст статті: ")
                insert_state(title, text)

            elif command == "*":
                users = select_state()
                if users:
                    for user in users:
                        print(user)
                else:
                    print("Статті немає додайте статтю.")

            elif command == "-":
                user_id = int(input("Введіть ID статті яку бажаєте видалити."))
                remove_state(user_id)

            else:
                print("Незрозуміла команда попробуйте ще раз")
