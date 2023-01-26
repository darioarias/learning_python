import collections


class Text(collections.UserString):
    def __repr__(self) -> str:
        return "Text({!r})".format(self.data)

    def reverse(self):
        return self[::-1]


word = Text("123")

# print(repr(word))
# print(word.reverse())

my_func = Text.reverse.__get__(None, Text)
# print(Text.reverse(Text("123")))

print(my_func((1, 2, 3)))
