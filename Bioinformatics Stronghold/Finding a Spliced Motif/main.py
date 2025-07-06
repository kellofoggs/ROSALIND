from Utilities.InputFileTools import Fasta
import sys

input_file_name = sys.argv[1]

# fasta_strings = Fasta.get_fasta_as_list(fasta_string='''>Rosalind_14
# ACGTACGTGACG
# >Rosalind_18
# GTA
# ''')


def main(parent_string:str, subsequence_str:str):
    '''Done greedily as this is the simplest way I could think of solving this problem
       We don't care if the subsequence is contiguous or not, just that it's a subsequence
    '''
    subsequence = list(subsequence_str)
    cur_subseq_char = None
    subseq_locs = []
    for i in range(0, len(parent_string)):
        curr_par_char = parent_string[i]

        # Remove a character from the subsequence string 
        if cur_subseq_char == None:
            if len(subsequence) == 0:
                break
            else:
                cur_subseq_char = subsequence.pop(0)

        if cur_subseq_char == curr_par_char:
            subseq_locs.append(i+1) # Zero based indexing
            cur_subseq_char = None

        pass

    print(' '.join(list(map(str,subseq_locs))))


parent_string, subsequence = Fasta.get_fasta_as_list(fasta_file=input_file_name)
main(parent_string,subsequence)

