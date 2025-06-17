
import re
import sys
from collections import defaultdict, Counter
import math
from io import TextIOWrapper
import textwrap

def main(data_set:TextIOWrapper):

    number_of_months, offspring_per_pair = list(map(int, data_set.readline().split(" ")))    
    # number_of_months = 5
    # offspring_per_pair = 3
    growing_child_rabbits = 1 # this step here is useless but helps to document the steps of the scenario
    adult_rabbits = 0



    # Month 0, take the child rabits and make them grow into adult rabbits
    newborn_rabbits = 0
    growing_child_rabbits = 0
    adult_rabbits = 1
    
    for month in range(0,number_of_months - 1):
        newborn_rabbits = adult_rabbits * offspring_per_pair
        adult_rabbits = adult_rabbits + growing_child_rabbits
        growing_child_rabbits = newborn_rabbits
        
        
        pass
    pass
    print(adult_rabbits)
    

dataset_name = sys.argv[1]

with open(dataset_name, "r") as data_set:
    main(data_set=data_set)
# main(data_set="RA")