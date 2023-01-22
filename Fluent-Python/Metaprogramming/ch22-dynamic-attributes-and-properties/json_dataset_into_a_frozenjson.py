import json
import keyword
from collections import abc


class FrozenJSON:
    """A read-only facade for navifating a JSON-like object\
        using attribute notation"""

    def __new__(cls, arg):
        if isinstance(arg, abc.Mapping):
            return super().__new__(cls)
        elif isinstance(arg, abc.MutableSequence):
            return [cls(item) for item in arg]
        else:
            return arg

    def __init__(self, mapping) -> None:
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += "_"
            self.__data[key] = value

    def __getattr__(self, name):
        try:
            return getattr(self.__data, name)
        except AttributeError:
            return FrozenJSON(self.__data[name])

    def __dir__(self):
        return self.__data.keys()

    # @classmethod
    # def build(cls, obj):
    #     if isinstance(obj, abc.Mapping):
    #         return cls(obj)
    #     elif isinstance(obj, abc.MutableSequence):
    #         return [cls.build(item) for item in obj]
    #     else:
    #         return obj


student = FrozenJSON(
    {
        "events": [
            {
                "serial": 33451,
                "name": "Migrating to the Web Using Dart and Polymer - A Guide for Legacy OOP Developers",
                "event_type": "40-minute conference session",
                "time_start": "2014-07-23 17:00:00",
                "time_stop": "2014-07-23 17:40:00",
                "venue_serial": 1458,
                "description": "The web development platform is massive. With tons of libraries, frameworks and concepts out there, it might be daunting for the &#x27;legacy&#x27; developer to jump into it.\r\n\r\nIn this presentation we will introduce Google Dart &amp; Polymer. Two hot technologies that work in harmony to create powerful web applications using concepts familiar to OOP developers.",
                "website_url": "http://oscon.com/oscon2014/public/schedule/detail/33451",
                "speakers": [149868],
                "categories": ["Emerging Languages"],
            }
        ]
    }
)
