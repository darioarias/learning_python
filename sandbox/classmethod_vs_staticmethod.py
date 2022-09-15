

# classmethod - used to define a method that operates on the class and not on instances
# classmethod changes the way the method is called, so it receives the class itself as the first argument, instead of an instance.
# Its most common use is for alternative constructors, like frombytes


# staticmethod - decorator [that] changes a method so that it receives no special first argument
# In essence, a static method is just like a plain function that hap‐ pens to live in a class body, 
# instead of being defined at the module level.


class Demo:
  @classmethod
  def klassmeth(*args):  # the first param is always the class
    return args 
  
  @staticmethod
  def statmeth(*args):  # no first param
    return args