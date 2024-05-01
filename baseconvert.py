from Stack import Stack

digits = '0123456789abcdefghijklmnopqrtsuvwxyz'

def changebase(num: int, base: int) -> str:
    """Represent the given NUM in base BASE.  Return the representation
    as a string."""
    # Pre:
    assert num >= 0 and 2 <= base <= len(digits)
    s = Stack[str]() # type: ignore
    while num > 0:
        # Push the least significant digit
        s.push(digits[num % base])
        num = num // base
    if s.empty(): # Number was 0 to start with
        s.push(digits[0])
        
    result = ''
    while not s.empty():
        result = result + s.pop()
    return result

def main(args: list[str]) -> int:
    num = int(input('Please enter a non-negative integer to convert: '))
    assert num >= 0, 'Number most be non-negative'
    base = int(input(f'Please enter a base to convert the number into (2-{len(digits)}): '))
    assert 1 < base <= len(digits), f'Base must be between 2 and {len(digits)}'
    print(f'The number {num} in base {base} is ', changebase(num, base))

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))