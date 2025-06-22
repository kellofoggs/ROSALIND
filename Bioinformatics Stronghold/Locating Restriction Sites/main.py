from Utilities.InputFileTools import Fasta
from Utilities.DNA import StringTools
import sys
'''
Notes:
    * A DNA string S is a reverse palindrome if it's reverse complement S' is equal to S
    * We could check if every 4-12 substring of S is in S' somewhere. If it is then the string is a reverse palindrome
    * We know where to check in S' for the string in S. It's location is the same as it's location in S but from the opposite side 
    i.e. if it's at 4 in S it starts at -(4+length of sub) in S' with 1 based indexing
    * The brute force method of this  has O(2^n) if the windows are size 1. However wiwhich is NP and pretty trash of a solution
    * 
'''




dna_string = Fasta.get_fasta_as_list(sys.argv[1])[0]


# print(StringTools.reverse_complement_dna(dna_string))
reverse_complement = StringTools.reverse_complement_dna(dna_string)

dna_string_len = len(dna_string)

max_window_size = 12
min_window_size = 4


def find_reverse_palindromes(dna):
    n = len(dna)
    revcomp = StringTools.reverse_complement_dna(dna)
    result = []

    for l in range(4, 13):
        for i in range(n - l + 1):
            j = i + l
            rev_start = n - j
            if dna[i:j] == revcomp[rev_start:rev_start + l]:
                result.append((i + 1, l))  # 1-based indexing

    return result

rev_pals = find_reverse_palindromes(dna_string)
for position, length in rev_pals:
    print(position, length)



