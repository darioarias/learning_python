
# reading varibales in different scopes
# Example 9-3. Function reading a local and a global variable

# b = '1'
# def f1(a):
#   print(a)
#   print(b)  # NameError: name 'b' is not defined -- if not declared above
#outside variable MUST be declared before CALLLING, not declaring, the function
# f1("2")

# Variable b is local, because it is assigned a value in the body of the function
b = 1
def f2(a):
  print(a)
  print( b)
  b = 3  # UnboundLocalError: local variable 'b' referenced before assignment
#crashes because it think b should be local
# f2(2)

b = 1
def f3(a):
  global b  # using global to tell python where to seek b
  print(a) # 2
  print(b) # 1
  b = 3

# f3(2) 
# print(b)  # 3

## using dis to look at the byte code 
from dis import dis

# print(dis(f3))
dis(f3)
print("+++++++ BREAK +++++++")
dis(f2)