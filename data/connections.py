import sqlite3

connection = sqlite3.connect("data/registers.db")
cursor = connection.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT, user_name TEXT UNIQUE NOT NULL, password TEXT NOT NULL)")
connection.commit()
connection.close()

connection2 = sqlite3.connect("data/users_notes.db")
cursor2 = connection2.cursor()
cursor2.execute("CREATE TABLE IF NOT EXISTS users_notes(user_name TEXT NOT NULL, title TEXT NOT NULL, content TEXT NOT NULL)")
connection2.commit()
connection2.close()