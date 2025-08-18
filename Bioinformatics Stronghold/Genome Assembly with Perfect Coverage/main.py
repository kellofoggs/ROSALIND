from Utilities.Graphs import DebruijnGraph
from Utilities.DNA import StringTools
from typing import List, Dict, Tuple
import sys
from Utilities.InputFileTools import GenericTextFile
'''

Refresher:

    A read is a section of a genome, we can also call it a k-mer
Motivation:
    * So far we've looked at linear chromosomes (the type found in eukaryotes (organisms who once in development/life had a well define nucleus) )
    * However some organisms like the majority of bacteria have circular chromosomes

New terms:
    Perfect coverage - When we have a read that starts at every possible location in the geonme
'''


'''
Given kmers from a circular chromosome, where each k-mer from the chromosome is present. The de bruijn graph has only one simple cycle


Ideas:
    1.) create a debruijn graph for the set of k-mers (not union with its reverse complement), do a walk through this graph: 
        for each source-destination pair: We'll find the simple cycle, the last k nodes on this walk should be found at the beginning of the output string
        as we have error free reads. 

'''
def main(kmer_plus_one_list):


    debruijn_adjacency_dict:Dict = DebruijnGraph.generate_de_bruijn_graph(kmer_plus_one_list, is_adjacency_map=True)
    # print(debruijn_adjacency_dict)
    debruijn_nodes = list(debruijn_adjacency_dict.keys())
    start_node = debruijn_nodes[0]

    visited = set()
    to_visit = [start_node]
    output_string = ""

    kmer_length = len(debruijn_nodes[0])
    while len(to_visit) > 0:
        current = to_visit.pop(0)


        for neighbor in debruijn_adjacency_dict[current]:
            if neighbor not in visited:
                to_visit.append(neighbor)
        
        output_string = StringTools.combine_strings(output_string, current)
        visited.add(current)
    
    # print(output_string)
    return output_string[:-(kmer_length-1)]
        
file_path = sys.argv[1]

k_mers_list = GenericTextFile.get_generic_file_as_lines(file_path)

output = main(k_mers_list)
print(output)    


# ATTAC
# ATTACA
# ATTACAG
# ATTACAGATT