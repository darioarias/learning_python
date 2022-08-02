""" Spoilers: Lists Are Mutable Sequences """

"""Creating Lists"""
""" A list literal looks almost exactly like a tuple literal, except that it is surrounded with square brackets ([ and ]) instead of parentheses:"""


""" List literals """


colors = ["red", "yellow", "green", "blue"]
type(colors)  # list

""" Using built in """
friends = list(("dario", "pepe", 'rome'))
type(friends)  # list

""" using split on string """
letters = "Python, C++17, JavaScript".split(",")

# print("python".split(""))  # Does not work, i wanted to split such that I get all letters

"""Updating multiple values in a list"""
colors_copy = colors
colors_copy[:3] = ["Amarillo", "Verde"]
# print(colors_copy)

""" Working with other methods """
queue = []

queue.extend(["One", "Two"])  # extend accepts a iterable param and adds the elements to the back of the list
queue.extend(("Three", "Four"))  # extend accepts a iterable param and adds the elements to the back of the list

queue.append("Five")  # append adds a value to the end of the list
queue.insert(len(queue), "Six")  # insert takes an index and adds an element at that index

last = queue.pop()  # pop removes an element at the end of the list if no index is given 
first = queue.pop(0)  # pop removes an element at a given index

# print(last, first, queue)
# print(sum([1, 2, 3]))
# print(min([1, 2, 3]))
# print(max([1, 2, 3]))

""" LIST COMPREHENSIONS """
numbers = (1, 2, 3, 4, 5)
squares = [num**2 for num in numbers]
# print(squares)