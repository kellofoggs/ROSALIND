""""""

import re
import sys
from collections import defaultdict, Counter
import math
def main(dataset_name:str):

    '''
    Given: Three positive integers k m and n representing a population 
    containing k+m+n organisms: k individuals are homozygous dominant for a factor, m
    are heterozygous, and n are homozygous recessive.

    Return: The probability that two randomly selected mating organisms will produce an individual 
    possessing a dominant allele (and thus displaying the dominant phenotype). Assume that any two
    organisms can mate.

    In mendelian inheritance a dominant trait occurs in offspring when either parent carries the trait.
    This happens when either (inclusive) parent is homogeneous dominant or (inclusive) hetereogeneous

    Therefore we're looking for P(either parent is homogenous dom or heterogeneous)

    '''

    
    with open(dataset_name, "r") as data_set:

        input_line = data_set.readline().split(" ")

        # hom_dom, heter, hom_rec = list(map(int, re.split("\s+", data_set.readline())))
    
        hom_dom = int(input_line[0])
        heter = int(input_line[1])
        hom_rec =int(input_line[2])

        total_individuals = hom_dom + heter + hom_rec

        '''Probability of having a dominant allele is 1 - probability of child being homogenous recessive
        First find probabilities of all potential pairings that can potentially result in homogeneous recessive child
        No homogeneous dominant cases are counted here as it guarantees that every child will have at least one copy of the dominant gene
        '''
        # Both hom rec parents
        p_hom_rec_parents = (hom_rec/total_individuals)*((hom_rec-1) /( total_individuals-1))


        # both heterogeneous parents
        p_heter_parents = (heter/total_individuals)*((heter-1)/(total_individuals-1))

        # One heterogeneous parent, one homogeneous recessive. The 2 allows us to also represent when the order of parent categories are different
        p_heter_hom_rec_parents = 2*(hom_rec/total_individuals)*(heter/(total_individuals-1))
        # print(p_heter_hom_rec_parents)

        # print((hom_rec/total_individuals)*(heter/(total_individuals-1)) + (heter/total_individuals)*(hom_rec/(total_individuals-1)))
        # Multiply the possibility of the pairings occuring with the possibility of the pairings producing homogeneous recessive children

        p_h_rec_hom_rec_parents = 1* p_hom_rec_parents

        hom_rec_child_heter_and_hom_rec_parents = 0.5* p_heter_hom_rec_parents

        p_h_rec_heter_parents = 0.25* p_heter_parents


        p_rec_hom_child = p_h_rec_hom_rec_parents + hom_rec_child_heter_and_hom_rec_parents+ p_h_rec_heter_parents
        # print(p_rec_hom_child)
        print(1-p_rec_hom_child)




        
main(dataset_name= sys.argv[1])