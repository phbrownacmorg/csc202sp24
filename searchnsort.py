from typing import TypeVar

T = TypeVar('T')

def binsearch(key: T, array: list[T]) -> bool:
    mid: int = len(array) // 2
    if len(array) == 0:
        found = False
    elif key == array[mid]:
        found = True
    elif key < array[mid]:
        found = binsearch(key, array[:mid])
    else: # key > array[mid]
        found = binsearch(key, array[mid+1:])
    return found

def partition(array: list[T], start: int, end: int) -> int:
    pivot = array[start] # Pick an element to partition around

    mid = start+1
    top = end-1
    while top >= mid:
        if array[mid] <= pivot:
            mid = mid + 1
        else: # array[mid] > pivot
            # Swap in an item from top
            array[top], array[mid] = array[mid], array[top]
            top = top - 1
    # When done, swap the pivot into the midpoint
    array[start], array[top] = array[top], array[start]
    return top

def quicksort(array: list[T], start: int = 0,  end: int = -100) -> None:
    """Perform a quicksort on ARRAY from index START up to but not
    including index END, in place."""
    if end == -100: # Handle the default parameter
        end = len(array)

    # Base case: list of length < 2 is already sorted
    if end - start > 1: # Recursive case
        mid = partition(array, start, end)
        quicksort(array, start, mid)
        quicksort(array, mid+1, end)
