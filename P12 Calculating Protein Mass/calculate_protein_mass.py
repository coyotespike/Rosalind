def calculate_protein_mass(filename):
    """
    Given: A protein string P of length at most 1000 aa.
    Return: The total weight of P.

    Sample dataset: SKADYEK
    Answer: 821.392

    clever method to make a dictionary
    #mass string to list
    mass = mass.split()
    #mass string to dict
    mass = dict(zip(mass[0::2],mass[1::2]))
    """

    # open the file with the data
    data = open(filename, "r")

    # extract the info inside as a string
    dataset = data.read()

    MONOISOTOPIC_MASS_TABLE = {
        'A': 71.03711,
        'C': 103.00919,
        'D': 115.02694,
        'E': 129.04259,
        'F': 147.06841,
        'G': 57.02146,
        'H': 137.05891,
        'I': 113.08406,
        'K': 128.09496,
        'L': 113.08406,
        'M': 131.04049,
        'N': 114.04293,
        'P': 97.05276,
        'Q': 128.05858,
        'R': 156.10111,
        'S': 87.03203,
        'T': 101.04768,
        'V': 99.06841,
        'W': 186.07931,
        'Y': 163.06333,
    }

    h={'A': 71.03711, 'C': 103.00919, 'E': 129.04259, 'D': 115.02694, 'G': 57.02146, 'F': 147.06841, 'I': 113.08406, 'H': 137.05891, 'K': 128.09496, 'M': 131.04049, 'L': 113.08406, 'N': 114.04293, 'Q': 128.05858, 'P': 97.05276, 'S': 87.03203, 'R': 156.10111, 'T': 101.04768, 'W': 186.07931, 'V': 99.06841, 'Y': 163.06333}
    sequence = dataset
    print round(sum([h[x] for x in sequence if x in h]), 3)

    result = 0
    for i in dataset:
        if i in MONOISOTOPIC_MASS_TABLE:
            result += MONOISOTOPIC_MASS_TABLE[i]

    return round(result, 3)

filename = "/Users/timothyroy/Documents/Rosalind/P12 Calculating Protein Mass/rosalind_prtm.txt"

print calculate_protein_mass(filename)