from __future__ import annotations

import typing


class Quantity:
    def __set_name__(self, owner: object, name: str) -> None:  # 1
        self.storage_name = name  # 2

    def __set__(self, instance: object, value: float) -> None:  # 3
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            msg = f"{self.storage_name} must be > 0"
            raise ValueError(msg)

    # no __get__ needed # 4


class LineItem:
    weight = Quantity()  # 5
    price = Quantity()

    def __init__(self, description: str, weight: float, price: float) -> None:
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self) -> float:
        assert isinstance(self.weight, float)
        assert isinstance(self.price, float)

        return self.weight * self.price
