from Utilities.InputFileTools import Fasta
from collections import defaultdict
from Utilities.DNA import DNAStringTools
from typing import List, Tuple, Dict, Set
import sys
def get_reverse_comp_and_orig_dna_reads(dna_read_list:List[str]) -> List[str]:
    extended_dna_reads_list = list(map(DNAStringTools.reverse_complement_dna, dna_read_list))
    extended_dna_reads_list.extend(dna_read_list)
    return extended_dna_reads_list

def get_incorrect_and_correct_reads(extended_dna_reads_list:List[str]) -> Dict[str, Set]:
    '''
    Returns a set of incorrect and correct dna read strings
    extended_dna_reads_list: a list of dna string reads along with their reverse complements
    return: Two sets within a dictionary, where the keys are "incorrect" and "correct"
    '''
    read_counts_dict = defaultdict(int)

    for read in extended_dna_reads_list:
        read_counts_dict[read] = read_counts_dict[read] + 1


    incorrect_reads = set() # An incorrect read appears exactly once
    correct_reads = set()
    for read in read_counts_dict.keys():
        read_count = read_counts_dict[read]
        if read_count >= 2:
            correct_reads.add(read)
            pass
        else:
            incorrect_reads.add(read)

    return {
        'correct': correct_reads,
        'incorrect': incorrect_reads
    }


def main(dna_read_list:List[str]):
    '''
    Strategy: first get a list of dna_reads and their reverse complements
             Find out which strings are "correct" and incorrect by counting how often they appear in the list
             For the incorrect strings in the original dna_read_list compare them to the correct strings in the comobined dna set
             For pairs of incorrect reads and correct reads with a hamming distance of 1, we will consider incorrect->correct as the proper correction
             (Note: we can in theory have multiple corrections for an incorrect, but the problem data set specifies we will unique 1 hamming distance [correct,incorrect] pairs 
             so we can use optimistic/greedy search.


    '''

    extended_dna_reads_list = get_reverse_comp_and_orig_dna_reads(dna_read_list)
    dna_reads_map = get_incorrect_and_correct_reads(extended_dna_reads_list)

    incorrect_reads = dna_reads_map["incorrect"]
    correct_reads = dna_reads_map["correct"]

    incorrect_reads = incorrect_reads.intersection(set(dna_read_list))
    corrections:List[Tuple[str,str]] = []

    for incorrect_read in incorrect_reads:
        for correct_read in correct_reads:
            dna_diffs = DNAStringTools.count_point_mutations(incorrect_read, correct_read)
            if dna_diffs == 1:
                corrections.append((incorrect_read, correct_read))
    
    for correction in corrections:
        print(f"{correction[0]}->{correction[1]}")

file_path = sys.argv[1]




dna_read_list:List = Fasta.get_fasta_as_list(fasta_file=file_path)
main(dna_read_list)



# First add the reverse complements of the reads to our reads list




