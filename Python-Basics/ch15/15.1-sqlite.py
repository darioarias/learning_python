import sqlite3
from sql_statements import *

# connection = sqlite3.connect("test_database.db")

# cursor = connection.cursor()

# query = "SELECT datetime('now', 'localtime');"
# data = cursor.execute(query).fetchone()


people = (
  ('Ron', "Obvious", 42),
  ("Luigi", "Vercotti", 43),
  ("Arthur", "Belling", 28)
)

with sqlite3.connect("test_database.db") as connection:
  cursor = connection.cursor()
  
  cursor.execute(create_people_table)
  # cursor.execute(insert_ron)
  # cursor.execute(insert_pepe)
  # cursor.execute(insert_rita)
  # data = cursor.execute(get_all).fetchall()
  cursor.executemany("INSERT INTO People VALUES (?, ?, ?)" , people)
  for record in cursor.execute(get_all):
    name, last_name, age = record
    print(
      f"Hello, {name} {last_name}. Hope all is well!", 
      f"Welcome to your 20s, {name}." 
      if age <= 23 
      else f"Loving your age, {age}."
    )
  cursor.execute(remove_people_table)
  # print(data)
