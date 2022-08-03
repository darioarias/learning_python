import json
from pathlib import Path
import csv


"""Opening files using the Pathlib module"""
working_dir = Path.cwd()
# Path(working_dir/"hello.txt").touch()
path_to_file = Path(working_dir/"hello.txt")
file = path_to_file.open(mode="r", encoding="utf-8")

# accessing content line by line
for line in file:
  # print(line)
  pass

# closing the file
file.close()  # bad because if the program crashes before, it wont get closed


# use with statement so that the file closes regarless of a crash
with path_to_file.open(mode='r', encoding="utf-8") as file:
  # hash = {}

  # for char in file.read():
  #   if not(char in hash):
  #     hash[char] = 0
  #   hash[char] += 1

  # analysis_path = Path(working_dir/"analysis.json")
  # analysis_path.touch(exist_ok=True)

  # with analysis_path.open(mode="w", encoding="utf-8") as analysis:
  #   analysis.write(json.dumps(hash))
  #   print('analysis file updated')

  for line in file.readlines():
    # print(line, end="")
    pass


"""Opening files using build in 'Open'"""

# print(str(Path("hello.txt")))
open_file = open("hello.txt", mode="r", encoding="utf-8")
for line in open_file:
  # print(line)
  pass

# closing the file
open_file.close()  # bad because if the program crashes before, it wont get closed


# use with statement so that the file closes regarless of a crash
with open("hello.txt", mode="r", encoding="utf-8") as file:
  for line in file:
    # print(line)
    pass


"""Working with CSV -- comma separeted values"""


# saving data to a comma separated values file
path = Path.joinpath(Path.cwd(), 'temperatures.csv')

# path.touch()
temps = [90, 60, 67, 80, 75]
with path.open(mode='a', encoding='utf-8') as temp_file:
  temp_file.write(str(temps[0]))
  for temp in temps[1:]:
    temp_file.write(f",{temp}")

# checking to see data
with path.open(mode='r', encoding="utf-8") as temp_file:
  # print(temp_file.read())
  pass


# getting the data out of a comma separated values file and converting back to origianl data types
with path.open(mode="r", encoding='utf-8') as data_file:
  temps = [int(temp) for temp in data_file.read().split(",")]
  # print(temps)


""" Working with the CSV module """
path = Path.joinpath(Path.cwd(), "temps_w_module.csv")
path.touch()

temperatures = [
    [90, 60, 67, 80, 75],
    [88, 62, 70, 75, 90],
    [70, 65, 60, 80, 85],
    [75, 61, 66, 74, 80],
]

# writting to the file
with path.open(mode="w", encoding="utf-8") as file:
  writer = csv.writer(file)
  # for temp_list in temperatures:  # you can use writerow to write one row at a time.
  #   writer.writerow(temp_list)
  writer.writerows(temperatures)  # you can also write multiple rows at a time


# reading from a file
with path.open(mode="r", encoding="utf-8") as file:
  reader = csv.reader(file)
  for row in reader:
    # print(row)
    pass


""" Working with CSV that have headers """
# data = [
#     ["name", "department", "salary"],
#     ["Lee", "Operations", 75000.00],
#     ["Jane", "Engineering", 85000.00],
#     ["Diego", "Sales", 80000.00]
# ]

# # creating the file
# new_path = Path.joinpath(Path.cwd(), "employees.csv")
# # new_path.touch()
# # with new_path.open(mode="w", encoding="utf-8") as file:
# #   writer = csv.writer(file)
# #   writer.writerows(data)

# with new_path.open(mode='r', encoding="utf-8") as file:
#   reader = csv.DictReader(file)

#   # print(list(reader))
#   print(reader.fieldnames)


"""Friends examples"""
friends = [
  {"name": "Pepe", "city": "New York", "age": 29},
  {"name": "Rome", "city": "Boston", "age": 25},
  {"name": "Libersom", "city": "Miami", "age": 26},
]

friends_file = Path.joinpath(Path.cwd(), "friends.csv")
friends_file.touch()

with friends_file.open(mode="w", encoding="utf-8") as file:
  writer = csv.DictWriter(file, fieldnames=friends[0].keys())
  writer.writeheader()
  writer.writerows(friends)