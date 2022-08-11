"""
How to make dictionary of 1st and 4th column of the table in the txt file here:
"""


"""

| ID  | Name    | Work    | Rate | Friends |
|-----|---------|---------|------|---------|
| 123 | John    | Writer  |   15 |      34 |
|     |         |         |      |         |
| 124 | Greene  | Doctor  |   53 |      76 |
|     |         |         |      |         |
| 125 | Stephen | Jobless |   86 |      86 |
|     |         |         |      |         |
| 126 | King    | Doctor  |   24 |      14 |
|     |         |         |      |         |
| 127 | Sal     | Writer  |   68 |      98 |
|     |         |         |      |         |
| 128 | Harp    | Teacher |   57 |       4 |
|     |         |         |      |         |
| 129 | Lee     | Pilot   |   48 |       2 |
|     |         |         |      |         |
| 130 | Ted     | Labor   |   96 |      68 |
|     |         |         |      |         |
| 131 | Zusak   | Doctor  |   85 |      98 |
|     |         |         |      |         |
| 132 | Mark    | Jobless |   35 |      24 |
|     |         |         |      |         |
| 133 | Twain   | Jobless |   75 |      98 |


"""

# from pathlib import Path
# file_path = Path.joinpath(Path.cwd(), 'data_.csv')


# with file_path.open(mode="r", encoding="utf-8") as file:
#   for line in file.readline():
#     print(line)


import csv  # module which makes it easy to work with csv files. 
from pathlib import Path  # module to work with paths. Provides reach support for file creating as well
from collections import namedtuple  # subclass of tuple, allows for fields to be named


file_path = Path.joinpath(Path.cwd(), 'data_.csv')  # represents the location for the file with the data
Record = namedtuple('Record', ['ID', 'Rate'])  # creates a represenation of what a record should look like

with file_path.open(mode="r", encoding="utf-8") as file:  # open file with an 'with' statement so that file closes when going out of scope
  reader = csv.DictReader(file)  # uses a DictReader class to manage the file
  fields = {'ID': [], 'Rate': []}  # an idea on how to represent your data. => {ID: [1, 2, 3,...], Rate: [10.00, 20.00,...]}
                                   # I don't like this because the association between ID and Rates is lost. 
                                   # Especially if at any moment fields['ID'] or fields['Rate'] changes.
  dict_list = []  # another idea on how to store your data. Example: [(Id, Rate), (Id, Rate), (Id, Rate)]. 
                  # I like this because the connection between Ids and Rates are kept

  for row in reader:  # use the reader obj to iterate through each line
    id, *_, rate, _ = row.values()  # grab the values for each row and unpack them, only grabbing what we need
    #saving to fields
    fields["ID"].append(id)
    fields["Rate"].append(rate)
    #saving to our list
    dict_list.append(Record(id, rate))
    
  print(fields)
  print(dict_list)

