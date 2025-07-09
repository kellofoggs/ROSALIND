from typing import List
from Utilities.InputFileTools import GenericTextFile
import sys
# Given: Array A where each element is the percent of males
#  with a recessive allele for an X-linked gene
# 
 


def main(probs_male_recessive_x:List[float]):
    
    '''
    Probability of male having recessive X linked trait is the same 
    as the probability of having one recessive allele


    Probability of female being carrier is P(Rr) + P(rR)

    P(R) = 1- r
    P(r) = r

    2(1-r)r is probability of being heterozygous female ( aka carrier for the recessive trait)
    '''
    output_list = []
    for p_male_rec_x_linked in probs_male_recessive_x:
        output_list.append(str(round(2*(1-p_male_rec_x_linked)*p_male_rec_x_linked, 3)))
    print(" ".join(output_list))



file_name = sys.argv[1]
input_list = list(map(float, GenericTextFile.get_generic_file_as_lines(file_name)[0].split()))
main(input_list)