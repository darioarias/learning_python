import inspect
import json
from functools import cache, cached_property

JSON_PATH = "osconfeed.json"


class Record:
    __index = None

    def __init__(self, **kwargs) -> None:
        self.__dict__.update(kwargs)

    def __repr__(self) -> str:
        return f"<{self.__class__.__name__} serial={self.serial!r}>"

    @staticmethod
    def fetch(key):
        if Record.__index is None:
            Record.__index = load()
            return Record.__index[key]


class Event(Record):
    def __init__(self, **kwargs) -> None:
        self.__speaker_objs = None
        super().__init__(**kwargs)

    def __repr__(self) -> str:
        try:
            return f"<{self.__class__.__name__} {self.name!r}>"
        except AttributeError:
            return super().__repr__()

    @cached_property
    def venue(self):
        key = f"venue.{self.venue_serial}"
        return self.__class__.fetch(key)

    @property
    @cache
    def speakers(self):
        spkr_serials = self.__dict__["speakers"]
        fetch = self.__class__.fetch
        return [fetch(f"speaker.{key}") for key in spkr_serials]


def load(path: str = JSON_PATH) -> dict[str, Record]:
    records: dict[str, Record] = {}

    with open(path) as fp:
        raw_data = json.load(fp)

    for collection, raw_records in raw_data["Schedule"].items():
        record_type: str = collection[:-1]  # 1
        cls_name = record_type.capitalize()  # 2
        cls = globals().get(cls_name, Record)  # 3

        if inspect.isclass(cls) and issubclass(cls, Record):  # 4
            factory = cls  # 5
        else:
            factory = Record  # 6

        for raw_record in raw_records:  # 7
            key = f'{record_type}.{raw_record["serial"]}'
            records[key] = factory(**raw_record)  # 8

    return records


# print(load())
