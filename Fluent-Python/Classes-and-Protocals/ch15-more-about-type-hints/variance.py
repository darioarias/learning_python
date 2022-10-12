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


# A Covariant Dispenser
# Example 15-19. covariant.py: type definitions and install function

T_co = TypeVar("T_co", covariant=True)


class BeverageDispenser(Generic[T_co]):
    def __init__(self, beverage: T_co) -> None:
        self.beverage = beverage

    def dispense(self) -> T_co:
        return self.beverage


def install(dispenser: BeverageDispenser[Juice]) -> None:
    """Install a fruit juice dispenser."""


juice_dispenser = BeverageDispenser(Juice())
install(juice_dispenser)  # valid

orange_juice_dispenser = BeverageDispenser(OrangeJuice())
install(orange_juice_dispenser)  # also valid because we are doing covariance

# still illegal
# beverage_dispenser = BeverageDispenser(Beverage())
# install(beverage_dispenser)


# A Contravariant Trash Can

# Example 15-20. contravariant.py: type definitions and install function
from typing import Generic, TypeVar


class Refuse:
    """Any refuse."""


class Biodegradable(Refuse):
    """Biodegradable refuse."""


class Compostable(Biodegradable):
    """Compostable refuse."""


T_contra = TypeVar("T_contra", contravariant=True)


class TrashCan(Generic[T_contra]):
    def put(self, refuse: T_contra) -> None:
        """Store trash until dumped."""


def deploy(trash_can: TrashCan[Biodegradable]):
    """Deploy a trash can for biodegrable refuse."""


# The following are acceptabel
bio_can: TrashCan[Biodegradable] = TrashCan()
deploy(bio_can)

trash_can: TrashCan[Refuse] = TrashCan()
deploy(trash_can)

# the following is illegal
compost_can: TrashCan[Compostable] = TrashCan()
deploy(compost_can)
