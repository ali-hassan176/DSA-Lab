# Class Node
class Node:
    def __init__(self, value):            # Constructor takes a value
        self.data = value                 # 'data' stores the actual value of the node
        self.next = None                  # 'next' points to the next node in the list
        self.prev = None                  # 'prev' points to the previous node in the list


# Class doubly limked list
class dlist:
    def __init__(self):                   # Constructor initializes an empty list
        self.head = None                  # 'head' points to the first node of the list
        self.tail = None                  # 'tail' points to the last node of the list
        self.n = 0                        # 'n' keeps track of the total number of nodes in the list

    def insert_head(self, value):
        new_node = Node(value)             # Create a new node with the given value
        if self.head is None:              # If the list is currently empty
            self.head = self.tail = new_node   # Both head and tail point to the new node
        else:                              # If the list is not empty
            new_node.next = self.head      # The new node’s next points to the current head
            self.head.prev = new_node      # The old head’s previous points back to the new node
            self.head = new_node           # Update head to be the new node
        self.n += 1                        # Increment the count of nodes

    def insert_tail(self, value):
        new_node = Node(value)             # Create a new node
        if self.tail is None:              # If the list is empty
            self.head = self.tail = new_node   # Head and tail both become this node
        else:                              # Otherwise, link it at the end
            self.tail.next = new_node      # Old tail’s next points to the new node
            new_node.prev = self.tail      # New node’s previous points to the old tail
            self.tail = new_node           # Update tail to the new node
        self.n += 1                        # Increment node count

    def traverse(self):
        temp = self.head                   # Start traversal from the head node
        print('[',end="")
        while temp:                        # Continue until temp becomes None (end of list)
            print(temp.data, end=" ")      # Print data of the current node
            temp = temp.next               # Move to the next node
        print(']')                            # Print a newline at the end

    def isempty(self):
        return self.head is None           # Returns True if there are no nodes, else False

    def len(self):
        return self.n                      # Simply return the counter of nodes

    def __getitem__(self, index):
        if index < 0 or index >= self.n:   # Check for invalid index
            raise IndexError("Index out of range")  # Raise an error if out of range
        temp = self.head                   # Start from the head
        for _ in range(index):             # Move index times to reach the target node
            temp = temp.next
        return temp.data                   # Return the data at the given index

    def delete_first(self):
        if self.head is None:              # If list is empty, nothing to delete
            return
        if self.head == self.tail:         # If there’s only one node
            self.head = self.tail = None   # Make both head and tail None (empty list)
        else:                              # If there are multiple nodes
            self.head = self.head.next     # Move head pointer to the second node
            self.head.prev = None          # New head’s previous should now be None
        self.n -= 1                        # Decrement node count

    def delete_last(self):
        if self.tail is None:              # If list is empty
            return
        if self.head == self.tail:         # If only one node
            self.head = self.tail = None   # Set both to None
        else:                              # Otherwise, adjust pointers
            self.tail = self.tail.prev     # Move tail pointer backward
            self.tail.next = None          # New tail’s next should be None
        self.n -= 1                        # Decrement node count

    def insert_at(self, index, value):
        if index < 0 or index > self.n:    # If index is invalid
            print("Index out of range")    # Print message and exit
            return
        if index == 0:                     # If inserting at start
            self.insert_head(value)        # Use existing insert_head method
            return
        elif index == self.n:              # If inserting at end
            self.insert_tail(value)        # Use existing insert_tail method
            return

        new_node = Node(value)             # Create the new node
        temp = self.head                   # Start from head
        for _ in range(index - 1):         # Move to node before the desired index
            temp = temp.next

        new_node.next = temp.next          # New node’s next points to the next node
        new_node.prev = temp               # New node’s previous points to current node
        temp.next.prev = new_node          # The next node’s previous points to new node
        temp.next = new_node               # Current node’s next points to new node
        self.n += 1                        # Increment node count

    def delete_at(self, index):
        if index < 0 or index >= self.n:   # If index is invalid
            print("Index out of range")
            return
        if index == 0:                     # If deleting the first node
            self.delete_first()            # Use existing delete_first
            return
        elif index == self.n - 1:          # If deleting the last node
            self.delete_last()             # Use existing delete_last
            return

        temp = self.head                   # Start from head
        for _ in range(index):             # Move to the node to be deleted
            temp = temp.next

        temp.prev.next = temp.next         # Link previous node to next node
        temp.next.prev = temp.prev         # Link next node to previous node
        self.n -= 1                        # Decrement node count


# Testing

L = dlist()

L.insert_head(20)
L.insert_head(30)
L.insert_head(40)
L.insert_tail(10)
L.insert_at(2, 50)
L.insert_at(7, 60)

L.traverse()
print(L.isempty())
print(L.len())
print(L[2])
L.delete_first()
L.delete_at(3)
L.traverse()
L.delete_last()
L.traverse()

