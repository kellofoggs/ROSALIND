from Utilities.EnumerationTools import Enumerations
from Utilities.InputFileTools import Fasta

import sys
import re

from collections import Counter

def count_overlapping_enums(text: str, enum_list: list[str]) -> dict[str, int]:
    enum_pattern = '|'.join(re.escape(word) for word in enum_list) 
    lookahead_pattern = f"(?=({enum_pattern}))"
    
    counter = Counter()
    for match in re.finditer(lookahead_pattern, text):
        word = match.group(1)
        counter[word] += 1
    return dict(counter)


file_path = sys.argv[1]
fasta_string = Fasta.get_fasta_as_list(file_path)[0]

def main( fasta_string):
    ordered_alphabet = ["A","C","G","T"]
    enum_len = 4
    lex_enums = Enumerations.fast_lex_words(ordered_alphabet, enum_len)
    enum_counts = count_overlapping_enums(fasta_string, lex_enums)
    
    for word in lex_enums:
        count = enum_counts.get(word) if enum_counts.get(word) is not None else 0
        print(count,end= ' ')

main(fasta_string)