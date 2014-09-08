import collections
def infer_mRNA(filename):
    """
    Modular arithmetic and combinatorics. Some problems will ask for a very large integer solution modulo a smaller number,
    to avoid the pitfalls of storing large numbers.

    if a cong b mod n, and co cong d mod n, then a+c cong b+d mod n, and a*c cong b*d mod n.
    you may wish to verify these relationships for a=29, b=73, c=10, d=32, and n=11

    Here, a cong b mod n, and c cong d mod n. Thus, a*b cong c*d mod n.

    Given: A protein string of length at most 1000 aa.
    Return: The total number of different RNA strings from which the protein could have been translated, modulo 1,000,000.
    (Don't neglect the importance of the stop codon in protein translation.)

    Sample dataset: MA
    Answer: 12

    Solution history: attempted to construct a reverse codon dict, as below. Python stores only unique keys, so the dict was shortened.
        d3 = dict(zip(codon_table.values(), codon_table.keys()))
        key_list = []
        value_list = []
        reversed_codon_table = {}
        for i in codon_table:
            key_list.append(i)
            value_list.append(codon_table[i])
            reversed_codon_table[codon_table[i]] = i
        d4 = dict(zip(value_list, key_list))

    Questions: what is the collections defaultdict? Why does iteritems() fix the 'too many values to unpack' problem?
    """

     # open the file with the data
    data = open(filename, "r")

    # extract the info inside as a string
    dataset = data.read()
    #dataset = filename

    # this is the table for translating codons into protein
    codon_table = \
        {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
        "UCU":"S", "UCC":"S", "UCA":"S", "UCG":"S",
        "UAU":"Y", "UAC":"Y", "UAA":"STOP", "UAG":"STOP",
        "UGU":"C", "UGC":"C", "UGA":"STOP", "UGG":"W",
        "CUU":"L", "CUC":"L", "CUA":"L", "CUG":"L",
        "CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P",
        "CAU":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
        "CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R",
        "AUU":"I", "AUC":"I", "AUA":"I", "AUG":"M",
        "ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T",
        "AAU":"N", "AAC":"N", "AAA":"K", "AAG":"K",
        "AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R",
        "GUU":"V", "GUC":"V", "GUA":"V", "GUG":"V",
        "GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A",
        "GAU":"D", "GAC":"D", "GAA":"E", "GAG":"E",
        "GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}

    # make a special dictionary of lists
    reverse_codon_table = collections.defaultdict(list)

    # each value in the codon dictionary becomes a key.
    # each codon dict key is appended as a value into the list.
    # the new special dictionary has a bunch of lists as values
    for key, val in codon_table.iteritems():
        reverse_codon_table[val].append(key)

    #this is our counter.
    result = 1

    # for each protein, get the length of the list of values in our new dict,
    # and multiply the counter by that length.
    # to make it smaller, modulo by a million
    for i in dataset:
        if i in reverse_codon_table:
            result *= len(reverse_codon_table[i])
            result = result % 1000000

    # don't forget the stop codons
    result *= len(reverse_codon_table['STOP'])

    # make a new file, open it, write the answer inside it, and close the file
    newfile = "/Users/timothyroy/Documents/Rosalind/P10 Inferring mRNA from Protein/inference answer"
    answer_file = open(newfile, "w")
    answer_file.write(str(result))
    answer_file.close()

    return result

filename = "/Users/timothyroy/Documents/Rosalind/P10 Inferring mRNA from Protein/rosalind_mrna.txt"
print infer_mRNA(filename)