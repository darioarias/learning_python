

""" String Concat """
str1 = "Hello"
str2 = "Word"

# print(f'{str1}, {str2}')
# print(str1 + " " + str2)


""" String Indexing """
str3 = str1 + ", " + str2

# print(str3, "<<>>", str3[0])


""" String Slicing """
second_word = str3[7:]
first_word = str3[:5]

# H e l l o ,   W o r d
# 0 1 2 3 4 5 6 7 8 9 10

#  H  e  l  l  o  ,     W  o  r  d
#-11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1


str3_copy = str3[:]
second_word_reverse = str3_copy[0:]

# print(second_word_reverse)


""" Strings are immutable """

message_str = "Park"
# message_str[0] = 'D'  # will create an error because strings cannot be changed: TypeError: 'str' object does not support item assignment
new_message = 'D' + message_str[1:]
print(new_message)