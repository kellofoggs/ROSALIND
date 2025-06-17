# Protein motifs: amino acid pattern in a protein's domain that is of significance

""" Protein Motif shorthand:
    * [XY] means either amino acid X or Y
    * {X} means any amino acid except for X
    * X means the amino acid X
"""
from typing import List
import sys
from urllib import request

from re import finditer
protein_request_string_fasta = "http://www.uniprot.org/uniprot/%s.fasta"
protein_request_string = "http://www.uniprot.org/uniprot/%s"


def get_protein_text_file(protein_id:str) -> bytes:
    '''
    Return the protein text file contents as a binary string
    '''

    #  It seems like a lot of the old protein IDs have been changed.
    #  Many species share proteins, so it makes ssense to not always included the species the protein came from in the ID
    # This gets around that issue, the only problem is rechecking by firing a second network request is quite slow
    # In a perfect world where I was guaranteed the schema of ids have changed for all proteins I would simply split on the underscore
    # For every id instead of doing a retry
    try:
        with request.urlopen(protein_request_string_fasta % (protein_id)) as response:
            output = response.read()
            return output
    except Exception:
        protein_id = protein_id.split("_")[0]
        with request.urlopen(protein_request_string_fasta % (protein_id)) as response:
            output = response.read()
            return output

    
def parse_protein_text_file(protein_file:bytes) -> str:
    '''
    Return locations in protein string where N-glycosylation motif is found
    If it is not found anywhere, return None
    '''

    
    
    # The first line in the fasta file format is a header that contains the sequence ID and some other optional info
    # We can skip this line when parsing
    sequence_string = b"".join(protein_file.splitlines()[1:])
    # N-glycosylation motif is written as N{P}[ST]{P}
    # This means the motif starts with N, is followed by any amino acid other than P, 
    # then followed by either S or T, and followed by any amino acid other than P 
    N_glycol_pattern = b"(?=(N[^P][ST][^P]))"
    match_locations = list(map(lambda zero_index: str((zero_index+1)),[match.start() for match in finditer(N_glycol_pattern, sequence_string)]))
    if match_locations:
        output = " ".join(match_locations)
        return output
    else:
        return None


    pass
def main(id_list:List):
    # id_list = ["A2Z669", "B5ZC00", "P07204_TRBM_HUMAN", "P20840_SAG1_YEAST"]
    for protein_id in id_list:
        n_glycols = parse_protein_text_file(get_protein_text_file(protein_id))

        if n_glycols is not None:
            output_string = f"{protein_id}\n{n_glycols}"
            print(output_string)

dataset_name = sys.argv[1]

with open(dataset_name, "r") as data_set:
    main(id_list=data_set.read().splitlines())
