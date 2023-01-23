class LineItem:
    def __init__(self, description: str, weight: float, price: float) -> None:
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    @property
    def weight(self) -> float:
        return self.__weight

    @weight.setter
    def weight(self, value: float) -> None:
        if value > 0:
            self.__weight = value
        else:
            raise ValueError("weight must be greater than 0")


# A Proper Look at Properties
class LineItem_legacy:
    def __init__(self, description: str, weight: float, price: float) -> None:
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self) -> float:
        return self.weight * self.price

    def get_weight(self) -> float:
        return self.__weight

    def set_weight(self, value: float) -> None:
        if value > 0:
            self.__weight = value
        else:
            raise ValueError("Weight must be greater than 0")

    weight = property(get_weight, set_weight, doc="weight in kilograms")


# Properties Override Instance Attributes

# Documentation
class Foo:
    @property
    def bar(self):
        """The bar attribute"""
        return self.__dict__["bar"]

    @bar.setter
    def bar(self, value):
        self.__dict__["bar"] = value
