
import re
import sys
from collections import defaultdict, Counter
import math
from io import TextIOWrapper
import textwrap

def main(data_set:TextIOWrapper):

    source_string, query_string = data_set.readline().replace("\n",""), data_set.readline().replace("\n","")
    
    zero_indices =  [match.start() for match in re.finditer( f"(?={query_string})",source_string)]
    print(zero_indices)
    for i in range(0, len(zero_indices)):
        if i != len(zero_indices) -1:
            string_end = " "
            
        else:
            string_end = ""
        print(f"{zero_indices[i] + 1}", end=string_end)
    

dataset_name = sys.argv[1]

with open(dataset_name, "r") as data_set:
    main(data_set=data_set)
# main(data_set="RA")