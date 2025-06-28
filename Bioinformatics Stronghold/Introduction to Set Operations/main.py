import sys
from typing import Set
from Utilities.InputFileTools import GenericTextFile
import re
'''
Given: A positive integer n such that (n <= 20,000) and two subsets A and B of {1,2,…,n}



'''





# print(num_set)
def convert_set_string_enc_to_set(set_string:str) -> Set:
    # Greedily find all numbers in the set string.
    # This implementation only works with numbers
    # Ideally we would want to remove the curly brackets and split on comma spaces
    '''    pattern = "[0-9]+"
    numbers = map(lambda match: match.group(), re.finditer(pattern, set_string))'''

    replacements = str.maketrans({
        "{": "",
        "}": ""
    })

    numbers = set_string.translate(replacements).strip().split(", ")
    num_set = set(map(int,numbers))    
    # print(num_set)
    return num_set


def set_complement(source_set:Set, universal_set:Set) -> Set:
    '''
    The set complement is the elements in the universal set that are not found in the source set
    '''
    return universal_set - source_set



def main(universal_set_size, set_one_string, set_two_string ):
    set_one = convert_set_string_enc_to_set(set_one_string)
    set_two = convert_set_string_enc_to_set(set_two_string)
    
    universal_set = set(range(1, universal_set_size+1))

    print(set_one.union(set_two))
    print(set_one.intersection(set_two))
    print(set_one - set_two)
    print(set_two-set_one)
    print(set_complement(source_set=set_one, universal_set=universal_set))
    print(set_complement(source_set=set_two, universal_set=universal_set))

input_file_path = sys.argv[1]
inputs = GenericTextFile.get_generic_file_as_lines(file= input_file_path) # First line is u set size, second line is set string for a, 3rd line is set string for b
main(int(inputs[0]), inputs[1], inputs[2]) 



