def count_DNA (filename):
    """
    Opens a data file of DNA and counts the occurrence of each base.
    Returns the number of occurrences.
    """

    # open the file with the data
    data = open(filename, "r")

    # extract the info inside as a string
    dataset = data.read()

    # initialize counters for each DNA type
    num_A = 0
    num_G = 0
    num_T = 0
    num_C = 0

    # add to counters for each base
    for i in dataset:
        if i == 'A':
            num_A += 1

        elif i == 'G':
            num_G += 1

        elif i == 'C':
            num_C += 1

        elif i == 'T':
            num_T += 1

    return num_A, num_C, num_G, num_T


filename = "/Users/timothyroy/Rosalind/rosalind_dna.txt"

print count_DNA (filename)