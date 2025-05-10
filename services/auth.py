import sqlite3
from .menu import Menu
import os

class Auth():
  def __init__(self):
    registers = os.path.abspath(os.path.join(os.getcwd(), 'notepad', 'data', 'registers.db'))
    self.connection = sqlite3.connect(registers)
    self.cursor = self.connection.cursor()
    
  @staticmethod
  def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
  
  def user(self):
      print('═' * 40)
      print('NOTEPAD FOR TERMINAL'.center(40))
      while True:
        try:
            print('═' * 40)
            option = str(input("""
╔════════════════════════════════════╗
║               MAIN MENU            ║      
  ══════════════════════════════════
║ [1] Login                          ║      
║ [2] Register new user              ║      
║ [3] Exit                           ║      
╚════════════════════════════════════╝
>>> """))
            print('═' * 40)
            if '1' in option:
              name = str(input('>>> Username: '))
              password = str(input('>>> Password: '))
              self.cursor.execute("SELECT user_name, password FROM users WHERE user_name = ? AND password = ?", (name, password,))
              if self.cursor.fetchone():
                while True:
                  m = Menu()
                  m.Options(name)
                  print('═' * 40)
              else:
                Auth.clear()
                print('Invalid login.')
            elif '2' in option:
                name = input('>>> Name: ').capitalize()
                self.cursor.execute("SELECT user_name FROM users WHERE user_name = ?", (name,))
                if self.cursor.fetchone():
                    print('This username has already token.')
                password = input('>>> Password: ')
                self.cursor.execute("INSERT INTO users (user_name, password) VALUES (?, ?)", (name, password))
                self.connection.commit()
                print('User registered sucessfully.')
            elif '3' in option:
              break
            else:
              Auth.clear()
              print("Invalid option.")
        except Exception:
            print('Error...')
            self.connection.close()