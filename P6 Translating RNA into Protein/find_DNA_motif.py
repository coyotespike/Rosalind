import re
def find_DNA_motif(filename):
    """
    Takes two DNA strings, s and t, and returns all locations of t as a substring of s.
    Returns an answer which counts from 1, rather than 0.

    Test:
    GATATATGCATATACTT
    ATAT

    Answer should be: 2 4 10
    """

    # open the file with the data
    data = open(filename, "r")

    #read it but then split by lines, and store as a list in dataset
    dataset = data.read().splitlines()

    #the first item in the dataset is the first line, and that's the target string
    targetstring = dataset[0]
    print targetstring
    #the second item is the second line, and that's the string to search for
    substring = dataset[1]
    print substring

    """
    regexresult = [m.start() for m in re.finditer(substring, targetstring)]
    print [m.start() for m in re.finditer('(?=tt)', 'ttt')]
    print (" ".join(str(x+1) for x in regexresult))
    """
    # this code is foxy. It starts with a bunch of numbers: a range as long as the target string.
    # then, it goes through the numbers in that range
    # and appends a number to a list, if the substring starts at targetstring[number].
    # finally, we add 1 to the number, because Rosalind wants our numbering to start from 1, not 0
    result = [i+1 for i in range(len(targetstring)) if targetstring.startswith(substring, i)]

    # here, we join each element in a string. That way we get rid of the commas and brackets that come with the list.
    return (" ".join(str(x) for x in result))


filename = "/Users/timothyroy/Documents/Rosalind/P7 Finding a Motif in DNA/rosalind_subs.txt"
print find_DNA_motif(filename)