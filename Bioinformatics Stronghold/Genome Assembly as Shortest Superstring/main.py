from typing import List

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



def find_max_overlaps(prefix_string, suffix_strings:List[str]) -> List:
    ''' Take in a prefix string, and list of suffix strings
        Return the strings that have the most overlap between each prefix and suffix string
        (Output list has the same length as the suffix_strings list)
    '''


    pass










# head_strand = strands.pop(0) # Smallest possible strand, which is just 

# while len(strands) > 0:
#     next = strands.pop(0)
#     head_strand = combine_strings(head_strand, next)
#     # print(head_strand)

# print(head_strand)
# combine_strings(head_strand, strands[0])

'''
overlaps = []
overlapping = []
for i in range(len(strands)):
    curr_read = strands[i]
    for j in range(len(curr_read) // 2, len(curr_read)):
        curr_suffix = curr_read[-(j + 1):]
        for k in range(len(strands)):
            curr_comp = strands[k]
            for l in range(len(curr_comp) // 2, len(curr_comp)):
                curr_prefix = curr_comp[:l]
                if curr_suffix == curr_prefix:
                    overlaps.append(k)
                    overlapping.append([len(curr_suffix), i, k])

s = set(overlaps)
first_read = ''
count = len(overlapping)
for m in range(len(overlapping)):
    suf_index = overlapping[m][1]
    if suf_index not in s:           #find first read and initialise new str
        first_read = suf_index
        new_str = strands[overlapping[m][1]] + strands[overlapping[m][2]][
            overlapping[m][0]:]
        count -= 1
        pref_index = overlapping[m][2]
        while count > 0:                       #when the first read is found, add 
            for n in range(len(overlapping)):  #the remaining in the correct order
                if pref_index == overlapping[n][1]:
                    new_str += strands[overlapping[n][2]][overlapping[n][0]:]
                    pref_index = overlapping[n][2]
                    count -= 1

print(new_str)
'''