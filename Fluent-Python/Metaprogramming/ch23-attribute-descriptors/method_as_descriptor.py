import collections


class Text(collections.UserString):
    def __repr__(self) -> str:
        return "Text({!r})".format(self.data)

    def reverse(self):
        return self[::-1]
