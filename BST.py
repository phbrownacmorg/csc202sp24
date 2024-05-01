from typing import cast, TypeVar
from BinTree import BinTree

T = TypeVar('T')

class BST(BinTree[T]):
    """Class to represent a binary search tree. This assumes that ==, <, and >
    are defined for type T."""

    def _invariant(self) -> bool:
        """Class invariant."""
        valid: bool = super()._invariant()
        if self.hasLeftChild():
            valid = valid and self.left()._invariant()
            valid = valid and max(self.left().inorder()) < self.data() # type: ignore
        if self.hasRightChild():
            valid = cast(bool, valid and self.right()._invariant())
            valid = valid and min(self.right().inorder()) > self.data() # type: ignore
        return cast(bool, valid)

    def BST(self, data: T | None = None): # type: ignore
        """Construct a BST with no children and data DATA."""
        super().__init__(data)

    # Query methods
    def __contains__(self, data: T) -> bool:
        """Return True if DATA is in the tree, or False otherwise."""
        present: bool = False # Handles the empty tree
        if not self.empty():
            if data == self.data():
                present = True
            elif data < self.data(): # type: ignore
                # Left subtree
                if not self.hasLeftChild():
                    present = False
                else:
                    present = (data in self.left()) # type: ignore
            else: # data > self.data(), right subtree
                if not self.hasRightChild():
                    present = False
                else:
                    present = (data in self.right()) # type: ignore
        return cast(bool, present)

    # Mutator methods
    def add(self, data: T) -> None:
        """Add a node to the BST."""
        if self.empty():
            self._data = data
        elif data < self.data(): # type: ignore
            # Add to the left subtree
            if not self.hasLeftChild():
                self._left = BST[T](data)
            else:
                cast(BST[T], self.left()).add(data)
        elif data > self.data(): # type: ignore
            # Add to the right subtree
            if not self.hasRightChild():
                self._right = BST[T](data)
            else:
                cast(BST[T], self.right()).add(data)
