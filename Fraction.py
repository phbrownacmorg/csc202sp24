import math
from typing import cast

class Fraction:
    """A class to represent a fraction.  Fractions are immutable,
    and are kept in lowest terms."""

    # Leading underscore means hidden from outside the class
    # (Python convention)
    def _invariant(self) -> bool:
        """Class invariant."""
        # Pre: none
        # Post: return is True iff self is a legit Fraction
        return self.denom > 0 and math.gcd(self.numr, self.denom) == 1

    def __init__(self, numerator: int, denominator: int):
        """Construct a Fraction with the given numerator 
        and denominator."""
        # Pre:
        assert denominator != 0, "Denominator cannot be 0"
        # Ensure that the denominator is positive
        if denominator < 0:
            denominator = -denominator
            numerator = -numerator
        # Reduce to lowest terms
        gcd: int = math.gcd(numerator, denominator)
        # Use of integer division depends on gcd being int
        self.numr: int = numerator // gcd
        self.denom: int = denominator // gcd
        # Post:
        assert self._invariant()

    # Query methods

    def __str__(self) -> str:
        return f'{self.numr}/{self.denom}'
    
    def getNumr(self) -> int:
        return self.numr
    
    def getDenom(self) -> int:
        return self.denom
    
    def __eq__(self, other: object) -> bool:
        """Determine whether the object OTHER is equal to self."""
        equal = True
        if not isinstance(object, Fraction):
            equal = False
        else:
            fracObj: Fraction = cast(Fraction, other)
            equal = (self.numr == other.numr
                     and self.denom == other.denom)
        return equal

    def __add__(self, other: 'Fraction') -> 'Fraction':
        return Fraction(self.numr * other.denom + other.numr * self.denom,
                        self.denom * other.denom)
