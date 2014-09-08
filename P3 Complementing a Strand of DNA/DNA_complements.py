import re

def DNA_complement(filename):
    """

    Reverse the DNA string
    """

    # open the file with the data
    data = open(filename, "r")

    # extract the info inside as a string
    dataset = data.read()

    # make a dictionary with items to replace each other
    rep_dict = {'T':'A', 'A':'T', 'G':'C', 'C':'G'}

    # define a new function to replace the items
    # the re.escape backslashes all non-alphanumeric character.
    # The backslash tells regex to search those too, not to treat them as special regex metacharacters
    # re.compile creates a "pattern object" with its own methods.
    # the pattern object is where the pattern to use gets defined. the | is an alternator.
    # "A|C|T|G"
    # sub takes three args: text to replace with, text to replace in, optional number of times to replace
    # the lambda i think puts the dictionary as a group into x
    def multiple_replace(dataset, rep_dict):
        pattern = re.compile("|".join([re.escape(k) for k in rep_dict.keys()]))
        return pattern.sub(lambda x: rep_dict[x.group(0)], dataset)

    complement = multiple_replace(dataset, rep_dict)


    # flip complement around
    complement_reverse = complement[::-1]

    #store the result in a new file
    newfile = "/Users/timothyroy/Documents/Rosalind/Problem 3/complement_reverse.txt"
    RNA_file = open(newfile, "w")
    RNA_file.write(complement_reverse)
    RNA_file.close()

    return complement_reverse

filename = ("/Users/timothyroy/Documents/Rosalind/Problem 3/rosalind_revc.txt")

print DNA_complement (filename)