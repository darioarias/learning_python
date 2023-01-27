

# type: The Built-In Class Factory

class MySuperClass:
    pass 

class MyMixin:
    pass
# class MyClass(MySuperClass, MyMixin):
#     x = 42 

#     def x2(self):
#         return self.x * 2



MyClass = type('MyClass', (MySuperClass, MyMixin), {'x': 42, 'x2': lambda self: self.x * 2})
t = MyClass()
print(t.x2())
