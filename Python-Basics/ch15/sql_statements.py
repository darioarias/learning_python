create_people_table = """ CREATE TABLE IF NOT EXISTS People (
  FirstName TEXT,
  LastName TEXT,
  Age INT
);"""

insert_ron = """ INSERT INTO People VALUES (
  'Ron',
  'Obvious',
  42
);"""
insert_pepe = """INSERT INTO People VALUES ('Pepe', 'Agosto', 25);"""
insert_rita = """INSERT INTO People VALUES ('Rita', 'Amundo', 22);"""


get_all = """SELECT * FROM people;"""

remove_people_table = "DROP TABLE IF EXISTS People;"