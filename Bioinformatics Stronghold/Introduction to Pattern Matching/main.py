from Utilities.InputFileTools import GenericTextFile
from Utilities.Graphs import Trie
from typing import List
import sys

# GenericTextFile.get_generic_file_as_lines()


def main(input_strings:List[str]):
    string_trie = Trie(input_strings)
    string_trie.depth_first_print()

input_file_path = sys.argv[1]

input_strings = GenericTextFile.get_generic_file_as_lines(input_file_path)
input_strings = ["ATAGA",
"ATC",
"GAT"
]
main(input_strings)


# yours = set(["1 2 A",
# "2 3 T",
# "3 4 A",
# "4 5 G",
# "5 6 A",
# "3 7 C",
# "1 8 G",
# "8 9 A",
# "9 10 T",]
# )


# mine = set(["1 2 A",
# "1 7 A"  ,
# "1 10 G" ,
# "10 11 A",
# "11 12 T",
# "7 8 T",
# "8 9 C",
# "2 3 T",
# "3 4 A",
# "4 5 G",
# "5 6 A",])

# print(mine-yours)