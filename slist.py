# Node class to represent each element in the linked list
class Node:
    def __init__(self, value):
        self.data = value     # stores the value of the node
        self.next = None      # pointer to the next node (initially None)

# Singly linked list class
class slist:
    def __init__(self):
        self.head = None   # initially the list is empty, so head is None
        self.n = 0         # keeps track of the number of nodes in the list

    def __len__(self):
        # returns the number of elements (nodes) in the list
        return self.n
    
    # Insert at the beginning (head) of the linked list
    def insert_head(self, value):
        new_node = Node(value)       # create a new node
        new_node.next = self.head    # new node points to the old head
        self.head = new_node         # update head to new node
        self.n += 1                  # increase node count
    
    # Insert at the end (tail) of the linked list
    def insert_tail(self, value):
        new_node = Node(value)       # create a new node
        if self.head == None:        # if list is empty
            self.head = new_node     # new node becomes head
            self.n += 1
            return
        curr = self.head             # start from head
        while curr.next != None:     # traverse until last node
            curr = curr.next
        curr.next = new_node         # link last node to new node
        self.n += 1
    
    # Insert a new node after a given value
    def insert_after(self, after, value):
        new_node = Node(value)       # create new node
        curr = self.head
        while curr != None:          # traverse the list
            if curr.data == after:   # stop when the target value is found
                break
            curr = curr.next
        if curr != None:             # if found
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
        else:                        # if not found
            return 'item not found'
    
    # String representation of the linked list (used in print)
    def __str__(self):
        curr = self.head
        result = ''
        while curr != None:          # traverse until end
            result = result + str(curr.data) + '->'
            curr = curr.next
        return result[:-2]           # remove last '->' for clean output
    
    # Get item at a particular index (like list[index])
    def __getitem__(self, index):
        curr = self.head
        poss = 0                     # position counter
        while curr != None:          # traverse the list
            if poss == index:        # when position matches index
                return curr.data
            curr = curr.next
            poss += 1
        return 'IndexError'          # if index out of range
    
    # Insert at a specific index (0-based)
    def insert_at(self, ind, value):
        new_node = Node(value)
        curr = self.head
        count = 0
        while curr != None:
            if count == ind-1:       # stop at node before target position
                break
            count += 1
            curr = curr.next
        if curr != None:             # if position found
            new_node.next = curr.next
            curr.next = new_node
            self.n += 1
        else:
            return 'index not found'

#Testing:
L = slist()              # create an empty linked list
L.insert_head(20)       
L.insert_head(30)        
L.insert_head(40)        
L.insert_head(50)       
L.insert_tail(10)        
L.insert_tail(1)        
L.insert_at(2, 70)      
print(L)                 # prints the linked list
print(L[2])              # prints the element at index 2 (70)
