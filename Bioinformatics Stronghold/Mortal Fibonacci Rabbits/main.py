
import re
import sys
from collections import defaultdict, Counter
import math
from io import TextIOWrapper
import textwrap


'''
Note:
    This is rather slow, we have to loop over all of the elements in the adult rabbit list to sum them to 
    determine the number of offspring.
'''
def main(data_set:TextIOWrapper):
    trial_months, lifespan_months = list(map(int, data_set.readline().split(" ")))    
    months_living = [1] # Index corresponds to the month, value corresponds to number of rabbits alive for index months
    
    for month in range(0, trial_months - 1):
        print(months_living)
        if len(months_living) == 1:
            months_living.insert(0,0)
        else: 
            months_living.insert(0, sum(months_living[1:]))
            if len(months_living ) > lifespan_months: # Get rid of the dead rabbits
                months_living.pop()
    
    print(months_living)
    print(sum(months_living))
          

dataset_name = sys.argv[1]

with open(dataset_name, "r") as data_set:
    main(data_set=data_set)
# main(data_set="RA")



