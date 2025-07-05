from math import comb

class Distributions:

    @staticmethod
    def binomial_pmf(num_trials:int, num_success:int,prob_succ:float):
        '''
        Returns the probability that the target number of successes occurs, given a number of samples and a probability of success
        per trial
        vars:
            num_trials: number of trials within our experiment
            num_success: The number of times of the Succes event occurs
            prob_succ: The probability of True/Success event in one trial
        
        Made because I'm tired of rewriting the same function in different files

        '''
        return comb(num_trials, num_success) * ((prob_succ)**num_success) * ((1-prob_succ)**(num_trials-num_success))
    @staticmethod
    def binomial_cdf(num_trials: int, num_success:int, prob_success: float, or_equal_to:bool = True, greater_than:bool= True):



        '''Return the probability that an event occurs less '''
        pass