

""" Upper and lower strings """

message = "The world is a Dark Place"


# print(message.lower())  # method for making a string lowercase
# print(message.upper())  # method for making a string uppercase

""" Removing white space from strings """
message2 = " only if I fail. Only then will i consider "

# print(message2.lstrip())  # removes white space from the left
# print(message2.rstrip())  # removes white space from the right
# print(message2.strip())  # removes white space from both, left and right


""" Checking starts with """
message3 = "The sky is blue"

print(message3.startswith('T'))  # check if a string starts with "T"
print(message3.endswith('e'))  # check if a string ends with "e"