def wascally_wabbits(n, k):
    """
    Given n months and k litters after each month,
    return number of rabbits in n-th month.

    Start with 1 pair
    """
    # in month 1 and 2, we have 1 pair
    if n == 1 or n == 2:
        return 1

    # if month 3 and more,
    # rabbits in this month = rabbits one month back + rabbits two months back (multiplied by the number of litters)
    else:
        return wascally_wabbits(n-1, k) + k*(wascally_wabbits(n-2, k))


def open_and_save():
    filename = ("/Users/timothyroy/Documents/Rosalind/Problem 4/rosalind_fib.txt")
    # open the file with the data
    data = open(filename, "r")

    # extract the info inside as a string
    dataset = data.read()
    dataset = dataset.split()

    n = int(dataset[0])
    k = int(dataset[1])

print wascally_wabbits (4, 1)
