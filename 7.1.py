import sqlite3
from contextlib import closing


def create_tables():
    with closing(sqlite3.connect("users.db")) as connection:
        with closing(connection.cursor()) as cursor:
            # Створення таблиці для статей
            cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
   id INTEGER PRIMARY KEY,
   login TEXT UNIQUE NOT NULL,
   password TEXT NOT NULL)
''')
