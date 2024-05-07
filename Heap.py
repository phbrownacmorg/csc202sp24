from typing import Generic, TypeVar

T = TypeVar('T')

class Heap(Generic[T]):
    """Class to represent a max-heap.  The class is implemented as a Python list,
    where the left child of the element at index p is at index 2p + 1, the right
    child is at index 2p + 2, and the parent is at index (p-1)//2."""

    def _invariant(self) -> bool:
        """Class invariant.  Checks the max-heap property."""
        is_heap = True
        for idx in range(1, len(self._heap)):
            # max-heap property.  If every element is less than or equal to its parent,
            # we have a max heap.
            is_heap = is_heap and (self._heap[idx] <= self._heap[(idx - 1)//2]) # type: ignore
        return is_heap

    def __init__(self): # type: ignore
        """Constructs an empty heap."""
        self._heap: list[T] = []
        # Post:
        assert self._invariant()

    # QUERY METHODS

    def __len__(self) -> int:
        """Return the size of the heap."""
        return len(self._heap)
    
    def empty(self) -> bool:
        """Returns True iff the heap is empty."""
        return len(self) == 0
    
    def peek(self) -> T:
        """Return the largest value in the heap, without changing the heap."""
        # Pre:
        assert not self.empty(), "Can't peek at an empty heap."
        return self._heap[0]
    
    # MUTATOR METHODS

    def _perc_up(self, idx: int) -> None:
        """Helper function to percolate the item at index IDX up the heap,
        restoring the heap property."""
        if idx > 0: # If idx == 0, do nothing
            p = (idx - 1)//2
            if self._heap[idx] > self._heap[p]: # type: ignore
                # Swap
                self._heap[idx], self._heap[p] = \
                    self._heap[p], self._heap[idx]
                self._perc_up(p)

    def _big_child_idx(self, idx: int) -> int:
        """Helper function to find the index of the largest child of the item
        at index IDX."""
        left_child_idx = 2 * idx + 1
        # Pre:
        assert left_child_idx < len(self) # Has to be at least one child

        result = left_child_idx # Default to left child
        right_child_idx = left_child_idx + 1

        # If there is a right child, and the right child is bigger than the left...
        if right_child_idx < len(self) and \
            self._heap[left_child_idx] < self._heap[right_child_idx]: # type: ignore
            result = right_child_idx
        return result

    def _perc_down(self, idx: int) -> None:
        """Helper function to percolate the item at index IDX down the heap,
        restoring the heap property."""
        if 2 * idx + 1 < len(self): # if the item at IDX has no children, do nothing
            big_child_idx = self._big_child_idx(idx)
            # Swap?
            if self._heap[idx] < self._heap[big_child_idx]: # type: ignore
                self._heap[idx], self._heap[big_child_idx] = \
                    self._heap[big_child_idx], self._heap[idx]
                self._perc_down(big_child_idx)

    def add(self, value: T) -> None:
        """Adds item VALUE to the heap."""
        self._heap.append(value) # Add VALUE to the end
        self._perc_up(len(self) - 1) # Percolate the new value up the heap
        # Post:
        assert self._invariant() # Should have the heap property back

    def pop(self) -> T:
        """Pops the largest item off the heap."""
        # Pre:
        assert not self.empty(), "Can't pop an empty heap."
        # Swap the first element with the last, so list.pop() doesn't foul up
        #   the tree structure
        self._heap[0], self._heap[-1] = self._heap[-1], self._heap[0]
        result = self._heap.pop() # Removes the last item, which used to be first
        # Restore the heap property
        self._perc_down(0)

        # Post:
        assert self._invariant()
        return result
