from Stack import Stack

def balanced(expr: str) -> bool:
    openers = '{(['
    closers = '})]'
    st = Stack[str]()
    bal = True
    for c in expr:
        if c in openers:
            st.push(c)
        elif c in closers:
            bal = bal and not st.empty()
            if bal:
                left = st.pop()
                # Check to see if it matches
                bal = bal and (openers.index(left) == closers.index(c))
            # If we found a mismatch, we're done.  It won't get better.
            if not bal:
                break
    bal = bal and st.empty()
    return bal

def main(args: list[str]) -> int:
    """Program to take an expression and print out whether the
    delimiters within that expression are balanced or not."""
    expr = input("Please enter an arithmetic expression: ")
    print(f'The delimiters in the expression "{expr}" are', end=' ')

    if not balanced(expr):
        print('NOT', end=' ')
    print('balanced.')

    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))