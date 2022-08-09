from collections import namedtuple

"""Example of class records"""

# Class id, which should uniquely identify a class
class_id = ['C1', 'C2', 'C3', 'C4']

# Year in which class took place
years = [2021, 2022]

# Teacher that thought the class 
teachers = ['T1', 'T2', 'T3']

# Touple to represent a record, each class has an id, year and a teacher
Record = namedtuple('Record', 'class_id year teacher')


# """ Creating records """

# using list comprehension
class_records = [Record(xclas, year, teach) for xclas in class_id for year in years for teach in teachers]
del class_records  # to clear the variable

# using for-loops
class_records = []
for class_id in class_id:
  for year in years:
    for teacher in teachers:
      class_records.append(Record(class_id, year, teacher))
      pass # makes it easy to comment-out the line above and have the code not break

# Both methods should have the same result
print(class_records)