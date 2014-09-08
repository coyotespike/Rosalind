def probable_mendel (k, m, n):
    """
    Given: Three positive integers k, m, and n, representing a population containing k+m+n organisms:
    k individuals are homozygous dominant for a factor, m are heterozygous, and n are homozygous recessive.
    homozygous dominant: two dominant alleles
    heterozygous: one dominant, one recessive
    homozygous recessive: two recessive alleles

    Return: The probability that two randomly selected mating organisms will produce an individual
    possessing a dominant allele (and thus displaying the dominant phenotype).
    Assume that any two organisms can mate.

    Sample Dataset: 2 2 2
    Answer: 0.78333

    In general, the number of possible outcomes will be equal to (k+m+n)*(k+m+n - 1).

    The probability of any outcome is either a/totalpop * a-1/totalpop-1,
    or a/totalpop * b/totalpop-1.

    Any outcome with a k will have a dominant allele.
    Any outcome without a k will have a 1/2 probability of a dominant allele,
    unless the outcome is nn. Thus, only three scenarios are of interest:
    with k, with no k but with m, and with only n. The probability of a dominant allele
    in those scenarios is 1, 1/2, and 0, respectively.

    """

    k = float(k)
    m = float(m)
    n = float(n)
    totalpop = k + m + n

    print (((k/totalpop) * ((m+n)/(totalpop-1)))*float(2))\
          + ((k/totalpop) * ((k-1)/(totalpop-1))*2)\
          + (((m/totalpop) * ((m-1)/(totalpop-1)))*(2/float(2)))\
          +(((m)/(totalpop)) * ((n)/(totalpop-1)))*(1/float(2))

    print (k/totalpop)*2
    print (k/totalpop) + (((m+n)/totalpop) * ((m+n-1)/(totalpop-1)))
              # + ((n/totalpop) * ((n-1)/(totalpop-1)))*(0)\




probable_mendel(2, 2, 2)