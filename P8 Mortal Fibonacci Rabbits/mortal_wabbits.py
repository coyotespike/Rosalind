# coding=utf-8
def mortal_wabbits(n, m):
    """
    Given: Positive integers n≤100 and m≤20.
    Return: The total number of pairs of rabbits that will remain after the n-th month if all rabbits live for m months.

    Assume the rabbits produce one pair of offspring each month.
    Start with one pair.

    Test: 6 3
    Return: 4
    """
    # in month 1 and 2, we have 1 pair
    if n == 1 or n == 2:
        return 1

    else:
        return wascally_wabbits(n-1, k) + k*(wascally_wabbits(n-2, k))


print mortal_wabbits (6, 3)