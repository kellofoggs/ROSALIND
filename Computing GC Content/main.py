'''Every string in a FASTA file begins with a single-line that contains the symbol '>' along with some 
labeling information about the string. The word following the '>' symbol is the identifier of the 
sequence, and the rest of the line is its description (both are optional). There should be no space between
 the ">" and the first letter of the identifier.

All subsequent lines contain the string itself; it is recommended that all lines of text are shorter than 80
symbols. The string ends when another line starting with '>' appears, indicating the start of another 
sequence (or if the end of the file is reached).
'''

import re
import sys
from collections import defaultdict, Counter

def main(dataset_name:str):
    with open(dataset_name, "r") as data_set:
        dna_string = data_set.read()
        
        matches_list = re.split(">(.*)", dna_string)[1:]
        id_to_sequence_list = dict(zip(matches_list[::2], matches_list[1::2]))

        gc_rate_list = []
        largest_GC = None
        for key in id_to_sequence_list.keys():
            string = id_to_sequence_list[key].replace("\n","")
            # print(string)
            counter = Counter(string)

            current_GC_rate = round(100*(counter["G"] + counter["C"])/ len(string), 6)
            if largest_GC == None or largest_GC["rate"] < current_GC_rate:
                largest_GC = {"key": key, "rate": current_GC_rate}
        
        print(f"{largest_GC["key"]}\n{largest_GC["rate"]}")
            # elif largest_GC["rate"] < current_GC_rate:
            #     largest_GC = {"key": key, "rate": current_GC_rate}






        
main(dataset_name= sys.argv[1])