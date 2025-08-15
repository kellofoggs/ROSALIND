from Utilities.Stats import Distributions 
from math import comb
from typing import List
from Utilities.InputFileTools import GenericTextFile
import sys
'''
Assumptions:
     each member of the population mates within its generation
     Next Generation is from the prior generation where N individuals are born
     
Assume we're studying a diploid 

given N m g k
N = number of diploid individuals initially
m = Initial copies of dominant allele
g = After how many generations we'll expect k  or more recessive allele copies
k = equal or more expected allele copies in the gth generation




'''



def get_prob_of_allele_counts_after_k_generations(generation_size:int, allele_count:int, num_generations:int, k:int) -> List[float]:
     '''
     For the ith generation its probabilities are based (i-1)th generation
     For the probability of each recessive allele count k, we need to consider all the probabilities of each count k in the i-1th generation
     It's a markov chain, sum up the product of (P())multiply the probabilities of  the previous generation with the current generation's probabilities
     There are some trivial states we really don't need to do all the sampling/summing/multiplication for; like no recessive alleles or all recessive alleles in the previous generation. This will always result in 0 or all recessive alleles in the next generation
     '''


     generation_alleles = generation_size*2

     all_generations_rec_allele_freq:List[list] = [] 

     cur_gen_rec_allele_freq = [0] * (generation_alleles+1) # Array where the index is the probability of index many recessive alleles appearing in the generation
     cur_gen_rec_allele_freq[allele_count] = 1 # For the initial generation, we know the exact number of recessive alleles. So probability is 1 for index@number_recessive, and 0 for all other indices


     # Because in the one generation case, we only need the first generation which has either 0 or 1 for each frequency,
     # we only need to calculate with frequencies == to 1 in the initial generation. This keeps the time complexity to a linear time complexity
     first_gen_allele_probs = []
     for num_alleles in range(0, generation_alleles + 1):
          first_gen_allele_probs.append(Distributions.binomial_pmf(generation_alleles, num_alleles, allele_count / generation_alleles))
     all_generations_rec_allele_freq.append(first_gen_allele_probs)


     # Create a probability vector for the next generation based on the current generation's probabilities, each index represents the probability of that many recessive alleles in the next generation
     for generation in range(1, num_generations):
          next_gen_rec_allele_freq = [0] * (generation_alleles + 1 )
          all_generations_rec_allele_freq.append(next_gen_rec_allele_freq)

          for alleles_in_next_gen in range(0, generation_alleles + 1):
               for alleles_in_prev_gen in range(0, generation_alleles + 1):
                    next_gen_rec_allele_freq[alleles_in_next_gen] += (all_generations_rec_allele_freq[generation - 1][alleles_in_prev_gen] * # Probability of reg alles in previous generation
                                                                           Distributions.binomial_pmf(generation_alleles, alleles_in_next_gen, alleles_in_prev_gen / generation_alleles)) # probability of exactly rec_alles in next ignoring previous generation 
     return all_generations_rec_allele_freq[-1]


def main(generation_size:int, dom_allele_count:int, num_generations:int, k:int):
          rec_allele_count = generation_size * 2 - dom_allele_count
          all_generations_rec_allele_freq = get_prob_of_allele_counts_after_k_generations(generation_size, rec_allele_count, num_generations, k)
          print(round(sum(all_generations_rec_allele_freq[k:]), 3)) # Sum all the probabilities of having k or more recessive alleles in the last generation


file_path = sys.argv[1]

generation_size, dom_allele_count, num_generations, k = list(map(int, GenericTextFile.get_generic_file_as_lines(file_path)[0].strip().split()))

main(generation_size, dom_allele_count, num_generations, k)





