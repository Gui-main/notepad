import sqlite3
import os
from time import sleep

class Functions():
  def __init__(self):
    users_notes = os.path.abspath(os.path.join(os.getcwd(), 'notepad', 'data', 'users_notes.db'))
    self.connection = sqlite3.connect(users_notes)
    self.cursor = self.connection.cursor()
    
    
  def view_titles(self, name):
    try:
      self.cursor.execute("SELECT title FROM users_notes WHERE user_name = ?", (name,))
      title_notes = self.cursor.fetchall()
      print('Loading...')
      sleep(1.2)
      if title_notes:
        print('Your notes.')
        for note in title_notes:
          print(f'-> {note}')
      else:
        print('You no have notes.')
    except Exception:
      print('Error...')
      
   
  def view_note(self, name):
  	try:
  		title = str(input('Title of note: '))
  		self.cursor.execute('SELECT content FROM users_notes WHERE user_name = ? AND title = ?', (name, title))
  		content = self.cursor.fetchone()
  		if content:
  			print('Loading...')  			
  			sleep(1.2)
  			print(f'-> {title} \n\n -> {content}\n')
  		else:
  			print('Loading...')
  			sleep(1.2)
  			print('This note does not exist.')   
  	except Exception:
  		print('Error...')
      
      
  def remove_note(self, name):
    try:
      rem_note = str(input('Which note would you like to delete?\n>>> ')).lower()
      self.cursor.execute('SELECT title FROM users_notes WHERE user_name = ?', (name,))
      if self.cursor.fetchone():
        self.cursor.execute('DELETE FROM users_notes WHERE user_name = ? AND title = ?', (name, rem_note,))
        self.connection.commit()
        self.connection.close()
        print('Loading...')
        sleep(1.2)
        print('Done!')
      else:
        print('Loading...')
        sleep(1.2)
        print('This note does not exist.')
    except Exception:
      print('Error...')
      
  
  def add_note(self, name):
    try:
      title = str(input('>>> Note Title: ')).lower()
      content = str(input('>>> Note content: ')).lower()
      self.cursor.execute('INSERT INTO users_notes(user_name, title, content) VALUES (?, ?, ?)', (name, title, content))
      self.connection.commit()
      self.connection.close()
      print('Loading...')
      sleep(1.2)
      print('Done!')
    except Exception:
      print('Error...')