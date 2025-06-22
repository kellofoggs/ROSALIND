from Utilities.InputFileTools import GenericTextFile
from Utilities.Trie import Trie
from typing import List
import sys

# GenericTextFile.get_generic_file_as_lines()


def main(input_strings:List[str]):
    string_trie = Trie(input_strings)
    string_trie.depth_first_print()

input_file_path = sys.argv[1]

input_strings = GenericTextFile.get_generic_file_as_lines(input_file_path)
main(input_strings)
