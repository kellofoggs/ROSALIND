from Utilities.DNA import DNAStringTools
from Utilities.InputFileTools import Fasta
import sys
import re
from typing import List

def main(dna_string:str, exons:List):
    
    # exons_translation = dict([(exon, " ") for exon in exons])
    intron_pattern = f'({"|".join(exons)})'
    exon_string = re.sub( intron_pattern, "", dna_string)
    print(DNAStringTools.translate_dna_to_amino_acid(exon_string))
    # print(exons_translation)
    # dna_string.translate(str.maketrans(exons_translation))

fasta_file_path = sys.argv[1]
dna_string, *exons = Fasta.get_fasta_as_list(fasta_file=fasta_file_path)
main(dna_string, exons)