from Utilities.InputFileTools import Fasta
from typing import Dict
import sys
fasta_string='''>Rosalind_1
ATCCAGCT
>Rosalind_2
GGGCAACT
>Rosalind_3
ATGGATCT
>Rosalind_4
AAGCAACC
>Rosalind_5
TTGGAACT
>Rosalind_6
ATGCCATT
>Rosalind_7
ATGGCACT'''

nucleotides = ["A", "C", "G", "T"]


fasta_file = sys.argv[1]
# sequence_list = Fasta.get_fasta_as_list(fasta_string)
sequence_list = Fasta.get_fasta_as_list(fasta_file)
dna_string_len = len(sequence_list[0])

# A numpy matrix would probably be better, but I don't want people to require numpy to try this out

consensus_count_dict = {
                        "A": dna_string_len*[0],
                        "T": dna_string_len*[0],
                        "C": dna_string_len*[0],
                        "G":dna_string_len*[0]


}

for i in range(0, dna_string_len):
    for sequence_string in sequence_list:
        sequence_char = sequence_string[i]
        consensus_count_dict[sequence_char][i] = consensus_count_dict[sequence_char][i] + 1

def get_max_nuc_from_table_at_index(dictionary:Dict, index:int):

    options_at_index = [ (nucleotide, dictionary.get(nucleotide)[index]) for nucleotide in nucleotides]
    most_abundant_nucleotide = options_at_index[0]
    for i in options_at_index:
        if most_abundant_nucleotide[1] < i[1]:
            most_abundant_nucleotide = i
    return most_abundant_nucleotide[0]
    pass


def print_char_count_row(char_count_header, char_count_list):

    output_count_list = list(map(str, char_count_list))
    output = f"{char_count_header}: {' '.join(output_count_list)}"
    print(output)
    pass
output = ""

for i in range(0, dna_string_len):
    most_aboundant_nuc_at_i = get_max_nuc_from_table_at_index(consensus_count_dict, i)
    output = output + most_aboundant_nuc_at_i

print(output)
for nuc in nucleotides:
    print_char_count_row(nuc, consensus_count_dict[nuc])
