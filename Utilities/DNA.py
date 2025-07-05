from typing import Dict, Set, List, Tuple
from decimal import Decimal
from collections import defaultdict, Counter

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

    @staticmethod
    def count_nucleoutides(dna_string:str):
        return Counter(dna_string)

class ProbabilityTools:

    @staticmethod
    def caclulate_dna_probability(gc_content:float, dna_string:str):
        '''Calculate the probability of the dna string occuring given GC content'''
        
        nuc_counts = StringTools.count_nucleoutides(dna_string)

        

        prob_dict = ProbabilityTools.calculate_nuc_probs_from_GC(gc_content)
        out_prob = 1
        A = nuc_counts["A"]
        T = nuc_counts["T"]
        G = nuc_counts["G"]
        C = nuc_counts["C"]
        return (prob_dict.get("A")**(A+T)) * (prob_dict.get("G")**(C+G))
        # for char in dna_string:
        #     prob = prob_dict.get(char)
        #     if prob is None and type(prob) not in {float,Decimal}:
        #         raise IOError("The dna string contains non-dna characters")
        #     else: # I know the else isn't necessary it's for readability
        #         out_prob = out_prob * prob

        return out_prob
        pass

    @staticmethod
    def calculate_nuc_probs_from_GC(gc_content:float) -> Dict[str, float]:
        '''
        Calculate the probability of each nucleotide occuring based on the GC content.
        @param: gc_content: percentage/float that represents the amount of the string that is either guanine or cytosine
        @return: A dictionary where 
             Each key is the letter that represents the nucleotide in {A,T,G,C} 
             Each value is the float that represents the probability of the nucleotide occuring
        '''

        prob_guanine = prob_cytosine = gc_content/2
        prob_adenine = prob_thymine = (1-gc_content)/2
        return {
            "A": prob_adenine,
            "T": prob_thymine,
            "G": prob_guanine,
            "C": prob_cytosine

        }
        
