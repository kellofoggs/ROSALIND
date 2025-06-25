from Utilities.DNA import ProbabilityTools
from math import comb, factorial
from Utilities.InputFileTools import GenericTextFile
from typing import Dict, List
from decimal import Decimal, ROUND_HALF_UP
import sys



'''
Inputs: 
    n: length of random string
    s: substring
    A: GC Content array
'''

def main(random_dna_str_len:int, dna_substring:str, gc_contents:List[float]):

    substring_len = len(dna_substring)
    possible_occurences = num_sub_fits_into_super(substring_len, random_dna_str_len)
    # Calculate the probability of the string occuring, given that it has enough space to occur
    # Multiply this possibility with the number of times the string can occur ( when it's given space to occur)
    string_probs = list(map(round_decimal,[Decimal(possible_occurences*ProbabilityTools.caclulate_dna_probability(gc_content=gc_content,dna_string=dna_substring))
                    for gc_content in gc_contents]))
    
    print(" ".join(map(str,string_probs)))
    

    pass

def num_sub_fits_into_super(substring_len:int, super_string_len:int)-> int:
    # A substring of length n can fit into a random string of length x: x-n+1 times if overlap is allowed
    # This assumes that the substring length is at most the same as the string length

    return super_string_len - substring_len + 1
    
    pass

def round_decimal(value: Decimal, digits: int=3) -> Decimal:
    # Used because for whatever reason python defaults to nearest even when a 5 is after the cutoff decimal
    precision = Decimal('1.' + '0' * digits)
    return value.quantize(precision, rounding=ROUND_HALF_UP)

file_path = sys.argv[1]
random_dna_string_len, substring, gc_contents = GenericTextFile.get_generic_file_as_lines(file_path)
random_dna_string_len = int(random_dna_string_len)
gc_contents = map(float,gc_contents.split())

main(random_dna_string_len, substring, gc_contents)

