from typing import cast, Generic, TypeVar
from BinTree import BinTree

T = TypeVar('T')

class BST(BinTree[T]):
    """Class to represent a binary search tree. This assumes that ==, <, and >
    are defined for type T."""

    def _invariant(self) -> bool:
        valid = super()._invariant()
        if self.hasLeftChild():
            valid = valid and self._left._invariant()
            # Weak! Doesn't cover the entire subtree.  Use max of subtree.
            valid = valid and self._left.data() < self.data()
        if self.hasRightChild():
            valid = valid and self._right._invariant()
            # Weak! Doesn't cover the entire subtree.  Use min of subtree.
            valid = valid and self._right.data() > self.data()
        return valid

        