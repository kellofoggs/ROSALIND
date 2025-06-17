import sys
import re
import itertools
from math import factorial

def main(sequence:str):
    # A perfect matching is a set of edges within the graph so that all nodes are represented with edges without any one node appearing in more than one edge
    #  


    # There is a guaranteed equal number of adenine and uracil, by counting the number of adenine we will also be counting the number of possible AU basepairs
    # There is a guaranteed equal number of guanine and cytosine, the above principle applies
    # We can take two cuts of the graphs splitting based on whether the edges form an au pair or gc pair
    pot_au_pairs = 0 
    pot_gc_pairs = 0
    for char in sequence:
        if char == "A":
            pot_au_pairs = pot_au_pairs + 1
        elif char == "G":
            pot_gc_pairs = pot_gc_pairs + 1
    print(pot_au_pairs)
    print(pot_gc_pairs)
    # There are pot_au_pairs! * pot_gc_pairs! ways to arrange these
    print(factorial(pot_au_pairs) * factorial(pot_gc_pairs))
    

data_set_name = sys.argv[1]

with open(data_set_name) as data_set:
    dna_string = data_set.read()
            
    matches_list = re.split(">(.*)", dna_string)[1:] # Skip the blankspace match

    sequence_label = matches_list[::2]
    sequence_list = list(map(lambda sequence: sequence.replace("\n",""), matches_list[1::2]))
    print(sequence_list)
    main(sequence= sequence_list[0])
    pass



'''with open(data_set_name) as data_set:
    dna_string = data_set.read()
            
    matches_list = re.split(">(.*)", dna_string)[1:] # Skip the blankspace match

    sequence_label = matches_list[::2]
    sequence_list = list(map(lambda sequence: sequence.replace("\n",""), matches_list[1::2]))
    id_to_sequence_list = dict(zip(sequence_label, sequence_list))
    print(sequence_list)
    pass
'''