

import re



def combine_strings(string_one:str, string_two:str):
    # max over lap is half of the string. This is the first half in string two. The second half in string one
    
    """
    What we want to do is look at the second half of the first string and see where 
    it has the same ordered chars as the first half of the second string
    We're trying to find the point in string one where the most of the first half of string two can reside
    """
    
    s_one_len = len(string_one)

    s_two_len = len(string_two)
    s_two_counter = 0 # s_two_counter is the index of the first non substring part of the second string 
    s_one_window = string_one
    s_two_window = string_two[:s_two_len//2]
    
    while s_two_counter < s_two_len:

        if s_one_window.endswith(s_two_window):
            # print(s_two_counter)
            print(s_two_window)
            s_one_offset = 1+ (len(s_one_window) - len(s_two_window))
            new_string = string_one[:s_one_offset] + string_two[s_two_counter:]
            # print(string_one)
            # print(string_two)
            print(new_string)
            return new_string 
            
            break
        else:
            s_two_window = s_two_window[:-1]
        s_two_counter  = s_two_counter + 1

    
    
    
  
    return None
strands = ["ATTAGACCTG",
"CCTGCCGGAA",
"AGACCTGCCG",
"GCCGGAATAC"]

head_strand = strands.pop(0) # Smallest possible strand, which is just 

while len(strands) > 0:
    next = strands.pop(0)
    head_strand = combine_strings(head_strand, next)
    # print(head_strand)

# print(head_strand)
# combine_strings(head_strand, strands[0])