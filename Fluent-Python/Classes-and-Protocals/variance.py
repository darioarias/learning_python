# An Invariant Dispenser

# Example 15-18. invariant.py: type definitions and install function
from typing import Generic, TypeVar


class Beverage:
    """Any beverage."""


class Juice(Beverage):
    """Any fruit juice."""


class OrangeJuice(Juice):
    """Delicious juice from Brazilian oranges."""


T = TypeVar("T")


class BeverageDispenser(Generic[T]):
    """A dispenser parameterized on the beverage type."""

    def __init__(self, beverage: T) -> None:
        self.beverage = beverage

    def dispense(self) -> T:
        return self.beverage


def install(dispenser: BeverageDispenser[Juice]) -> None:
    """Install a fruit juice dispenser."""


juice_dispenser = BeverageDispenser(Juice())
install(juice_dispenser)

# the following is illegal
# beverage_dispenser = BeverageDispenser(Beverage())
# install(beverage_dispenser)

# the following is also illegal, note though that orangejuice is of type juice
# orange_juice_dispenser = BeverageDispenser(OrangeJuice())
# install(orange_juice_dispenser)
