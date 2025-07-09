
import re
import sys
from collections import defaultdict, Counter
import math
from io import TextIOWrapper
import textwrap
from Utilities.InputFileTools import Fasta


def main(data_set:TextIOWrapper):
        overlap_bound = 3

        sequence_map = Fasta.get_fasta_as_dict(data_set)

        adjacency_set = set()
        print(sequence_map)
        for i_id in sequence_map.keys():
                i_sequence = sequence_map[i_id]
                for j_id in sequence_map.keys():
                        j_sequence = sequence_map[j_id]
                        if i_id != j_id and i_sequence[len(i_sequence) - overlap_bound:] == j_sequence[:overlap_bound] :
                                adjacency_set.add((f"{i_id} {j_id}"))

                        pass
    
        for item in adjacency_set:
                print(item)





dataset_name = sys.argv[1]

with open(dataset_name, "r") as data_set:
    main(data_set=data_set)
# main(data_set="RA")



