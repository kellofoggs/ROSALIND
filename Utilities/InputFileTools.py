
from typing import Dict, List, Set, Union
# A class for opening and interpreting fasta files, I got tired of rewriting the same function
from io import TextIOWrapper
import re

class Fasta:
    '''
    Class for handling the fasta format, can use either a raw fasta string or a file handle as input or the file's path
    '''
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
    def get_fasta_as_list(fasta_file: Union[TextIOWrapper, str]= None, fasta_string= None) -> Dict:   
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


class GenericTextFile:
    '''
    Used to convert fasta file into different formats, pass in the file path or file handle
    '''
    @staticmethod
    def get_generic_file_as_lines(file: Union[str, TextIOWrapper]) -> List[str]:
        if type(file) == str:
            with open(file) as text_file:
                return text_file.read().splitlines()
        elif type(file) == TextIOWrapper:
            return file.read().splitlines()
            pass
        else:
            raise Exception("Either pass in the fast file as a string that is it's file path or a TextIOWrapper object")
    
    @staticmethod 
    def get_generic_file_as_str(file: Union[str, TextIOWrapper]) -> str:
            if type(file) == str:
                with open(file) as text_file:
                    return text_file.read()
            elif type(file) == TextIOWrapper:
                return file.read()
            else:
                raise Exception("Either pass in the fast file as a string that is it's file path or a TextIOWrapper object")
    