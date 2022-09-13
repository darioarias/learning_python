from strategy_pattern import Flies
from strategy_pattern.Animal import Animal
from strategy_pattern.animals import Dog, Duck

# state = Flies.CantFly()

# print(state.fly())

# animal = Animal("tiguere")
# animal.fly = Flies.CanFly()

# print(animal.fly.fly())

pet = Dog('Tiguere')
pet2 = Duck('Goose')

print(pet2.flies())