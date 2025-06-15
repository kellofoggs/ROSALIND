
from typing import Dict, List, Set, Union
# A class for opening and interpreting fasta files, I got tired of rewriting the same function
from io import TextIOWrapper
import re

class Fasta:
    pass


    @staticmethod
    def get_fasta_as_dict(fasta: Union[TextIOWrapper, str]) -> Dict:   
        if type(fasta) == TextIOWrapper:
            fasta_string = fasta.read()
        elif type(fasta) == str:
            fasta_string = fasta
        matches_list = re.split(">(.*)", fasta_string)[1:] # Skip the blankspace match

        sequence_label = matches_list[::2]
        sequence_list = list(map(lambda sequence: sequence.replace("\n",""), matches_list[1::2]))
        id_to_sequence_dict = dict(zip(sequence_label, sequence_list))

        return id_to_sequence_dict

    @staticmethod
    def get_fasta_as_list(fasta_file: Union[TextIOWrapper, str], fasta_string= None) -> Dict:   
        if fasta_string is not None:
            string = fasta_string
        else:
            if type(fasta_file) == TextIOWrapper:
                string = fasta_file.read()
            elif type(fasta_file) == str:
                with open(fasta_file) as f_file:
                    string = f_file.read()
        matches_list = re.split(">(.*)", string)[1:] # Skip the blankspace match

        
        sequence_list = list(map(lambda sequence: sequence.replace("\n",""), matches_list[1::2]))
        

        return sequence_list


