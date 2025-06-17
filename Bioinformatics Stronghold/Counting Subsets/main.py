import sys

data_set_path = sys.argv[1]

def main(set_size):
    
    print(((2**set_size)% 1000000)) 
    pass


with open(data_set_path) as file:

    main(int(file.readline()))