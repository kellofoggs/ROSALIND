import sys
from math import sqrt
from typing import List
from Utilities.InputFileTools import GenericTextFile

# R homogeneous recessive
# A heterogeneneous
# D homogeneous dom


# 1-R = D + A

# We're interested on calcing A

# A = 1-R-D

# D+A = dom alleles / 2population
# R = 1-(D+A) 



def main(probs_hom_recessive:List[float]):
    # We're given the frequency of a recessive homozygous individual "R"
    # This is the same thing as saying the probability of having two recessive genes (which is prob_having_one^2)
    # Therefore we can derive the probability of having a single recessive gene as sqrt(R)
    
    prob_at_least_one_rec = []
    for i in range(0, len(probs_hom_recessive)):
        p_both_rec = probs_hom_recessive[i] # rr
        
        p_recessive = sqrt(p_both_rec) # Frequency of recessive allele

        p_dominant = 1 - p_recessive# 1 - p_rec

        prob_at_least_one_rec.append(str(round(2*p_recessive*p_dominant + p_both_rec,3
        )))
        ''' 
            2*p_recessive*p_dominant -> for P(Rr) + P(rR)
            p_both_rec -> for P(rr)
            Those are all the cases where there is at least one recessive allele
            Alternatively we could to 1 - P(RR)

        '''
    print(" ".join(prob_at_least_one_rec))


file_name = sys.argv[1]
list_of_hom_rec_rates = list(map(float,GenericTextFile.get_generic_file_as_lines(file_name)[0].split()))
main(list_of_hom_rec_rates)