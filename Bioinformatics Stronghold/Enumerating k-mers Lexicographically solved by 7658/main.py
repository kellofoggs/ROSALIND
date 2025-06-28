from typing import List
import sys
from Utilities.InputFileTools import GenericTextFile
from Utilities.EnumerationTools import Enumerations





    

def main(alphabet_string:str, string_length:int):
    lexographic_strings = Enumerations.fast_lex_words(alphabet_string, string_length)
    for word in lexographic_strings:
        print(word)

file_lines = GenericTextFile.get_generic_file_as_lines(file=sys.argv[1])

print(file_lines[0])
main(alphabet_string=file_lines[0].split(), string_length=int(file_lines[1]))
