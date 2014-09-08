def translate_RNA_protein(filename):
    """
    Given an RNA string, returns the appropriate protein string.
    Strips off the stop codons but keeps the start codons.
    Also saves the protein string in a new file.

    sample dataset: AUGGCCAUGGCGCCCAGAACUGAGAUCAAUAGUACCCGUAUUAACGGGUGA
    answer should be: MAMAPRTEINSTRING
    """

 # open the file with the data
    data = open(filename, "r")

    # extract the info inside as a string
    dataset = data.read()
    #dataset = filename

    codon_table = {"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L",
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

    # map applies a function to every element of an iterable. Here the function is "".join
    # iter() returns an iterator object. with only one argument, iter() requires an iterable object.

    split_data = map(''.join, zip(*[iter(dataset)]*3))

    """
    protein_string = ""
    for codon in split_data:
        if codon_table[codon] != "STOP":
            protein_string.join(codon_table[codon])
    """

    protein_string = "".join([codon_table[i] for i in split_data if codon_table[i] != "STOP"])

    # make a new file, open it, write the answer inside it, and close the file
    newfile = "/Users/timothyroy/Documents/Rosalind/P6 Translating RNA into Protein/proteinanswer"
    protein_file = open(newfile, "w")
    protein_file.write(protein_string)
    protein_file.close()

    return protein_string

filename = "/Users/timothyroy/Documents/Rosalind/P6 Translating RNA into Protein/rosalind_prot.txt"

print translate_RNA_protein(filename)