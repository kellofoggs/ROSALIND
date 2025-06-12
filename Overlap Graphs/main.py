
import re
import sys
from collections import defaultdict, Counter
import math
from io import TextIOWrapper
import textwrap

# Perfect place for linkedlist, we're only going to push and pop

'''
Note:
    This is rather slow, we have to loop over all of the elements in the adult rabbit list to sum them to 
    determine the number of offspring.
'''
def main(data_set:TextIOWrapper):
        sequence_file_contents = data_set.read()

        overlap_bound = 3
#         sequence_file_contents = '''>Rosalind_0498
# AAATAAA
# >Rosalind_2391
# AAATTTT
# >Rosalind_2323
# TTTTCCC
# >Rosalind_0442
# AAATCCC
# >Rosalind_5013
# GGGTGGG
# '''
        
        matches_list = re.split(">(.*)", sequence_file_contents)[1:] # Skip the blankspace match

        sequence_labels = matches_list[::2]
        sequence_list = list(map(lambda sequence: sequence.replace("\n",""), matches_list[1::2]))
        id_to_sequence_list = dict(zip(sequence_labels, sequence_list)) # This is a 
        # print(id_to_sequence_list)
        adjacencyy_set = set()

        for i_id in sequence_labels:
                i_sequence = id_to_sequence_list[i_id]
                for j_id in sequence_labels:
                        j_sequence = id_to_sequence_list[j_id]
                        if i_id != j_id and i_sequence[len(i_sequence) - overlap_bound:] == j_sequence[:overlap_bound] :
                                adjacencyy_set.add((f"{i_id} {j_id}"))

                        pass
    
        for item in adjacencyy_set:
                print(item)





dataset_name = sys.argv[1]

with open(dataset_name, "r") as data_set:
    main(data_set=data_set)
# main(data_set="RA")



