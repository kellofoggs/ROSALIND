from typing import List
import sys
from Utilities.InputFileTools import GenericTextFile




def make_lexographic_strings(alphabet_string:str, string_length=2):
    k_mer_len = 2
    alphabet_list = alphabet_string.split()

    if string_length == 1:
        return alphabet_list

    output_list = len(alphabet_list)*[list()]
    enumeration = make_string_recur(alphabet_list,alphabet_list, count=string_length, current_layer=0)
    for word in enumeration:
        print(word)

    pass


def make_string_recur(prev_layer:List,base_layer:List, count=0, current_layer=0):

    
    if current_layer == count - 1:
        return prev_layer
    
    # prev_layer = []
    curr_layer = []
    for i in range(0, len(prev_layer)):
        for j in range(0, len(base_layer)):
            curr_layer.append(prev_layer[i] + base_layer[j])


    next_layer = make_string_recur(curr_layer ,base_layer, count, current_layer+1)
    
    return next_layer

    

def main(alphabet_string:str, string_length:int):
    make_lexographic_strings(alphabet_string, string_length)

file_lines = GenericTextFile.get_generic_file_as_lines(file=sys.argv[1])
main(alphabet_string=file_lines[0], string_length=int(file_lines[1]))
