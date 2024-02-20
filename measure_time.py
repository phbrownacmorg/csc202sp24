import random
import timeit

def makelist(size: int) -> list[int]:
    """Return a list of SIZE random integers in the range [0, 100000]."""
    return [random.randrange(0, 100000) for i in range(size)]

def sumlistloop(numbers: list[int]) -> int:
    """Sum a list of numbers using the accumulator pattern."""
    total = 0
    for num in numbers:
        total += num
    return total

def main(args: list[str]) -> int:
    for n in [10, 100, 1000]:
        print('size =', n)
        print(timeit.timeit(stmt=f'sum(makelist({n}))',
                            number=1000, globals=globals()))
        print(timeit.timeit(stmt=f'sumlistloop(makelist({n}))',
                            number=1000, globals=globals()))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main([]))