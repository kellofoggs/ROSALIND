from collections import defaultdict
from math import inf
from Utilities.InputFileTools import GenericTextFile
import sys
from typing import List
'''
Notes:
    * Mass spectrum: mass or mass/charge ratio of chemical particles in a sample
    * Mass spectra : Collection of mass spectrum

    * In biology we're often interested in seeing if two peptide chains came from the same protein
    * want to see how similar they are
    *  In a case where we know the two peptide chains do not overlap/contian one another we can use shared peaks counts.
    * This does not work in the case where we have 2 spectra, and one measure is for a peptide that is within a larger peptide chain that we have a measure for
    * In such a case there spectra may have a similar number of peaks, with a similar height , but they are shifted
    in different places. We should be able toshift the spectra by a value of X to align them

    * Multiset: A set where you can have duplicate elements. All sets are considered multisets
    * Multiplictity: How many times an element x appears in a multiset [0, +inf)
    
    * Minkowski sum: given multiset A and multiset B where both sets contain only real numbers
        - Multiset of all possible sums of elements a and b 
        mink_sum(A, B) = [a + b | for all a in A, and all b in B] 

    * Minkowski Difference: minkowski sum but subtraction instead of addition:
        mink_diff(A, B) = [a-b| for all a in A, and all b in B] 
        -


    
'''


'''
Problem:
Given multisets of positive real numbers A and B

Return the largest multiplicity of the minkowski difference A B

'''

def main(spectra_ms_one:List[float], spectra_ms_two:List[float]):
    mink_differences = defaultdict(int)
    highest_mink_difference_multiplicity = (0, -inf) # Tuple where the first element is the multiplicity and the second is the mink difference with the max multiplicity
    # Used to avoid having to sort to find the largest multiplicity    

    for a in spectra_ms_one:
        for b in spectra_ms_two:
            diff = round(a-b, 5)
            mink_differences[diff] = mink_differences[diff] +  1
            if mink_differences[diff] > highest_mink_difference_multiplicity[0]:
                highest_mink_difference_multiplicity = (mink_differences[diff], diff)

    print(f"{highest_mink_difference_multiplicity[0]}\n{highest_mink_difference_multiplicity[1]}")

input_file_path = sys.argv[1]
multi_set_string_one, multi_set_string_two = GenericTextFile.get_generic_file_as_lines(input_file_path)

multi_set_one = list(map(float, multi_set_string_one.split()))
multi_set_two = list(map(float, multi_set_string_two.split()))

main(multi_set_one, multi_set_two)
