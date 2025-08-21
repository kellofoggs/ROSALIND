'''

This problem is considered to be an example of the traveling salesman problem.
It is NP-hard, and there is no known guaranteed polynomial time solution without constraints.
However thankfully we are given a dataset that satisfies the following condition:
There exists a unique way to reconstruct the entire chromosome from these reads by 
gluing together pairs of reads that overlap by more than half their length.

There is a D-P algorithm that can be used to solve this problem in O(n^2 2^n) time where n is the number of input strings
but it is not implemented here. This is known as the Held-Karp algorithm.

There is a very clear problem with treating the shortest superstring problem as a valid way of DNA assembly.
If there are duplicate strings in a DNA reading, the shortest superstring may not be the correct assembly. Who is to say that the duplicate reading
is caused by a sequencing error or that it is a valid reading of the DNA? If it's a valid reading of the DNA then the shortest superstring will not be the correct assembly as
it will be merged with other duplicate strings.

My solution is what is known as a mickey mouse solution. It only works for the dataset provided, and does not guarantee a correct assembly
without the constraints specified by Rosalind. However it runs in a reasonable time complexity.
creating a lps array takes O(n+m) time where n is the length of the first string and m is the length of the second string.
We do this for every pair of strings in the worst-case, so the time complexity is O(k^2 * (n+m)) where k is the number of input strings and m is the average length of the strings.


Reference material for shortest superstring:
    https://math.mit.edu/~goemans/18434S06/superstring-lele.pdf
    https://www.youtube.com/watch?v=QykgNu0vdos
    https://www.youtube.com/watch?v=BHUgDbVC4js
'''


from typing import List


from Utilities.Search import KMP
from Utilities.InputFileTools import Fasta
import sys
from datetime import datetime as dt

def combine_strings(string_one:str, string_two:str, overlap_threshold:int=None) -> str:
    ''' The dataset is guaranteed to satisfy the following condition: there exists a unique way to 
    reconstruct the entire chromosome from these reads by gluing together pairs of reads that overlap by
     more than half their length.

     This means that if over half of the second string is in the first we string we combine them and are guaranteed to get the correct combination
    '''

    """
    What we want to do is look at the second half of the first string and see where 
    it has the same ordered chars as the first half of the second string
    We're trying to find the point in string one where the most of the first half of string two can reside
    """
    
    s_one_len = len(string_one)

    s_two_len = len(string_two)
    if overlap_threshold is None:
        overlap_threshold = min(s_one_len//2, s_two_len//2)


    # What we want to do is see how much of the suffix of the first string overlaps with the prefix of the second string
    # If the overlap is past our overlap threshold, we can combine the two strings
    # Else we will return None

    num_overlap_chars = find_max_overlaps(string_one, string_two)

    if num_overlap_chars > overlap_threshold:
        output = string_one + string_two[num_overlap_chars:]
        return output
    else:
        return None

def find_max_overlaps(prefix_string, suffix_strings:str) -> int:
    ''' Take in a prefix string, and list of suffix strings
        Return the maximum overlap between the two strings 
        
    '''

    # We will use the lps borrowed from the KMP algorithm to find the maximum overlap between the two strings
    # If we construct a string that is the second string + <a_char_we_know_is_outside_the alphabet of the two strings)> + the first string
    # We can use the lps array to find the maximum overlap between the two strings (as the lps array will tell us how many characters match between the
    # prefix of the second string and the suffix of the first string)

    combined_strings = f'{suffix_strings}#{prefix_string}'
    max_overlap = KMP.generate_lps(combined_strings)[-1]  # The last value in the lps array will tell us the maximum overlap between the two strings
    return max_overlap


def main(strands:List[str]):
    strands_set = sorted(list(set(strands)), key= lambda x: len(x)) # Ensure we have no duplicate strands
    if len(strands_set) == 1:
        print(strands_set[0])
        return



    threshold = min((len(strands_set[0])+1)//2, (len(strands_set[1])+1)//2)
    print(f"Threshold: {threshold}")
    i, j = 0, 0
    while len(strands_set) > 1:


        while i < len(strands_set):

            while j < len(strands_set):

                
                if i != j:

                    combined = combine_strings(strands_set[i], strands_set[j], overlap_threshold= threshold )

                    if combined is not None:  
                        strands_set.pop(max(i,j)) # Remove larger index first to avoid index errors

                        strands_set.pop(min(j,i))
                        strands_set.append(combined)
                        
                        i = 0  # Reset i and j to start from the beginning again
                        j = 0  
                        continue
                j += 1
            j = 0
            i += 1

        print(combined)


file_path = sys.argv[1]
strands = Fasta.get_fasta_as_list(file_path)



main(strands)