"""
Write a script named first_letter.py that first prompts the user 
for input by using the string "Tell me your password:" 
The script should then determine the first letter of the user’s input, 
convert that letter to upper-case, and display it back.

For example, if the user input is "no" then the program should respond like this:
The first letter you entered was: N

For now, it’s okay if your program crashes when the user enters noth- ing as input—that is, 
they just hit Enter instead of typing something in. You’ll learn about a couple of ways 
you can deal with this situation in an upcoming chapter.
"""

user_pwd = input("Tell me your password:")

print(f'the first letter you entered was: {user_pwd[0].upper()}')