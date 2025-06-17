from typing import Dict, Set, List
class StringTools:



    '''
    Class with static methods used for handling common DNA tasks such as 
    converting DNA codons to amino acids and reverse complementing dna
    
    Also 
    '''

    dna_nuc_complement_trans = str.maketrans({"A": "T", "T": "A", "G": "C", "C":"G"})
    codon_table_string = '''TTT F      CTT L      ATT I      GTT V
TTC F      CTC L      ATC I      GTC V
TTA L      CTA L      ATA I      GTA V
TTG L      CTG L      ATG M      GTG V
TCT S      CCT P      ACT T      GCT A
TCC S      CCC P      ACC T      GCC A
TCA S      CCA P      ACA T      GCA A
TCG S      CCG P      ACG T      GCG A
TAT Y      CAT H      AAT N      GAT D
TAC Y      CAC H      AAC N      GAC D
TAA Stop   CAA Q      AAA K      GAA E
TAG Stop   CAG Q      AAG K      GAG E
TGT C      CGT R      AGT S      GGT G
TGC C      CGC R      AGC S      GGC G
TGA Stop   CGA R      AGA R      GGA G
TGG W      CGG R      AGG R      GGG G 
'''


    dna_codon_to_amino_acid = dict(zip(*[iter(codon_table_string.split())] * 2)) # Convert our string into a dictionary of dna to codon translations
    stop_codons = set(["TAA", "TAG", "TGA"])
    start_codons = set(["ATG"]) # "ATG" aka methionine is the most commonly seen start codon although others do exist. For the purposes of this we will assume


    @staticmethod
    def reverse_dna(dna_string:str):
        return dna_string[::-1]
    @staticmethod
    def complement_dna(dna_string:str):
        return dna_string.translate(StringTools.dna_nuc_complement_trans)
        pass

    @staticmethod
    def reverse_complement_dna(dna_string):
        return StringTools.reverse_dna(StringTools.complement_dna(dna_string))
    
    @staticmethod
    def translate_dna_to_amino_acid(dna_string:str):
        output = ""
        for i in range(0, (len(dna_string)//3)):
            codon = dna_string[3*i: 3*i + 3]
            if codon not in StringTools.stop_codons:
                output = output + StringTools.dna_codon_to_amino_acid[codon] 
            else:
                break
        return output   

    @staticmethod
    def to_RNA(dna_strand:str) -> str:
        '''
        Convert a DNA strand string to an RNA strand string by replacing T with U
        '''
        return dna_strand.replace("T", "U")


