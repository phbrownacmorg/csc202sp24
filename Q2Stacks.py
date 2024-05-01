from typing import Generic, TypeVar
from Stack import Stack

T = TypeVar('T')

class Queue(Generic[T]):
    """Class to represent a queue, based on two stacks."""

    def __init__(self): # type: ignore
        """Construct an empty queue."""
        self.__inbox: Stack[T] = Stack[T]() # type: ignore
        self.__outbox: Stack[T] = Stack[T]() # type: ignore

    # Query methods
    def empty(self) -> bool:
        """Return True iff the queue is empty."""
        return self.__inbox.empty() and self.__outbox.empty()

    def peek(self) -> T:
        """Peek at the item at the head of the queue."""
        # Pre:
        assert not self.empty()
        if self.__outbox.empty():
            self.__refillOutbox()
        return self.__outbox.peek()

    # Mutator methods
    def __refillOutbox(self) -> None:
        """Refill the outbox."""
        # Pre:
        assert self.__outbox.empty()  # Otherwise the order gets fouled up
        while not self.__inbox.empty():
            self.__outbox.push(self.__inbox.pop())
        # Post:
        assert self.__inbox.empty()
        # Either the outbox is not empty or self *is* empty,
        # but asserting self.__inbox.empty() implies that

    def add(self, new_item: T) -> None:
        """Add NEW_ITEM to the end of the queue."""
        self.__inbox.push(new_item)

    def pop(self) -> T:
        """Remove and return the item at the head of the queue.
        The queue must not be empty."""
        # Pre:
        assert not self.empty()
        if self.__outbox.empty():
            self.__refillOutbox()
        assert not self.__outbox.empty()
        return self.__outbox.pop()
