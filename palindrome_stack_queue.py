from Queue import Queue
from Stack import Stack

def palindrome(s: str) -> bool:
    """Return TRUE if the string S is a palindrome.
    Ignores case and non-letters."""
    pal = True
    s = s.lower()
    q = Queue[str]()
    st = Stack[str]()

    for c in s:
        if c.isalpha():
            q.add(c)
            st.push(c)
    
    while pal and not q.empty():
        c1 = q.pop()
        c2 = st.pop()
        pal = pal and (c1 == c2)
    pal = pal and st.empty()

    return pal

def main(args: list[str]) -> int:
    s = input('Please enter a string: ')
    print(f'The string "{s}" is ', end='')

    if not palindrome(s):
        print('NOT ', end='')
    print('a palindrome.')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))