"""10.4 Challenge: Model a Farm"""


class Animal(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def __str__(self) -> str:
    return f"Hello I'm {self.name}"
  
  def greet(self, mood: str):
    if mood.lower() == "indeferent":
      return "Meh, hello" 
    if mood.lower() == "happy":
      return "HEY there! How are you!?"
    if mood.lower() == "angry":
      return "What do you want?"

class Cow(Animal):
  def greet(self, mood='happy'):
    return super().greet(mood)

class Horse(Animal):
  def greet(self, mood="indeferent"):
    return super().greet(mood)

class Pig(Animal):
  def greet(self, mood="angry"):
    return super().greet(mood)



pig = Pig("piggie", 10)
cow = Cow("Madams", 40)
horse = Horse("Punny", 20)

print(isinstance(pig, Cow))