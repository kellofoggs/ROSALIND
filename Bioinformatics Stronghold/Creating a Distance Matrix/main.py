from Utilities.InputFileTools import Fasta
from typing import Dict, Set, List
import sys
fasta = '''>Rosalind_9499
TTTCCATTTA
>Rosalind_0942
GATTCATTTC
>Rosalind_6568
TTTCCATTTT
>Rosalind_1833
GTTCCATTTA'''


# There is a very obvious O(mn^2) solution where m is the length of the string and n is the number of strings
# strand_list = Fasta.get_fasta_as_list(fasta_string=fasta)
strand_list = Fasta.get_fasta_as_list(fasta_file=sys.argv[1])
strand_list_len = len(strand_list)
strand_len = len(strand_list[0])
distance_matrix = []
print(distance_matrix)

for i in  range(0, strand_list_len):
    strand_one = strand_list[i]
    for j in range(0, strand_list_len):
        strand_two = strand_list[j]

        pass
def point_mutation_count(strand_one, strand_two)->float:
    count = 0
    for i in range(0, len(strand_one)):
        if strand_one[i] != strand_two[i]:
            count = count + 1

    return count

    pass
# def get_strand_match_indices(strand_one:str, strand_two:str)->Set:
#     strand_one_len = len(strand_one)
#     strand_two_len = len(strand_two)
#     differing_indices = set()
#     if strand_one_len == strand_two_len:
#         for i in range(0, len(strand_one)):
#             # print(strand_one[i], strand_two[i])
#             # print()
#             if strand_one[i] != strand_two[i]:
#                 differing_indices.add(i)
#     else:
#         raise ValueError("The two strands must be of the same length")
#     return differing_indices


# list_of_differences = [] # This is the list of differences between the first dna strand other strands
# for i in range(0, strand_list_len):
#     list_of_differences.append(get_strand_match_indices(strand_list[0], strand_list[i]))

# print(list_of_differences)

for i in range(0, len(strand_list)):
    outputs_arr = []
    for j in range(0, len(strand_list)):
        outputs_arr.append(
            str(
                round(
                    (point_mutation_count(strand_list[i], strand_list[j])/strand_len)
            , 5)))
    print(" ".join(outputs_arr))
        

# To find the difference between strand 3 and strand 2, we can see where strand 2 differed from strand 0, and where strand 3 differed from strand 0
# The difference between strand 3



# If what we're interested is simply proportion of differences between a closed set maybe we 
# Can do this in O(m*n) time complexity. 
# Comp
