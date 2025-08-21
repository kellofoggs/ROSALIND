from math import comb, log10
from Utilities.Stats import Distributions
from decimal import Decimal
from Utilities.InputFileTools import GenericTextFile
from Utilities.Math import Rounding
import sys
'''
Diploid- cells have two sets of each chromosome (Generally one from each parent)
Haploid - Such as sex cells, one set for each chromosome

We're interested in the probability that two diploid siblings share k or more of their 2n chromosomes
We're given n, the number of pairs of chromosomes
'''

file_name = sys.argv[1]

def main(pairs_of_chromosomes:int):
    num_chromosomes = pairs_of_chromosomes * 2


    p_sib_chrom_is_same = 0.50 # By law of independent assortment, two siblings have a 50-50 percent chance of having the same chromosome from their shared parents


    # Note: This is symmetrical because it's a binomial with an equal rate of success/failure,
    # We could get away with only calculating up to the num_chromosomes//2 trial but this makes the solution less readable
    prob_exactly_k_shared = [Distributions.binomial_pmf(num_trials= num_chromosomes, num_success=k, prob_success= p_sib_chrom_is_same) for k in range(num_chromosomes+1)]

    last_prob = round(0.000, 3)
    log_probs = []
    for i in range(len(prob_exactly_k_shared)-1,0, -1):
        last_prob = sum((last_prob, + prob_exactly_k_shared[i]))
        log_probs.insert(0, f"{log10(last_prob):.3f}")

    print(' '.join(log_probs))

pairs_of_chromosomes = int(GenericTextFile.get_generic_file_as_lines(file_name)[0])
main(pairs_of_chromosomes)