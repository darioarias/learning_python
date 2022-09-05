## Scope recap

def closure():
  # closure scope
  item_tacker = []
  def action(item):
    # free variable scope -- creating new vars remove them from being free vars
    item_tacker.append(item)
    return item_tacker[-1] 
  return action

tracker = closure()  # tracker now has a reference to 'action'
tracker('Dario')  # the same as doing "action('dario')"

# Example 9-12. A broken higher-order function to calculate a running average without keeping all history
def make_averager():
  count, total = 0, 0

  def averager(new_count):
    nonlocal count, total
    count += 1
    total += new_count

    return total / count
  
  return averager

avg = make_averager()

# Variable Lookup Logic
# Rule for looking up variables in a funciton
## If there is a global x declaration, x comes from and is assigned to the x global variable module.
## If there is a nonlocal x declaration, x comes from and is assigned to the 
##   x local variable of the nearest surrounding function where x is defined
## If x is a parameter or is assigned a value in the function body, then x is the local variable.
## If x is referenced but is not assigned and is not a parameter:
##   x will be looked up in the local scopes of the surrounding function bodies
##    (nonlocal scopes)
##   If not found in surrounding scopes, it will be read from the module global scope.
##   If not found in the global scope, it will be read from __builtins__.__dict__.