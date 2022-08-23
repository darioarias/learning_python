# since python uses the code points to sort string, 
# this yields unwanting results for langauges that do not use ASCII 


fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted(fruits)  # ['acerola', 'atemoia', 'açaí', 'caju', 'cajá']

# note that the above is not correct since accents do not change the order
# The result should be: ['açaí', 'acerola', 'atemoia', 'cajá', 'caju']

# we can use locale.strxfrm to sort
from locale import strxfrm, setlocale, LC_COLLATE

# first we set a locale 
my_locale = setlocale(LC_COLLATE, 'pt_BR.UTF-8')

# print(my_locale)  # pt_BR.UTF-8
sorted_fruits = sorted(fruits, key=strxfrm)
# print(sorted_fruits)  # ['açaí', 'acerola', 'atemoia', 'cajá', 'caju']

# Finding, you need to know the locale for the language and hope that the OS has it and is implemented correctly

## Sorting with the Unicode Collation Algorithm
import pyuca

coll = pyuca.Collator()
fruits = ['caju', 'atemoia', 'cajá', 'açaí', 'acerola']
sorted_fruits = sorted(fruits, key=coll.sort_key)
print(sorted_fruits)