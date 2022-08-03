from pathlib import Path

"""Creating directories and Files"""
working_dir = Path.cwd()

new_dir = working_dir/"testing_dir-dy"

if not new_dir.exists():
  new_dir.mkdir(exist_ok=True)


"""Searching Files"""
paths = working_dir.glob("*.py")
print(list(paths))