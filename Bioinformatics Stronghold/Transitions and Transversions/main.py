from Utilities.InputFileTools import Fasta
from typing import List
import sys
'''New vocab: 
        * pyrimideine: A nucleobase in the followinge set {Cytosine, Thymine, Uracil}
        * Purine:  A nucleobase in the following set {Adenine, Guanine}

        New Point Mutation Types:
            * Transitions - substitute a purine for a purine, or substitutes a pyrmidine for a pyrimidine
            * Transversions - Pyrimidine <-> Purine, more drastic change to base chemical structure, so less common than transitions
            * coding region - The exons (part of the genome that are turned into mrna and eventually aminoacids->proteins )
            * Silent substitution - When the end-result protein is not affected by the mutation
        Info: 
            The ratio transitions:transversions is 2 on average, but higher in coding regions. 

            Therefore finding a region with a high ratio of transitions to transversions helps to identity a coding region of a genome

            A transition in a coding region is less likely to change the amino acid when the substituted base is the third member of a codon
            


'''


# Input two DNA strings of equal length


# Return the transition/transversion ratio

purines = set(["A", "G"])
pyrimidines = set({"C","T","U"}) # We can leave out Uracil as this is DNA but it helps to acknowledge that uracil is a pyrmidine too

def main(dna_strings:List[str]):
    dna_string_one = dna_strings[0]
    dna_string_two = dna_strings[1]
    num_transition = 0
    num_transversion = 0
    for i in range(0, len(dna_string_one)):
        
        nuc_one = dna_string_one[i]
        nuc_two = dna_string_two[i]

        # Check if the nucleobases are different
        if nuc_one != nuc_two:
            # If the two are different the mutation is either transition or  transversion
            if is_transition(nuc_one, nuc_two):
                num_transition = num_transition + 1
            else:
                num_transversion = num_transversion + 1
            pass
    print(num_transition/num_transversion)
def is_transition(nuc_one:str, nuc_two:str):
    '''Returns True if the mutation is a transition (purine for purine, pyrimidine for pyrimidine)'''
    return (nuc_one in purines and nuc_two in purines) or (nuc_one in pyrimidines and nuc_two in pyrimidines)

dna_file_path = sys.argv[1]

dna_strings = Fasta.get_fasta_as_list(fasta_file=dna_file_path
)
main(dna_strings)