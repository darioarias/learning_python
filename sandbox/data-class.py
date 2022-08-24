## Python offers a few ways to build a simple class that is just a collection of fields, with little or no extra functionality. 
# That pattern is known as a “data class”—and data classes is one of the packages that supports this pattern.

# example of data classes
# collections.namedtuple - The simplest way—available since Python 2.6.
# typing.NamedTuple - An alternative that requires type hints on the fields—since Python 3.5, with class syntax added in 3.6.
# @dataclasses.dataclass - A class decorator that allows more customization than previous alternatives, 
                            # adding lots of options and potential complexity—since Python 3.7.

