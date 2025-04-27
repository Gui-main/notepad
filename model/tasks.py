import sqlite3

from time import sleep

class Tasks():
  def __init__(self):
    users_tasks = 'data/users_tasks.db'
    self.connection = sqlite3.connect(users_tasks)
    self.cursor = self.connection.cursor()
    
    
  def view_tasks(self, name):
    try:
      self.cursor.execute("SELECT title, content FROM users_tasks WHERE user_name = ?", (name,))
      title_tasks = self.cursor.fetchall()
      print('Loading...')
      sleep(1.2)
      if title_tasks:
        print('Your tasks.')
        for task, content in title_tasks:
          print(f'{task} - {content}')
      else:
        print('You no have tasks.')
    except Exception:
      print('Error...')
      
    
  def remove_task(self, name):
    try:
      print('═' * 40)
      rem_task = str(input('Which task would you like to delete?\n>>> ')).lower()
      self.cursor.execute('SELECT title FROM users_tasks WHERE user_name = ?', (name,))
      if self.cursor.fetchone():
        self.cursor.execute('DELETE FROM users_tasks WHERE user_name = ? AND title = ?', (name, rem_task,))
        self.connection.commit()
        self.connection.close()
        print('Loading...')
        sleep(1.2)
        print('Done!')
      else:
        print('Loading...')
        sleep(1.2)
        print('This task does not exist.')
    except Exception:
      print('Error...')
      
  
  def add_task(self, name):
    try:
      title = str(input('>>> Task Title: ')).lower()
      content = str(input('>>> task content: ')).lower()
      self.cursor.execute('INSERT INTO users_tasks(user_name, title, content) VALUES (?, ?, ?)', (name, title, content))
      self.connection.commit()
      self.connection.close()
      print('Loading...')
      sleep(1.2)
      print('Done!')
    except Exception:
      print('Error...')