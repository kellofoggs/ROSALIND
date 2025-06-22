from typing import List, Dict, Set 

class Node: 
    children:Set # A set of nodes that are the children of the node
    content:str = None
    
    def __init__(self, content):
        self.content = content
        self.children = set()
        
        pass

    def add_children(self, children: List):
        for child in children:
            self.children.add(child)

    


        

class Trie:

    '''A class used for tries. This was created for solving
    Introduction to Pattern Mathcing
    The exercise in question just asks for printing out a walk of a trie where the edges
    are symbols in the string and the nodes are states. However I am using this trie to have the nodes be symbols
    This accomplishes the same functionality with a trie as a node cannot have more than one ancestor.
    This means that following the node with symbol x will be the same as jumping to the node with symbol x from the current node



    I chose this method as I think I'll probably have to revisit other trie/graph style problems eventually and
    I personally think edge list is one of the worst ways to represent any sort of graph

       '''
    root_node:Node = None
    node_order_dict:Dict = None # A dictionary where the key is the object, the value is the order of when it was added into the dict

    '''Make a Trie where each edge node other than the is a '''
    def __init__(self, input_strings):
        self.root_node = Node(None)
        self.node_order_dict = dict()
        self.node_order_dict[self.root_node] = 1
        self.create_trie_from_strings(input_strings)
        pass

    def create_trie_from_strings(self, input_strings:List[str]):
        for string in input_strings:
            self.add_string_to_graph(string)
            

    def add_string_to_graph(self, string):
        pass
        curr_node = self.root_node
        for char in string:
            child_nodes:Set[Node] = curr_node.children
            child_is_found = False
            for child in child_nodes:
                # Search child nodes for 
                if child.content == char:
                    curr_node = child
                    child_is_found = True
                    break
            # If we don't find the expected node, then create it
            if not child_is_found:
                new_child = Node(char)
                curr_node.add_children([new_child])
                curr_node = new_child
                self.node_order_dict[curr_node] = len(self.node_order_dict) + 1

        pass

        
        # 

    def depth_first_print(self):
        # start off at the root node
        
        to_visit_stack = [self.root_node] 
        visited = set()
        # to_visit_stack.append()



        while len(to_visit_stack) > 0:
            
            current:Node = to_visit_stack.pop()
            if current not in visited:
                visited.add(current)
                parent_num = self.node_order_dict[current]

                for child in current.children:
                    child_node_num = self.node_order_dict[child]
                    edge_label = child.content
                    print(f"{parent_num} {child_node_num} {edge_label}")
                    to_visit_stack.append(child)
                # to_visit_stack.extend(list(current.children))


            
            






        
        pass

    def dfs_wrapper(self, query_string):
        '''
        @param: query_string: The string that you're searching for in the trie
        @return: Return what part of the string was found in the tree (i.e.) the path taken to it
        '''
        # See how far u 

    def breadth_first_search(self, query_string):
        # For constructing a trie it's probably best to use bfs
        query_arr = list(query_string)
        discovered = set() # A discovered set is not needed as we know that the graph is a tree (no cycles possible)
        start_vertex  = self.root_node #query_arr.pop(0) 
        to_visit = start_vertex.children
        



    def add_node(self, path_to_start:str, ):
        pass

    def add_node(self, parent_node:Node, child_node_name):
        child_node = Node(content=child_node_name)
        parent_node.add_children([child_node])
    
        
        

    
