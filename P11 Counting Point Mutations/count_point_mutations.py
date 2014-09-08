def count_mutations (filename):
    """
    Given: Two DNA strings s and t of equal length (not exceeding 1 kbp).
    Return: The Hamming distance dH(s,t).

    A point mutation is the simplest type of mutation; one basepair replaces another at a nucleotide.

    Given two strings s and t of equal length, the Hamming distance between s and t, denoted dH(s,t),
    is the number of corresponding symbols that differ in s and t.

    The principle of parsimony demands that evolutionary histories should be explained as simply as possible.

    Sample dataset:
    GAGCCTACTAACGGGAT
    CATCGTAATGACGGCCT
    Answer: 7

    An optimal solution:
    sum(a != b for a, b in itertools.izip(s1, s2))
    """
    # open the file with the data
    data = open(filename, "r")

    #read it but then split by lines, and store as a list in dataset
    dataset = data.read().splitlines()

    #the first item in the dataset is the first line, and that's the first string to compare
    firststring = dataset[0]

    #the second item is the second line, and that's the second string to compare
    secondstring = dataset[1]

    count = 0
    for i in range(len(firststring)):
        if firststring[i] != secondstring[i]:
            count +=1

    return count

"""
filename = "GAGCCTACTAACGGGAT\nCATCGTAATGACGGCCT"
# make a new file, open it, write the answer inside it, and close the file
newfile = "/Users/timothyroy/Documents/Rosalind/P11 Counting Point Mutations/testfile"
answer_file = open(newfile, "w")
answer_file.write(str(filename))
answer_file.close()
"""

filename = "/Users/timothyroy/Documents/Rosalind/P11 Counting Point Mutations/rosalind_hamm.txt"
print count_mutations (filename)