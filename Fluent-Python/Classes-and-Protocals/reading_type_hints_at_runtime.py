# given the following function
def clip(text: str, max_len: int = 80) -> str:
    ...


# The type hints are stored as a dict in the __annotations__ attribute of the function:
# print(
#     clip.__annotations__
# )  # {'text': <class 'str'>, 'max_len': <class 'int'>, 'return': <class 'str'>}


# Problems with Annotations at Runtime
# The increased use of type hints raised two problems:
## Importing modules uses more CPU and memory when many type hints are used.
## Referring to types not yet defined requires using strings instead of actual types.

# class Rectangle:
#     # ... lines omitted ...
#     def stretch(self, factor: float) -> 'Rectangle':
#     return Rectangle(width=self.width * factor)

# using type hint as string
# get_type_hints(obj, globals=None, locals=None, include_extras=False) -> inspect.get_annotations(...)
## [...] This is often the same as obj.__annotations__.
## In addition, forward refer‐ ences encoded as string
## literals are handled by evaluating them in globals and locals namespaces. [...]


# start module with `from __future__ import annotations` to that annotation
# are no longer evaluated at function definition time.
# Instead, they are preserved in annotations in string form.


## Dealing with the Problem

# Given the unstable situation at present, if you need to read annotations at runtime, I recommend
## Avoid reading __annotations__ directly; instead,
## use inspect.get_annota tions (from Python 3.10) or typing.get_type_hints (since Python 3.5).

## Write a custom function of your own as a thin wrapper around inspect
## .get_annotations or typing.get_type_hints, and have the rest of your
## codebase call that custom function, so that future changes are localized to a single function.
