from Utilities.StringTools import KMP
from Utilities.InputFileTools import Fasta
import sys

'''
The goal here is to prove that we've actually used KMP by printing out our lps array
'''
def main(dna_string:str):
    print(" ".join(list(map(str, KMP.generate_lps(dna_string)))))
    pass

file_name = sys.argv[1]
dna_string = Fasta.get_fasta_as_list(fasta_file=file_name)[0]
main(dna_string)