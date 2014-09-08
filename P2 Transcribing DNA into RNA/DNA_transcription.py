def transcribe_DNA (filename):
    """
    Opens a data file of DNA.
    Returns RNA by replacing thymine with uracil.
    """

    # open the file with the data
    data = open(filename, "r")

    # extract the info inside as a string
    dataset = data.read()

    RNA_dataset = dataset.replace('T', 'U')

    newfile = "/Users/timothyroy/Documents/Rosalind/Problem 2/rosalind_rna2.txt"
    RNA_file = open(newfile, "w")

    RNA_file.write(RNA_dataset)
    RNA_file.close()

    print "try it now"

filename = ("/Users/timothyroy/Documents/Rosalind/Problem 2/rosalind_rna.txt")

transcribe_DNA (filename)