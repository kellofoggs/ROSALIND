from Utilities.InputFileTools import GenericTextFile
from typing import List
import sys

'''
Given a sample populatoin N
and a list of allele frequencies, where each frequency is a float within the following range: [0, 1]
Calculate the expected number of occurences of the alleles

These assume a binomial distribution where the probability of success is the observed allele frequencies

If you have taken an intro stats class you know the binomial distribution Expected value for success class is the sample size * success probability 
This eliminates the need to actually do the ncr * p^s(1-p)^(n-s) calculations, and allows us to do the calcs in linear time.
'''



def main(sample_size:int, frequency_list:List[float]):

    expected_list = map(lambda x: str(
        round((x * sample_size), 3)
        ) ,frequency_list)
    print(" ".join(expected_list))


file_path = sys.argv[1]
file = GenericTextFile.get_generic_file_as_lines(file_path)
sample_size = int(file[0].strip())
frequency_list = map(float, file[1].strip().split())

main(sample_size, frequency_list)