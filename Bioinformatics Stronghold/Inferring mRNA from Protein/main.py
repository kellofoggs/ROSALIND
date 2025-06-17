
import re
import sys
from collections import defaultdict, Counter
import math
from io import TextIOWrapper
import textwrap

def main(data_set:TextIOWrapper):

    protein_string = data_set.readline().replace("\n","")

    protein_to_num_RNA_strings(protein_string=protein_string)

def protein_to_num_RNA_strings(protein_string:str):

    # Dictionary where key is the amino acid english language symbol
    # Value is a set of RNA codons that encode for that value
    codons = ["UUU", "UUC", "UUA", "UUG", "UCU", "UCC", "UCA", "UCG", "UAU", "UAC", "UAA", "UAG", 
    "UGU", "UGC", "UGA", "UGG", "CUU", "CUC", "CUA", "CUG", "CCU", "CCC", "CCA", "CCG", 
    "CAU", "CAC", "CAA", "CAG", "CGU", "CGC", "CGA", "CGG", "AUU", "AUC", "AUA", "AUG", 
    "ACU", "ACC", "ACA", "ACG", "AAU", "AAC", "AAA", "AAG", "AGU", "AGC", "AGA", "AGG",
    "GUU", "GUC", "GUA", "GUG", "GCU", "GCC", "GCA", "GCG", "GAU", "GAC", "GAA", 
    "GAG", "GGU", "GGC", "GGA", "GGG"]



    amino_acids = ["F", "F", "L", "L", "S", "S", "S", "S", "Y", "Y", "Stop", "Stop", "C", "C", "Stop",
      "W", "L", "L", "L", "L", "P", "P", "P", "P", "H", "H", "Q", "Q", "R", "R", "R", 
      "R", "I", "I", "I", "M", "T", "T", "T", "T", "N", "N", "K", "K", "S", "S", "R", 
      "R", "V", "V", "V", "V", "A", "A", "A", "A", "D", "D", "E", "E", "G", "G", "G", "G"]
    
    codon_to_amino_acid = dict(zip(codons, amino_acids))
    amino_acid_to_codon_count = defaultdict(int)
    # amino_acid_to_codon = defaultdict(set) # If you want to keep the specific codons as well, not required for this problem

    for i in range(0, len(codons)):
        codon = codons[i]
        amino_acid = amino_acids[i]
        amino_acid_to_codon_count[amino_acid] = amino_acid_to_codon_count[amino_acid] + 1
    print(amino_acid_to_codon_count)

    possible_mrna_strings = 1
    for j in range(0, len(protein_string)):
        amino_acid = str(protein_string[j])
        possible_mrna_strings = possible_mrna_strings * amino_acid_to_codon_count[amino_acid]
    possible_mrna_strings = possible_mrna_strings * amino_acid_to_codon_count["Stop"]
    print(possible_mrna_strings % (10**6))


    



    

    pass

dataset_name = sys.argv[1]

with open(dataset_name, "r") as data_set:
    main(data_set=data_set)
# main(data_set="RA")

# protein_to_num_RNA_strings("MA")