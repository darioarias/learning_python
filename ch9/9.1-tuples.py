
""" Creating Tuples """


"""Tuple Literals"""
my_first_tuple = (1, 2, 3)  # valid tuple
my_second_tuple = (1, 2.0, "three")  # also valid tuple


empty_tuple = ()  # the empty tuple in case there is no solution

single_tuple = (1,)  # creating a tuple with one element


""" Using Built in: The tuple() Built-In """
my_built_in_tuple = tuple([1, 'two', 3.0])

# print(my_built_in_tuple)


""" Tuples Attributes """
"""Tuples Have a Length"""
numbers = (1, 2, 3, 4, 5)
len(numbers)  # 3

"""Tuples Support Indexing and Slicing"""
name = tuple('Dario')
# print(name[:2][0])

"""Tuples Are Immutable"""
values = numbers[:3]
# values[0] = 0  # creates a TypeError exception
# print(values)



"""Tuple Packing and Unpacking"""
"""Another way to create tuple - AKA packing values"""
coordinates = 4.21, 9.29
type(coordinates)  # tuple

"""Unpacking values"""
x, y = coordinates