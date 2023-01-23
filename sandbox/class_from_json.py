import json
import typing
from reprlib import repr


class Event(typing.Protocol):
    name: str
    description: str
    categories: list[str]


class EventWrapper:
    pass


EVENTS = []

with open("events.json", "r") as file:
    events = json.load(file)

    for event in events:
        EVENT = EventWrapper()
        for key in event:
            setattr(EVENT, key, event[key])
        EVENTS.append(EVENT)


def print_event_info(event: Event) -> None:
    print(f"\t{event.name}\n{repr(event.description)}, \n{event.categories[0]}")
    print()


for event in EVENTS:
    print_event_info(event)
