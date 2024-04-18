def make_change_greedy(amount: int, coin_values: tuple[int, ...]) -> list[int]:
    """Makes change for AMOUNT using COIN_VALUES.  Returns a list of how many
    of each coin is needed.  Uses a greedy algorithm to make the change, which
    assumes that each coin value divides the next bigger one evenly.  Other
    assumptions: (1) there exists a penny, so it is possible to make change
    for any positive integer amount, and (2) the coin values are sorted in
    descending order."""
    # Pre:
    assert amount >= 0, f"Cannot make change for a debt: amount was {amount}"
    assert amount == 0 or coin_values[-1] == 1, f"No penny in coin_values {coin_values}"
    # assert coin_values is sorted in descending order
    # assert each coin value divides the next bigger coin value evenly
    result: list[int] = []  # Handles the base case
    if amount > 0: # Assume there's always a penny
        result = [amount // coin_values[0]] # Take as many of the largest coin as possible
        # Then make change for the remaining value with the *rest* of the coin values 
        result = result + make_change_greedy(amount % coin_values[0], coin_values[1:])
    return result

def main(args: list[str]) -> int:

    amount: int = int(input('For how many cents do you want to make change? '))
    print(make_change_greedy(amount, (25, 10, 5, 1)))
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))