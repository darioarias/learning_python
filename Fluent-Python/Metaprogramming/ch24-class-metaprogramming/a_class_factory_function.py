from collections.abc import Iterable, Iterator
from typing import Any, Union

FieldNames = Union[str, Iterable[str]]


def record_factory(cls_name: str, field_names: FieldNames) -> type[tuple]:
    slots = parse_identifiers(field_names)

    def __init__(self, *args, **kwargs) -> None:
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)

        for name, value in attrs.items():
            setattr(self, name, value)

    def __iter__(self) -> Iterator[Any]:
        for name in self.__slots__:
            yield getattr(self, name)

    def __repr__(self) -> str:
        values = ", ".join(
            f"{name}={value!r}" for name, value in zip(self.__slots__, self)
        )

        cls_name = self.__class__.__name__
        return f"{cls_name}({values})"

    cls_attrs = dict(
        __slots__=slots,
        __init__=__init__,
        __iter__=__iter__,
        __repr__=__repr__,
    )

    print(cls_attrs)

    return type(cls_name, (object,), cls_attrs)


# def record_factory(cls_name: str, field_names: FieldNames) -> type[tuple]:
#     slots = parse_identifiers(field_names)

#     def __init__(self, *args, **kwargs) -> None:
#         attrs = dict(zip(self.__slots__, args))
#         attrs.update(kwargs)
#         for name, value in attrs.items():
#             setattr(self, name, value)

#     def __iter__(self) -> Iterator[Any]:
#         for name in self.__slots__:
#             yield getattr(self, name)

#     def __repr__(self):
#         values = ", ".join(
#             f"{name}={value!r}" for name, value in zip(self.__slots__, self)
#         )
#         cls_name = self.__class__.__name__
#         return f"{cls_name}({values})"

#     cls_attrs = dict(
#         __slots__=slots,
#         __init__=__init__,
#         __iter__=__iter__,
#         __repr__=__repr__,
#     )

#     return type(cls_name, (object,), cls_attrs)


def parse_identifiers(names: FieldNames) -> tuple[str, ...]:
    if isinstance(names, str):
        names = names.replace(",", " ").split()

    if not all(s.isidentifier() for s in names):
        raise ValueError("names must all be valid identifiers")

    return tuple(names)


# def parse_identifiers(names: FieldNames) -> tuple[str, ...]:
#     if isinstance(names, str):
#         names = names.replace(",", " ").split()
#     if not all(s.isidentifier() for s in names):
#         raise ValueError("names must all be valid identifiers")
#     return tuple(names)


Perro = record_factory("Dog", "name weight owner")

print(Perro)
