from math import factorial, pow
from typing import List
num_integers = 3

num_perumtations = factorial(num_integers)

ancestor_array = list(range(1, num_integers+1))
print(ancestor_array) 


# We can do this problem recursively


# def swap(s_list, swap_index_1, swap_index_two):
#     ''' Swap index in place, this changes the array from the scope outside of this function'''

#     temp = s_list[swap_index_1]
#     s_list[swap_index_1] = s_list[swap_index_two]
#     s_list[swap_index_two] = temp

#     pass

# # Recrusively find all permutations
# def _find_permutations(output_buffer:List, input_array, index):
#     pass

# def find_permutations(input_array):




# my = [1,2,3]

# print(my)

# swap(my, 0,1)
# print(my)

# Function to swap elements in the array
def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

# Function to find the possible permutations. 
# Initial value of idx is 0.
def permutations(res:List, arr, idx):
  
    # Base case: if idx reaches the size of the array,
    # add the permutation to the result
    if idx == len(arr):
        res.append(arr[:])
        return

    # Permutations made by swapping each element
    for i in range(idx, len(arr)):
        swap(arr, idx, i)
        permutations(res, arr, idx + 1)
        swap(arr, idx, i)  # Backtracking

# Function to get the permutations
def permute(arr):
    res = []
    permutations(res, arr, 0)
    return res

# Driver code
arr = [1, 2, 3,4,5,6,7]
res = permute(arr)
print(len(res))
# Printing result
for perm in res:
    print(" ".join(map(str, perm)))

