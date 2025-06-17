import sys
from Utilities.InputFileTools import GenericTextFile
'''
1.) AA-AA 100% chance of having dominant phenotype
2.) AA-Aa 100% chance of having dominant phenotype
3.) AA-aa 100% chance of having dominant phenotype
4.) Aa-Aa 75% chance of each offspring having dominant phenotype
5.) Aa-aa 50% chance of each offspring having dominant phenotype
6.) aa-aa 0% chance of each offspring having dominant phenotype
'''
''' We want to know the expected number of offspring displaying the dominant phenotype, given that each couple has two children'''




def main(input_string:str):

    input_arr = list(map(int,input_string.strip().split()))
    # print(input_arr)
    expected = 0
    prob_list = [1,1,1,.75,.50,0]
    for i in range(0, len(input_arr)):
        expected = expected + (2 * input_arr[i]* prob_list[i])
        
        pass
    print(expected)

    pass



input_file_path = sys.argv[1]
main(input_string=GenericTextFile.get_generic_file_as_lines(input_file_path)[0])

# input_string = "1 0 0 1 0 1"
# main(input_string)