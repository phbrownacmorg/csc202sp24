from typing import cast, Generic, TypeVar

T = TypeVar('T')

class LList(Generic[T]):
    """Class to represent a linked list.  In this implementation, a list
    is either (1) an empty list, or (2) a node with data followed by
    a linked list.  The empty list is represented by a sentinel node.
    This list does not support storing None as a data value."""

    def __invariant(self) -> bool:
        """Class invariant."""
        valid = True
        if self.__next is None: # Sentinel node (empty list)
            valid = self.__data is None
        else: # There's more list after this node
            valid = self.__data is not None and self.__next.__invariant()
        return valid
        
    def __init__(self): # type: ignore
        """Create an empty list."""
        self.__data = None # Reference to data value
        self.__next = None # Reference to next node
        # Post:
        assert self.__invariant()

    # QUERY METHODS

    def empty(self) -> bool:
        """Returns True if the list is empty, else False."""
        return self.__next is None # (and self.__data is None)
    
    def value(self) -> T:
        """Returns the value stored in the current node."""
        # Pre:
        assert self.__invariant() and not self.empty()
        return cast(T, self.__data)
    
    def next(self) -> 'LList[T]':
        """Returns the next node after this one."""
        # Pre:
        assert self.__invariant() and not self.empty()
        return cast(LList[T], self.__next)
    
    def __len__(self) -> int:
        """Returns the number of nodes in the list (not counting the sentinel)."""
        nodes = -1
        if self.empty(): # Empty list, or...
            nodes = 0
        else:            # A node followed by a linked list
            nodes = 1 + len(self.next())
        return nodes

    def __str__(self) -> str:
        """Returns a string representation of the list."""
        result = ''
        if self.empty(): # Empty list, or...
            result = '∅'
        else:            # A node followed by a linked list
            result = f'❬{str(self.value())}❭➞' + str(self.next())
        return result
    
    def index(self, val: T) -> int:
        """Returns the index of the first occurrence of VAL in the list.
        Raises ValueError if VAL is not in the list."""
        idx = -1
        if self.empty(): # Empty list, or...
            raise ValueError(f"{val} is not in list")
        elif self.value() == val: # A node...
            idx = 0
        else:            # followed by a list
            idx = 1 + self.next().index(val)
        return idx

    # MUTATOR METHODS

    def add(self, val: T) -> None:
        """Add a node with value VAL at the beginning of the list."""
        newnode: LList[T] = LList[T]() # type: ignore
        newnode.__data = self.__data
        newnode.__next = self.__next
        self.__next = newnode
        self.__data = val
        # Post:
        assert self.__data == val and self.__invariant()

    def pop(self, idx: int = -1) -> T:
        """Returns the item at index IDX, remiving it from the list."""
        value: T | None = None
        # Ensure IDX is within limits
        size = len(self)
        if idx < -size or idx >= size:
            raise IndexError(f'List size is {size}; index {idx} out of range')

        # Support negative indices (count from the end)
        if idx < 0:
            idx += size
        assert self.empty() or idx >= 0, 'Index out of range not caught'
        if self.empty(): # Empty list, or...
            raise IndexError('Cannot pop from empty list')
        elif idx == 0:   # a node...
            value = self.value()
            # Remove the item from the list.  Order is important!
            self.__data = self.next().__data
            self.__next = self.next().__next
        else:            # followed by another node
            value = self.next().pop(idx - 1)
        return value