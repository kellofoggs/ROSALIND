
from math import log10
from Utilities.InputFileTools import GenericTextFile
from collections import Counter
from typing import List
import sys
# The goal here is to see if we can tell how probable a string is based on gc content


# GC content is the proportion of the dna sample that is either Guanine or cytosine.
# 1- GC content is the AT content in DNA, and AU content in RNA

# We assume that GC content is split evenly between G and C so we divide the GC content to get the probability of a char being G or C
# Similarly with AT the probability of being A or T is (1 - GC)/2

# input_string = '''ACGATACAA
# 0.129 0.287 0.423 0.476 0.641 0.742 0.783
# '''
def main(dna_string:str, gc_content_arr:List[float]):


    string_char_count = Counter(dna_string)
    A_T_Count = string_char_count["A"] + string_char_count["T"]
    GC_Count = string_char_count["G"] + string_char_count["C"]
    log_prob_string_matches_with_GC = []

    for gc_content in gc_content_arr:
        log_gc_prob = log10(gc_content/2)
        log_at_prob = log10((1-gc_content)/2)

        base_matches_log_prob = sum(A_T_Count*[log_at_prob]) + sum(GC_Count*[log_gc_prob])
        

        log_prob_string_matches_with_GC.append(str(round(base_matches_log_prob, 3)))            
        pass

    # list(map(lambda log_prob: round(log_prob, 3), log_prob_string_matches_with_GC))
    print(" ".join(log_prob_string_matches_with_GC))

# Process the input file first line is the string, second line is probabilities
dna_string, gc_content_arr = GenericTextFile.get_generic_file_as_lines(sys.argv[1])
gc_content_arr = list(map(float, gc_content_arr.split()))

main(dna_string, gc_content_arr)