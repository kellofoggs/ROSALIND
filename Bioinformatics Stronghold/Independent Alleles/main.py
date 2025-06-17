from math import comb

# Tom has Aa Bb
# Tom mates with someone with Aa Bb and has 2 children
# each of Tom's children have 2 children and breed with an Aa Bb genotype partner


# Params: k N
# k is the last generation of tom's family
# P(N or more individuals have Aa Bb)

# We assume that a gene and b gene are independent of one another

# Tom's first offspring: 

# We want to calculate the expected number of Aa Bb offspring

## 4/16 chance of producing Aa Bb offspring by mating Aa Bb with Aa Bb This is the same thing as .25

# We've only got 2 possible outcomes, either it's AaBb child or it's not so we can use the binomial distribution 
prob_both_hetero = 4/16
prob_not_both_hetero = 1 - prob_both_hetero

num_gens = 6
num_both_genotype_hetero = 18
total_population = 2**num_gens # We start off with 1 person (2^0), Each generation each child has 2 children so we multiply our offspring by 2 afterwards  with the genotype,

output = 0
for i in range(num_both_genotype_hetero,total_population+1 ):
    output = output + comb(total_population, i) * ((prob_both_hetero**i) *(prob_not_both_hetero **(total_population - i)))

print(round(output, 3))