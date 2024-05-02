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
    def getNode(self, data: T) -> 'BST[T]':
        """Return the node containing DATA in the tree.  Raises ValueError if
        DATA is not in the tree."""
        node = self
        if self.empty():
            raise ValueError(f'{data} is not in the tree.')
        elif data < self.data(): # type: ignore
            # Left subtree
            if not self.hasLeftChild():
                raise ValueError(f'{data} is not in the tree.')
            else:
                node = self.left().getNode(data)
        elif data > self.data(): # type: ignore
            # Right subtree
            if not self.hasRightChild():
                raise ValueError(f'{data} is not in the tree.')
            else:
                node = self.right().getNode(data)
        # already handled data == self.data()
        return node
        
    def __contains__(self, data: T) -> bool:
        """Return True if DATA is in the tree, or False otherwise."""
        present: bool = True
        try:
            node = self.getNode(data)
        except ValueError:
            present = False
        return present
    
    def findSuccessor(self) -> T:
        """Find the successor value to self.data() in an inorder traversal of the tree."""
        # Pre:
        assert self.hasRightChild(), 'No successor'
        current: BST[T] = self.right()
        while current.hasLeftChild():
            current = current.left()
        return current.data()

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

    def remove(self, data: T) -> 'BST[T]':
        """Remove the node with DATA from the tree, preserving
        the BST-ness of the tree.  Raises ValueError if DATA is
        not in the tree.  Returns the changed tree."""
        if self.empty():
            raise ValueError(f'Error: {data} was not in the tree')
        elif data < self.data(): # type: ignore
            # Left subtree
            if self.hasLeftChild():
                self._left = self.left().remove(data) # type: ignore
            else:
                raise ValueError(f'Error: {data} was not in the tree')
        elif data > self.data(): # type: ignore
            # Right subtree
            if self.hasRightChild():
                self._right = self.right().remove(data) # type: ignore
            else:
                raise ValueError(f'Error: {data} was not in the tree')
            
        else: # data == self.data(), this is the node to delete
            # Leaf
            if (not self.hasLeftChild()) and (not self.hasRightChild()):
                self._data = None # Make this node empty
                # Cut off any empty trees below
                self._left = None
                self._right = None
            # Only left child
            elif self.hasLeftChild() and (not self.hasRightChild()):
                # Copy up the child.  Order is rickety.
                self._data = self._left.data()
                self._right = self.left()._right
                self._left = self.left()._left # Has to happen last
            # Only right child
            elif self.hasRightChild() and (not self.hasLeftChild()):
                # Copy up the child.  Order is rickety.
                self._data = self._right.data()
                self._left = self.right()._left
                self._right = self.right()._right # Has to happen last
            # Two children
            else:
                self._data = self.findSuccessor()
                self._right = self.right().remove(self.data()) # Remove the successor
        return self
