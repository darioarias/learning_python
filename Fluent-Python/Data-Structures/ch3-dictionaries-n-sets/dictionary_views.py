

# The dict instance methods .keys(), .values(), and .items() return 
# instances of classes called dict_keys, dict_values, and dict_items, respectively.


# The .values() method returns a view of the values in a dict
d = dict(a=10, b=20, c = 30)
values = d.values()  # dict_values([10, 20, 30])
len(values)  # 3
list(values)  # [10, 20, 30]
reversed(values)  # <dict_reversevalueiterator object at <memo-address>>
# values[0]  # TypeError: 'dict_values' object is not subscriptable


# A view object is a dynamic proxy. If the source dict is updated, 
# you can immediately see the changes through an existing view. 
d['z'] = 99
d  # {'a': 10, 'b': 20, 'c': 30, 'z': 99}
values  # dict_values([10, 20, 30, 99])



# The classes dict_keys, dict_values, and dict_items are internal: 
# they are not avail‐ able via __builtins__ or any standard library module, a
# nd even if you get a reference to one of them, 
# you can’t use it to create a view from scratch in Python code:

values_class = type({}.values())
# v = values_class()  # TypeError: cannot create 'dict_values' instances

