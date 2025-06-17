import sys

def main(dataset_name:str):
    with open(dataset_name, "r") as data_set:
        dna_string ="".join(data_set.readlines())
        output = dna_string.replace('T', "U")
        print(output)
        with open("./output", 'w') as output_file:
            output_file.write(output)
    

main(dataset_name= sys.argv[1])