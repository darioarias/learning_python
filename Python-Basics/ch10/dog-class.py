


class Dog(object):
  species = "Canis familiaris"
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def __str__(self):
    return f"Hello I'm {self.name}. I am currently {self.age} years old"

  def speak(self, sound):
    return f"{self.name} barks: {sound}"

class JackRussellTerrier(Dog):
  def speak(self, sound="Arf"):
    return super().speak(sound)

class Dachshund(Dog):
  pass 

class Bulldog(Dog):
  pass


miles = JackRussellTerrier("Miles", 4) 
buddy = Dachshund("Buddy", 9)
jack = Bulldog("Jack", 3) 
jim = Bulldog("Jim", 5)

print(miles.speak())