from typing import TypeVar

T = TypeVar('T')

def binsearch(key: T, array: list[T]) -> bool:
    """Perform a recursive binary search for KEY in ARRAY,
    using slicing."""
    mid: int = len(array) // 2
    if len(array) == 0:
        found = False
    elif key == array[mid]:
        found = True
    elif key < array[mid]: # type: ignore
        found = binsearch(key, array[:mid])
    else: # key > array[mid]
        found = binsearch(key, array[mid+1:])
    return found

def partition(array: list[T], start: int, end: int) -> int:
    """Partition ARRAY[START:END], and return the final position
    of the pivot.  The pivot is simply array[start]."""
    # Pre:
    assert 0 <= start < len(array) and start < end \
        and 0 <= end <= len(array)
    pivot = array[start] # Pick an element to partition around

    mid = start+1
    top = end-1
    while top >= mid:
        if array[mid] <= pivot: # type: ignore
            mid = mid + 1
        else: # array[mid] > pivot
            # Swap in an item from top
            array[top], array[mid] = array[mid], array[top]
            top = top - 1
    # When done, swap the pivot into the midpoint
    array[start], array[top] = array[top], array[start]
    return top

def quicksort(array: list[T], start: int = 0, end: int = -1) -> None:
    """Perform a quicksort on ARRAY from index START up to but not
    including index END, in place."""
    # Pre:
    assert 0 <= start <= len(array) and \
            ((start <= end and (0 <= end <= len(array))) \
             or (start == 0 and end == -1)), \
                f"{start}, {end}, {len(array)}"
    # Make END default to len(array).  Needed because we can't call
    # len(array) in the argument list.
    if end == -1: 
        end = len(array)

    # Base case: list of length < 2 is already sorted
    # Recursive case:
    if end - start > 1:
        mid = partition(array, start, end)
        quicksort(array, start, mid)
        quicksort(array, mid+1, end)
