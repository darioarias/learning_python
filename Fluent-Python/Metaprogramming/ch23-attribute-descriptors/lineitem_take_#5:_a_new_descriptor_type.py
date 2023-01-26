import abc


class Validated(abc.ABC):
    def __set_name__(self, owner: object, name: str):
        self.storage_name = name

    def __set__(self, instance: object, value: float | str) -> None:
        value = self.validate(self.storage_name, value)
        instance.__dict__[self.storage_name] = value

    @abc.abstractmethod
    def validate(self, name: str, value: float | str) -> float | str:
        """return validated value or raise ValueError"""


class Quantity(Validated):
    """a number greater than zero"""

    def validate(self, name: str, value: float) -> float:
        if value <= 0:
            raise ValueError(f"{name} must be > 0")
        return value


class NonBlank(Validated):
    """a string with at least one non-space character"""

    def validate(self, name: str, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError(f"{name} cannot be blank")
        return value
