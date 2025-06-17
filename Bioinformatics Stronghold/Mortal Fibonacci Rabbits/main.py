
import re
import sys
from collections import defaultdict, Counter
import math
from io import TextIOWrapper
import textwrap

# Perfect place for linkedlist, we're only going to push and pop
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head:Node = None
        self._size:int = 0

    def size(self):
        return self._size
    

    def append(self, data):
        """Add a node to the end of the list."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        self._size = self._size + 1

    def prepend(self, data):
        """Add a node at the beginning of the list."""
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self._size = self._size + 1

    def delete(self, key):
        """Delete the first node with the given data."""
        current = self.head

        if current and current.data == key:
            self.head = current.next
            return

        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if current:
            prev.next = current.next
            self._size = self._size - 1

    def delete_at_index(self, index):
        """Delete node at a specific index (0-based)."""
        if index < 0:
            print("Invalid index.")
            return

        current = self.head

        if index == 0:
            if current:
                self.head = current.next
            return

        prev = None
        count = 0
        while current and count < index:
            prev = current
            current = current.next
            count += 1

        if current:
            prev.next = current.next
            self._size = self._size - 1
        else:
            print("Index out of range.")


    def find(self, key):
        """Search for a node with the given data."""
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def display(self):
        """Print all elements in the list."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        print("LinkedList:", elements)


'''
Note:
    This is rather slow, we have to loop over all of the elements in the adult rabbit list to sum them to 
    determine the number of offspring.
'''
def main(data_set:TextIOWrapper):
    trial_months, lifespan_months = list(map(int, data_set.readline().split(" ")))    
    # trial_months = 6
    # lifespan_months = 3
    # trial_months = 96
    # lifespan_months = 17
 
    # number_of_months, offspring_per_pair = list(map(int, data_set.readline().split(" ")))    
    
    months_living = [1] # Index corresponds to the month, value corresponds to number of rabbits alive for index months
    
    for month in range(0, trial_months - 1):
        print(months_living)
        if len(months_living) == 1:
            months_living.insert(0,0)
        else: 
            months_living.insert(0, sum(months_living[1:]))
            if len(months_living ) > lifespan_months: # Get rid of the dead rabbits
                months_living.pop()
    
    print(months_living)
    print(sum(months_living))
    # print(months_living[:lifespan_months-1])
    # print(sum(months_living[:lifespan_months-1]))

    # print(sum(months_living[:lifespan_months]))
        
        
            

        
    


    # # number_of_months = 5
    # # offspring_per_pair = 3
    # growing_child_rabbits = 1 # this step here is useless but helps to document the steps of the scenario
    # adult_rabbits = 0



    # # Month 0, take the child rabits and make them grow into adult rabbits
    # newborn_rabbits = 0
    # growing_child_rabbits = 0
    # adult_rabbits = 1
    


    # for month in range(0,number_of_months - 1):
    #     newborn_rabbits = adult_rabbits * offspring_per_pair
    #     adult_rabbits = adult_rabbits + growing_child_rabbits
    #     growing_child_rabbits = newborn_rabbits
        
        
    #     pass
    # pass
    # print(adult_rabbits)
    

dataset_name = sys.argv[1]

with open(dataset_name, "r") as data_set:
    main(data_set=data_set)
# main(data_set="RA")



