""""""

import re
import sys
from collections import defaultdict, Counter

def main(dataset_name:str):
    with open(dataset_name, "r") as data_set:
        dna_strings = data_set.readlines()
        diff = 0
        for i in range(0, len(dna_strings[0])):
            if dna_strings[0][i] != dna_strings[1][i]:
                diff = diff + 1
        print(diff)
                               





        
main(dataset_name= sys.argv[1])