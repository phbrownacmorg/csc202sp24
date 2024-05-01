from typing import cast, Generic, TypeVar

T = TypeVar('T')

class Queue(Generic[T]):
    """Class to represent a queue, using a Python list
    in a circular-queue arrangement.  The items on the
    queue cannot be None."""

    INITIAL_SIZE = 4

    def __init__(self): # type: ignore
        """Construct an empty queue."""
        self.__head = 0
        self.__tail = 0
        self.__items: list[T | None] = [None] * Queue.INITIAL_SIZE

    # Query methods
    def empty(self) -> bool:
        """Return True iff the queue is empty."""
        return self.__items[self.__head] is None

    def peek(self) -> T:
        """Peek at the item at the head of the queue."""
        # Pre:
        assert not self.empty()
        return cast(T, self.__items[self.__head])

    # Mutator methods
    def add(self, new_item: T) -> None:
        """Add NEW_ITEM to the end of the queue."""
        # If the queue is full, resize it
        if self.__items[self.__tail] is not None:
            self.__resize()
        assert self.__items[self.__tail] is None
        self.__items[self.__tail] = new_item
        self.__tail = (self.__tail + 1) % len(self.__items)

    def pop(self) -> T:
        """Remove and return the item at the head of the queue.
        The queue must not be empty."""
        # Pre:
        assert not self.empty()
        value = self.__items[self.__head] # Grab the value
        self.__items[self.__head] = None  # Clear out the space
        self.__head = (self.__head + 1) % len(self.__items)
        return cast(T, value)

    def __resize(self) -> None:
        """Increase the size of the queue."""
        # Pre:
        self.__items[self.__tail] is not None # self.__items is full
        newItems: list[T | None] = cast(list[T | None], [None] * 2 * len(self.__items))

        for i in range(len(self.__items)):
            newItems[i] = self.pop()
        assert self.empty()
        self.__head = 0
        self.__tail = len(self.__items) # Old capacity
        self.__items = newItems
        # Post: all the previous items are still there
        assert self.__items[self.__tail] is None and self.__head == 0 \
            and self.__tail == len(self.__items) // 2
        # self.__tail *implies* that self.__items doubled in size