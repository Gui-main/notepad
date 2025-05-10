import sqlite3
import os 

path = os.path.abspath(os.path.join(os.getcwd(), 'notepad', 'data', 'registers.db'))
connection = sqlite3.connect(path)
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, user_name TEXT UNIQUE NOT NULL, password TEXT NOT NULL)")
connection.commit()
connection.close()

path2 =os.path.abspath(os.path.join(os.getcwd(), 'notepad', 'data', 'users_notes.db'))
connection2 = sqlite3.connect(path2)
cursor2 = connection2.cursor()
cursor2.execute("CREATE TABLE IF NOT EXISTS users_notes(user_name TEXT NOT NULL, title TEXT NOT NULL, content TEXT NOT NULL)")
connection2.commit()
connection2.close()