'''

RNA Codon table, translates 3 sequence Codon to an alphabetical representation of a protein
UUU F      CUU L      AUU I      GUU V
UUC F      CUC L      AUC I      GUC V
UUA L      CUA L      AUA I      GUA V
UUG L      CUG L      AUG M      GUG V
UCU S      CCU P      ACU T      GCU A
UCC S      CCC P      ACC T      GCC A
UCA S      CCA P      ACA T      GCA A
UCG S      CCG P      ACG T      GCG A
UAU Y      CAU H      AAU N      GAU D
UAC Y      CAC H      AAC N      GAC D
UAA Stop   CAA Q      AAA K      GAA E
UAG Stop   CAG Q      AAG K      GAG E
UGU C      CGU R      AGU S      GGU G
UGC C      CGC R      AGC S      GGC G
UGA Stop   CGA R      AGA R      GGA G
UGG W      CGG R      AGG R      GGG G 

'''

import re
import sys
from collections import defaultdict, Counter
import math
from io import TextIOWrapper
import textwrap

def main(data_set:TextIOWrapper):
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
    
    for i in range(0,len(amino_acids)):
        if amino_acids[i] == "Stop" or amino_acids[i] == "Start":
            print(i)
    codon_to_amino_acid = dict(zip(codons,amino_acids))

    mrna_string = data_set.readline().replace("\n","")
    mrna_len = len(mrna_string)
    index = 0
    protein_string = ""


    while index < mrna_len:
        
        next_codon = index + 3 #mrna_len
        
        codon = mrna_string[index:next_codon]
        # print(index)
        # print(next_codon)
        # print("\n")
        if codon_to_amino_acid[codon] == "Stop":
            break
        protein_string = protein_string + codon_to_amino_acid[codon]
        index = next_codon


    print(protein_string)



    pass

dataset_name = sys.argv[1]
with open(dataset_name, "r") as data_set:
    main(data_set=data_set)
