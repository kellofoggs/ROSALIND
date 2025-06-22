from typing import List
import sys
from math import comb
from Utilities.DNA import ProbabilityTools
from Utilities.InputFileTools import GenericTextFile
'''90000 0.6
ATAGCCGA
'''


# Given N random DNA strings of the same length as a dna string S, and a GC content
# Determine the probability of 1 or more strings being equal to s


# If this is at most 10 basepairs then we don't have to worry about float overflow with probability of string occuring

# This screams binomial distribution as we're allowed replacement and we have a s

def main(num_strings:int, gc_content:float, dna_string:str):
    prob = ProbabilityTools.caclulate_dna_probability(gc_content, dna_string)
    
    # We're interested in the probability that the dna string appears once or more
    # This is equivalent to 1 - the probability it never appears at all
    # We have the probability of it appearing from the gc content
    # We simply plug it back into the binomial distribution to get the probability of it never appearing
        
    # prob ** 0 and n choose 0 will always be 1, we could omit this but I want it to be clear we're doing binomial
    output =  comb(num_strings, 0) * ((prob**0) *((1-prob) **(num_strings)))  

    print(round((1-output), 3))

    pass

file_path = sys.argv[1]

file_contents:List[str] = GenericTextFile.get_generic_file_as_lines(file_path)
num_strings, gc_content = file_contents[0].split()
num_strings = int(num_strings)
gc_content = float(gc_content)
dna_string = file_contents[1]

main(num_strings, gc_content, dna_string)

