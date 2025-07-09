import re
# Oh my goodness, the notes on Rosalind are not the best way to understand the Newick tree format
# https://www.youtube.com/watch?v=KTZIYt8z9zQ explains way more concisely


# Comma means common ancestor
# Parentheses is a tree/subtree

# (dog, cat) would not touch, and would have a common ancestor. There are two edges in between them so there distance would 2

# (cat)dog would be distance 1 where dog is the ancestor of the cat group


# 

# Use two pointer approach



tree_string = "(dog,cat);"
dist_nodes = set("dog cat".strip().split())

tree_distance_chars = "(\(|\)|,)"
split_arr = [ele for ele in re.split(tree_distance_chars, tree_string) if ele] # Get rid of the empty string at the start of the array
print(split_arr)
distance = 0
left_index = 0
right_index = len(tree_distance_chars) -1 

found_entities = 0
arr_index = 0

while found_entities < 2:
    string = split_arr[arr_index]
    print(string)


    if found_entities == 0:
        if string in dist_nodes:
            found_entities += 1

    elif found_entities == 1:
        if string in {"(", ","}:
            distance += 1            
        if string in dist_nodes:
            distance += 1
            print(distance)
            break
        pass
        

    arr_index = arr_index+ 1
    pass



# Outer parnetheses is the largest part of the tree, each inner
# If two strings are in the same group they are distance one apart ( comma in same parenthese) If 
# First find where the two strings are in the array

