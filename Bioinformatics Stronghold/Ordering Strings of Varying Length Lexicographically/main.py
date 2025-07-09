from Utilities.EnumerationTools import Enumerations

my_enum = Enumerations.fast_lex_words(["D", "N", "A"], 3)
for elem in my_enum:
# for elem in sorted(my_enum):
    print(elem)