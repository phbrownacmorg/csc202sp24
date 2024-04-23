from LList import LList

class Hashtable:
    """Class to represent a Hashtable that stores strings.
    The table handles hash collisions by hash chaining.
    Items are stored as (key, value) tuples."""

    INITIAL_SIZE = 4

    @staticmethod
    def letterhash(val: str) -> int:
        """Find the letter hash value of a string,
        *independent* of the size of the hashtable."""
        hashstr = val.upper()
        total = 0
        for c in hashstr:
            total += ord(c) - ord('A') + 1

        return total

    def _invariant(self) -> bool:
        """Class invariant."""
        valid = True
        for i in range(len(self._bins)):
            bin = self._bins[i]
            valid = valid and bin is not None
            while not bin.empty():
                # All the items *in* the bin must *belong* in the bin
                valid = valid and self._hash(bin.value()[0]) == i
                bin = bin.next()
        return valid

    def __init__(self):
        """Create an empty hashtable.  The initial size is 4."""
        self._bins: list[LList[tuple[str, str]]] = []
        for i in range(Hashtable.INITIAL_SIZE):
            self._bins.append(LList[tuple[str, str]]())
        # Post:
        assert self._invariant(), 'Constructor postcondition failed'

    # Query methods
    def _hash(self, key: str) -> int:
        """Returns the hash value for KEY given the current size of the hash table."""
        return Hashtable.letterhash(key) % len(self._bins)

    def __contains__(self, key: str) -> bool:
        """Returns True if KEY is present in the hashtable."""
        found = False
        hashval = self._hash(key)
        bin = self._bins[hashval]
        while not found and not bin.empty():
            found = (bin.value()[0] == key)
            bin = bin.next()
        return found

    def get(self, key: str) -> str:
        """If KEY is present in the Hashtable, return its
        associated value.  If KEY is not in the Hashtable,
        raise KeyError."""
        hashval = self._hash(key)
        bin = self._bins[hashval]
        while not bin.empty() and bin.value()[0] != key:
            bin = bin.next()
        if bin.empty():
            raise KeyError(f"Key {key} not found")
        # Only reachable if bin is looking at the right item
        return bin.value()[1]
    # Mutator methods

    def put(self, key: str, value: str) -> None:
        """Put a string VALUE into the hashtable, using key KEY."""
        hashval = self._hash(key)
        self._bins[hashval].add((key, value))
        # Post:
        assert self._invariant(), 'put() failed'