import pathlib

current_working_dir = pathlib.Path.cwd()  # getting the currrent working directory
current_file = current_working_dir/"12.2-working-w-file-paths.py"  # Extending path using /

"""Checking if the path is absolute"""
current_file.is_absolute()  # true

relative_path = pathlib.Path(".")
relative_path.is_absolute()  # false

# printing all the files in the current directory
for file in relative_path.iterdir():
  # print(file)
  pass

# printing all the parents of a file
# print(list(pathlib.Path(pathlib.Path.home()).parents))

#  looping through the parents
for parent in pathlib.Path(pathlib.Path.cwd()).parents:
  # print(parent)
  pass

# look at the root using anchor
# current_working_dir = pathlib.Path(".")  # overwrites path to relative path
# print(
#   current_working_dir.anchor 
#   if current_working_dir.is_absolute()
#   else "anchor not available since path is not absolute"
# )  # print the anchor (root) or a feeback message

# printing the name a path points to, stem and suffix
# print(current_file.name)  # 12.2-working-w-file-paths.py
# print(current_file.stem)  # prints the stems of the file
# print(current_file.suffix)  # prints the suffix of the file

# checking if a path exist
# wrong_path = pathlib.Path(current_working_dir/"does_not_exist.py")

# checking if a path is a file or directory 
# print(current_working_dir.is_file())  # false 
# print(pathlib.Path(current_working_dir/"12.2-working-w-file-paths.py").is_file())  # true

# print(current_working_dir.is_dir())  # true 
# print(pathlib.Path(current_working_dir/"12.2-working-w-file-paths.py").is_dir())  # false