from Utilities.InputFileTools import GenericTextFile
import sys
from math import factorial
file_name:str = sys.argv[1]




def main(collection_size:int, group_size:int):


    # The formula for partial permutation is n! / (n-r)!
    # Where n is the size of the collection and r is the size of the permutation
    num_partial_permutations = factorial(collection_size)/factorial((collection_size-group_size))
    print((num_partial_permutations % 1000000))



collection_size, group_size = list(map(int,GenericTextFile.get_generic_file_as_lines(file_name)[0].split()))
main(collection_size, group_size)