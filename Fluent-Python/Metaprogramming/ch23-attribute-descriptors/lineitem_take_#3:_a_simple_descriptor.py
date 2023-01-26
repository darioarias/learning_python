# Descriptor class
## A class implementing the descriptor protocol.

# Managed class
## The class where the descriptor instances are
## declared as class attributes.

# Descriptor instance
## Each instance of a descriptor class,
## declared as a class attribute of the managed class.

# Managed instance
## One instance of the managed class.

# Storage attribute
## An attribute of the managed instance that holds
## the value of a managed attribute for that particular instance.


# Managed attribute
## A public attribute in the managed class that is handled by
## a descriptor instance, with values stored in storage attributes.

from __future__ import annotations

import typing


class Quantity:
    def __init__(self, storage_name: str) -> None:
        self.storage_name = storage_name

    def __set__(self, instance: object, value: int) -> None:
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            msg = f"{self.storage_name} must be > 0"
            raise ValueError(msg)

    def __get__(self, instance: object, owner: object) -> Quantity | int:
        if instance is None:
            return self
        else:
            return instance.__dict__[self.storage_name]
