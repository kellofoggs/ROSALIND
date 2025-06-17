import sys

def main(dataset_name:str):
    with open(dataset_name, "r") as data_set:
        dna_string ="".join(data_set.readlines())

        # Complement of one strand of DNA string is the reverse of the string, with the partner nucleotide
        # A-> T, T-> A, G->C, C->G
        nucleotide_partners = str.maketrans({"A": "T", "T": "A", "G": "C", "C":"G"})
        output = dna_string.translate(nucleotide_partners)
        output = output[::-1]

        print(output)

        with open("./output", 'w') as output_file:
            output_file.write(output)
    

main(dataset_name= sys.argv[1])