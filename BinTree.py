from typing import cast, Generic, TypeVar

T = TypeVar('T')

class BinTree(Generic[T]):
    """Class to represent a binary tree.  An empty tree is represented
    as (a) a node with no data and no children *if* it is the root, or
    (b) None if it is not the root."""

    def _invariant(self) -> bool:
        """Class invariant."""
        valid = True
        if self._data is None: # if this is the root of an empty tree
            if self._left is not None or self._right is not None:
                valid = False
        return valid

    def __init__(self, data: T | None = None):
        self._data: T | None = data
        self._left: BinTree[T] | None = None
        self._right: BinTree[T] | None = None
        assert self._invariant()

    # Query methods
    def empty(self) -> bool:
        """Check for an empty tree.  Only works fully at the root (because lower
        down there is no self, just None)."""
        return self._data is None and self._left is None and self._right is None

    def hasLeftChild(self) -> bool:
        """Does this node have a left child?"""
        return self._left is not None
    
    def hasRightChild(self) -> bool:
        """Does this node have a right child?"""
        return self._right is not None
    
    def data(self) -> T:
        """Get the data."""
        # Pre
        assert not self.empty()
        return self._data
    
    def __len__(self) -> int:
        """Count the nodes in the tree."""
        nodes = 0
        if not self.empty():
            nodes = 1
            if self.hasLeftChild():
                nodes += len(self._left)
            if self.hasRightChild():
                nodes += len(self._right)
        return nodes
    
    def height(self) -> int:
        """Find the height of the tree."""
        height = 0
        if not self.empty():
            height = 1
            if self.hasLeftChild() and self.hasRightChild():
                height += max(self._left.height(), self._right.height())
            elif self.hasLeftChild(): # No right child
                height += self._left.height()
            elif self.hasRightChild(): # No left child
                height += self._right.height()
        return height
    
    def preorder(self) -> list[T]:
        """Preorder traversal (parents before children)."""
        result: list[T] = []
        if not self.empty():
            result += [self.data()]
            if self.hasLeftChild():
                result += self._left.preorder()
            if self.hasRightChild():
                result += self._right.preorder()
        return result
    
    def postorder(self) -> list[T]:
        """Postorder traversal (children before parents)."""
        result: list[T] = []
        if not self.empty():
            if self.hasLeftChild():
                result += self._left.postorder()
            if self.hasRightChild():
                result += self._right.postorder()
            result += [self.data()]
        return result
    
    def inorder(self) -> list[T]:
        """Inorder traversal (left subtree, parent, right subtree)."""
        result: list[T] = []
        if not self.empty():
            if self.hasLeftChild():
                result += self._left.inorder()
            result += [self.data()]
            if self.hasRightChild():
                result += self._right.inorder()
        return result