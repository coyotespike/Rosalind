import re

def compute_gc(filename):

    # open the file with the data
    data = open(filename, "r")

    # extract the info inside as a string

    dataset = data.read()
#    dataset = filename

    # initialize counters for each DNA type
    num_A = 0
    num_G = 0
    num_T = 0
    num_C = 0

    # make a pattern object of >Rosalind_ followed by 4 numbers (the FASTA label)
    pattern = re.compile('>Rosalind_\d{4}')

    # find all those pattern objects in the dataset, and bind them as a list to stringnames
    stringnames = pattern.findall(dataset)

    # split the dataset by those pattern objects. Bind the dataset as a list to result.
    result = pattern.split(dataset)

    # next, zip the lists together, turn into a dictionary, store as an empty dictionary.
    emptydict = dict(zip(stringnames, result[1:]))

    # pull out each value in the dictionary, and count each base in the value

    for key in emptydict:
        num_A = emptydict[key].count("A")
        num_T = emptydict[key].count("T")
        temp_G = emptydict[key].count("G")
        temp_C = emptydict[key].count("C")

        # store the greatest number of GC content
        if temp_G + temp_C > num_G + num_C:
            num_G = temp_G
            num_C = temp_C
            highestPercentage = round(100*(float(num_G + num_C)/float(num_G + num_C + num_A + num_T)), 4)
            correctLabel = key

    # divide GC/ATCG and round to three digits

    # return the string label and percentage of the highest GC-content string
    return correctLabel, highestPercentage




filename = ("/Users/timothyroy/Documents/Rosalind/rosalind_gc.txt")
"""
filename = ">Rosalind_6404CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG\
>Rosalind_5959CCATCGGTAGCGCATCCTTAGTCCAATTAAGTCCCTATCCAGGCGCTCCGCCGAAGGTCTATATCCATTTGTCAGCAGACACGC\
>Rosalind_0808CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"
"""

print compute_gc(filename)