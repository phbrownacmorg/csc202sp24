from LList import LList
from typing import cast, SupportsFloat
import random

def make_random_list(length: int, max: float) -> LList[float]:
    """Make a list of LENGTH random numbers in the range 0-MAX."""
    # Pre:
    assert length >= 0
    if length == 0: # Base case
        # Return an empty list
        return LList[float]() # type: ignore
    else:           # Recursive case
        number_list = make_random_list(length - 1, max)
        number_list.add(random.random() * max)
        return number_list

def sumlist(number_list: LList[SupportsFloat]) -> float:
    """Sum a list of numbers, recursively."""
    if number_list.empty(): # Base case
        return 0
    else:                   # Recursive case
        return float(number_list.value()) + sumlist(number_list.next())

def test_sumlist() -> None:
    number_list = LList[SupportsFloat]() # type: ignore
    assert sumlist(number_list) == 0 
    number_list.add(5)
    assert sumlist(number_list) == 5
    number_list.add(10)
    assert sumlist(number_list) == 15
    number_list.add(15)
    assert sumlist(number_list) == 30
    print('Tests for sumlist passed')

def string_reverse(s: str) -> str:
    """Reverse a string, recursively."""
    if len(s) <= 1:
        return s
    else:
        return s[-1] + string_reverse(s[:-1])

def test_string_reverse() -> None:
    assert string_reverse('') == ''
    assert string_reverse('I') == 'I'
    assert string_reverse('ab') == 'ba'
    assert string_reverse('Hannah') == 'hannaH'
    assert string_reverse("Madam, I'm Adam.") == ".madA m'I ,madaM"
    print('Tests for string_reverse passed')


def gcd(a: int, b: int) -> int:
    """Return the GCD of two integers, recursively."""
    if b == 0:
        return abs(a)
    else:
        return gcd(b, a % b)
    
def test_gcd() -> None:
    assert gcd(0, 0) == 0
    assert gcd(1, 0) == 1
    assert gcd(0, 1) == 1
    assert gcd(6, 9) == 3
    assert gcd(9, 6) == 3
    assert gcd(-9, 6) == 3
    assert gcd(-9, -6) == 3
    assert gcd(9, -6) == 3
    assert gcd(10, 20) == 10
    assert gcd(20, 10) == 10
    print('Tests for GCD passed')

def expt(a: int, b: int) -> int:
    """Raise A to the B power, recursively."""
    # Pre:
    assert b > -1, 'Negative exponents are not supported'
    if b == 0:   # Base case 1
        return 1
    elif b == 1: # Base case 2
        return a
    else:        # b > 1; recursive case
        return a * expt(a, b-1)

def test_expt() -> None:
    assert expt(2, 0) == 1
    assert expt(-1, 0) == 1
    assert expt(433, 0) == 1
    assert expt(2, 1) == 2
    assert expt(-1, 1) == -1
    assert expt(433, 1) == 433
    assert expt(2, 2) == 4
    assert expt(-1, 2) == 1
    assert expt(433, 2) == 433 ** 2
    assert expt(2, 15) == 32768
    assert expt(-1, 15) == -1
    assert expt(433, 15) == 433 ** 15
    print('Tests for expt passed.')

def fastexpt(a: int, b: int) -> int:
    """Raise A to the B power, recursively, quickly."""
    # Pre:
    assert b > -1, 'Negative exponents are not supported'
    if b == 0:   # Base case 1
        return 1
    elif b == 1: # Base case 2
        return a
    elif b % 2 == 0: # Recursive case 1: b is even
        half_expt = fastexpt(a, b // 2)
        return half_expt * half_expt
    else:            # b % 2 == 1; Recursive case 2: b is odd
        half_expt = fastexpt(a, b // 2)
        return half_expt * half_expt * a

def test_fastexpt() -> None:
    assert fastexpt(2, 0) == 1
    assert fastexpt(-1, 0) == 1
    assert fastexpt(433, 0) == 1
    assert fastexpt(2, 1) == 2
    assert fastexpt(-1, 1) == -1
    assert fastexpt(433, 1) == 433
    assert fastexpt(2, 2) == 4
    assert fastexpt(-1, 2) == 1
    assert fastexpt(433, 2) == 433 ** 2
    assert fastexpt(2, 15) == 32768
    assert fastexpt(-1, 15) == -1
    assert fastexpt(433, 15) == 433 ** 15
    print('Tests for fastexpt passed.')

def baseconvert(a: int, b: int) -> str:
    """Recursively express an integer A in a base B, where
    1 < B < 36."""
    digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    # Pre:
    assert 1 < b < len(digits), f'Unsupported base {b}'
    if a < 0:
        return '-' + baseconvert(-a, b)
    elif a < b:
        return digits[a]
    else:
        return baseconvert(a // b, b) + digits[a % b]

def test_baseconvert() -> None:
    assert baseconvert(433, 2) == '110110001'
    assert baseconvert(433, 16) == '1B1'
    assert baseconvert(-433, 16) == '-1B1'
    assert baseconvert(0x1b1, 10) == '433'
    assert baseconvert(0b110110001, 10) == '433'
    assert baseconvert(0x1b1, 5) == '3213'
    assert baseconvert(0x1b1, 12) == '301'
    print('Tests for base conversion passed.')

def slowfib(n: int) -> int:
    """Simple recursive calculation of a Fibonacci number."""
    # Pre:
    assert n >= 0, f'n must be non-negative; {n} supplied'
    if n < 2:
        return n
    else:
        return slowfib(n-1) + slowfib(n-2)
    
def fib(n: int) -> int:
    """More efficient recursive FIbonacci calculation."""
    # Pre:
    assert n >= 0, f'n must be non-negative; {n} supplied'
    return fastfib(n)[0]

def fastfib(n: int) -> tuple[int, int]:
    """Fibonacci calculation, returning *two* integers, fib(n)
    and fib(n-1).  This avoids recalculating fib(n-1)."""
    # Pre: (error message is incomplete)
    assert n >= 0, f'n must be non-negative; {n} supplied'
    if n < 2:
        return (n, 0)
    else:
        fib_n_less_1 = fastfib(n - 1) # Just call it once!
        return fib_n_less_1[0] + fib_n_less_1[1], fib_n_less_1[0]

def test_fib() -> None:
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(5) == 5
    assert fib(6) == 8
    assert fib(7) == 13
    assert fib(8) == 21
    assert fib(9) == 34
    assert fib(10) == 55
    assert fib(11) == 89
    assert fib(20) == 6765
    assert fib(30) == 832040
    assert fib(40) == 102334155
    assert fib(50) == 12586269025
    print('Tests for Fibonacci passed.')


def main(args: list[str]) -> int:
    test_sumlist()
    test_string_reverse()
    test_gcd()
    test_expt()
    test_fastexpt()
    test_baseconvert()
    test_fib()
    # length = int(input('How many random numbers should be on the list? '))
    # max = float(input('Please enter a maximum value for the random numbers: '))
    # number_list = make_random_list(length, max)
    # print('The list is', number_list)
    # print('The sum of the list is ', sumlist(number_list))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))