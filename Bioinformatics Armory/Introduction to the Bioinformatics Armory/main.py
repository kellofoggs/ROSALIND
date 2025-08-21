from Bio.Seq import Seq
from Utilities.InputFileTools import GenericTextFile
from Utilities.DNA import DNAStringTools
from Utilities.Solution import BaseSolution
import sys
import argparse


class Solution(BaseSolution):
    def __init__(self):
        super().__init__()
        
    def solve(self):
        dna_string = "".join(self.get_generic_input_file())
        count_dict = DNAStringTools.count_nucleoutides(dna_string)
        nucs = ["A", "C", "G", "T"]

        nuc_counts = list(map(lambda nuc: str(count_dict.get(nuc)), nucs ))
        print(" ".join(nuc_counts))
        
        pass

def main():

    my_solution = Solution()
    my_solution.solve()


main()