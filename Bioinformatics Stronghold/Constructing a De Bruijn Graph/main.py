from Utilities.InputFileTools import GenericTextFile
from Utilities.DNA import DNAStringTools
from typing import List, Tuple
from collections import defaultdict
import sys
from Utilities.Graphs import DebruijnGraph
'''
Light recap: 
    * kmer is a substring of length k
    * (k+1) mer is substring of length k+1 

New stuff:
    Given that we have:
        * a set S of (k+1 )-mers
        * set S^(rc) which is all reverse complements of S 
    De bruijn graph is a directed graph has 
        Nodes: 
            * all kmers that are present in the k-mers from the union of S and S^(rc)
        Edges:
            * [the first element to the k element in our (k+1)-mer, the second element to the end of our (k+1)-mer]
'''









def main(k_plus_1_mer_list: List[str]):

    k_plus_1_mer_rev_comp_list = list(map(DNAStringTools.reverse_complement_dna, k_plus_1_mer_list))
    source_union_rev_comp_list = list(set(k_plus_1_mer_rev_comp_list).union(set(k_plus_1_mer_list)))
    debruijn_edge_list =  DebruijnGraph.generate_de_bruijn_graph(source_union_rev_comp_list)

    for edge in debruijn_edge_list:
        print(f"({edge[0]}, {edge[1]})")
        pass

    pass

file_path = sys.argv[1]

k_plus_1_mer_list = GenericTextFile.get_generic_file_as_lines(file_path)
main(k_plus_1_mer_list)