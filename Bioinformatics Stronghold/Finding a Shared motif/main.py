from Utilities.InputFileTools import Fasta
from typing import List
import sys
# dna_strings = sorted(Fasta.get_fasta_as_list(fasta_string='''>Rosalind_1
# GATTACA
# >Rosalind_2
# TAGACCA
# >Rosalind_3
# ATACA'''
#                                       )
# , key= len)
# print(dna_strings)

# This approach is very slow but it works, we can use suffix trie instead to do it in linear time

def main(dna_strings:List[str]):
    dna_strings = sorted(dna_strings, key= len)
    shortest_seq = dna_strings[0]

    substrings_of_shortest_string = sorted([shortest_seq[i:j] for i in range(len(shortest_seq)) for j in range(i+1, len(shortest_seq)+1)], key=lambda string: len(string), reverse=True)

    # print(substrings_of_shortest_string)

    other_strings = dna_strings[1:]
    len_other_strings = len(other_strings)
    for substring in substrings_of_shortest_string:
        num_seen = 0
        for index in range(0, len_other_strings):
            if substring not in other_strings[index]:
                break
            else: 
                num_seen = num_seen + 1

        if num_seen == len_other_strings:
            print(substring)
            return
            
            pass

dna_file_name = sys.argv[1]
dna_strings = Fasta.get_fasta_as_list(dna_file_name)
main(dna_strings)