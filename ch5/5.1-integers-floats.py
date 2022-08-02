

"there are two ways to write number literals"
from cmath import inf


first_int=1000
secon_int=1_000

same_int = True if secon_int == first_int else False
are_same_ints = f"{first_int} and {secon_int} are {'not ' if not same_int else ''}the same" # "not" if not are_the_same else ""


first_float = 1000.0
second_float = 1_000.0
third_float = 1e3

same_float = True if (first_float == second_float) and (first_float == third_float) else False
are_same_float = f"{first_float}, {second_float} and {third_float} are{' not' if not same_float else ''} the same"



num = inf
