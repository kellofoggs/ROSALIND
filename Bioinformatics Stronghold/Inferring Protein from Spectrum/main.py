from Utilities.MassSpectrometry import Spectrometry
from Utilities.InputFileTools import GenericTextFile
from decimal import Decimal
from typing import List
import sys
'''
Concept:
For a rough estimation of the amino acids that make up a protein (and by extension the type of protein created),
we can look at the prefix or suffix spectrum of a weighted string. 
A prefix spectrum of a protein ABC is the proper prefixes (i.e. no whole string):
A, AB.

As we've only added one amino acid from A to AB, the difference of the two masses should be extremely close to the
the weight of B. 

We can deduce the identity of the amino acid at B by looking at an amino acid isotopic mass table (this table has the most weight of the most common isotope
, which is different in mass by number of neutrons as electron mass is negligible )

Certain amino acids such as leucine and isoleucines are isomers ( same chemical formulas, but different shape) so spectrometry cannot properly distinguish between the two
'''

prefix_mass_list = [3524.8542,
3710.9335,
3841.974,
3970.0326,
4057.0646]
file_name = sys.argv[1]
prefix_mass_list = list(map(float,GenericTextFile.get_generic_file_as_lines(file_name)))

def main(prefix_mass_list:List[float]):

    amino_acid_mass_list = []
    for i in range(1, len(prefix_mass_list)):
        # print(prefix_mass_list[i])
        amino_acid_mass_list.append(round(prefix_mass_list[i]-prefix_mass_list[i-1], 4))
        
    # print(amino_acid_mass_list)

    print("".join(list(map(Spectrometry.get_amino_acid_from_mass, amino_acid_mass_list))))

main(prefix_mass_list)