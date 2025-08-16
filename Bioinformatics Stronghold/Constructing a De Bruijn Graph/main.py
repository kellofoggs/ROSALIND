from Utilities.InputFileTools import GenericTextFile
from Utilities.DNA import StringTools
from typing import List, Tuple
from collections import defaultdict
import sys
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








def generate_de_bruijn_graph(k_plus_1_mer_list:List[str], is_adjacency_map:bool=False) -> List[Tuple[str, str]]:
    '''
    Function that generates a debruijn graph given a list of (k+1)-mers in two formats:
        Adjacency map
        Edge list
    This is set by the optional parameter is_adjacency_map which is a boolean, by default it is set to return
    an edge list. Set to true to return an adjacency map. 
    '''
    k = len(k_plus_1_mer_list[0]) -1 
    
    if not is_adjacency_map:

        debruijn_edges:List[Tuple[str, str]] = []
        for k_plus_1_mer in k_plus_1_mer_list:
            edge_tuple = (k_plus_1_mer[:k], k_plus_1_mer[1:])
            debruijn_edges.append(edge_tuple)
        return(debruijn_edges)
    
    else:
        adjacency_map = defaultdict(list)
        for k_plus_1_mer in k_plus_1_mer_list:
            adjacency_map[k_plus_1_mer[:k]] = k_plus_1_mer[1:]
        return adjacency_map



def main(k_plus_1_mer_list: List[str]):

    k_plus_1_mer_rev_comp_list = list(map(StringTools.reverse_complement_dna, k_plus_1_mer_list))
    source_union_rev_comp_list = list(set(k_plus_1_mer_rev_comp_list).union(set(k_plus_1_mer_list)))
    debruijn_edge_list =  generate_de_bruijn_graph(source_union_rev_comp_list)

    for edge in debruijn_edge_list:
        print(f"({edge[0]}, {edge[1]})")
        pass

    pass

file_path = sys.argv[1]

k_plus_1_mer_list = GenericTextFile.get_generic_file_as_lines(file_path)
main(k_plus_1_mer_list)