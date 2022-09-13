# from strategy_pattern import Flies
# from strategy_pattern.Animal import Animal
# from strategy_pattern.animals import Dog, Duck

from flightweight_pattern.Rectangle import Rectangle


# state = Flies.CantFly()

# print(state.fly())

# animal = Animal("tiguere")
# animal.fly = Flies.CanFly()

# print(animal.fly.fly())
rec1 = Rectangle((1,2,3), (0, 0))
rec2 = Rectangle((1,2,3), (4, 0))

print(rec2.factory)
# pet = Dog('Tiguere')
# pet2 = Duck('Goose')

# print(pet2.flies())

# factory = RectangleFactory()
# factory.getColor((255, 255, 255))
# factory.getColor((255, 150, 255))
# factory.getColor((255, 255, 150))
# factory.getColor((255, 255, 150, .05))

# print(factory)