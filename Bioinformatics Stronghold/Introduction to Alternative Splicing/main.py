from math import comb, factorial
from Utilities.InputFileTools import GenericTextFile
import sys
'''
New Vocab: 
    * Protein Isoforms - Different forms of a protein
    * Exon skipping - omission of certain exons from mRNA to form different proteins
    * Alternative Splicing -  

'''

def main(n, m):
    ''' Summation of (n c k % 1000000) where each k is an integer between M and n'''

    # n = 6
    # m = 3
    # print(n)
    # print(m)
    output = 0
    for k in range(m, n+1):
        # new_comb = 
        # print(new_comb)
        output += comb(n,k)

    output = output % 1000000
    print(output )

file_path = sys.argv[1]
n,m = map(int,GenericTextFile.get_generic_file_as_lines(file_path)[0].split())
main(n, m)

