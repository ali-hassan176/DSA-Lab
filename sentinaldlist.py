# Node class for doubly linked list
class Node:
    def __init__(self, value=None):
        # value stores the data
        self.data = value
        # next points to the next node
        self.next = None
        # prev points to the previous node
        self.prev = None

# Doubly Linked List class with Sentinel Nodes
class DList:
    def __init__(self):
        # Create two sentinel (dummy) nodes: head and tail
        # They don't store real data — just structure
        self.head = Node()   # sentinel head
        self.tail = Node()   # sentinel tail
        # Link head and tail to each other initially
        self.head.next = self.tail
        self.tail.prev = self.head
        # Length of actual data nodes (not counting sentinels)
        self.n = 0
    def insert_head(self, value):
        # Create a new node with given value
        new_node = Node(value)

        # The node currently after head (could be tail if empty)
        first = self.head.next

        # Link new_node between head and first
        new_node.prev = self.head
        new_node.next = first

        # Update pointers of surrounding nodes
        self.head.next = new_node
        first.prev = new_node
        # Increase node count
        self.n += 1
    def insert_tail(self, value):
        # Create new node
        new_node = Node(value)

        # The node currently before tail
        last = self.tail.prev

        # Link new_node between last and tail
        new_node.next = self.tail
        new_node.prev = last

        # Update surrounding nodes
        last.next = new_node
        self.tail.prev = new_node

        # Increase count
        self.n += 1

    def insert_at(self, index, value):
        # Check for valid range
        if index < 0 or index > self.n:
            print("Index out of range")
            return
        # Traverse from head to the node just before index
        temp = self.head
        for _ in range(index):
            temp = temp.next

        # Create the new node
        new_node = Node(value)

        # Adjust pointers to insert new_node between temp and temp.next
        new_node.next = temp.next
        new_node.prev = temp
        temp.next.prev = new_node
        temp.next = new_node

        # Increase count
        self.n += 1

    def delete_first(self):
        # If list is empty (no nodes between sentinels)
        if self.head.next == self.tail:
            print("List is empty")
            return

        # Node to delete
        first = self.head.next

        # Bypass it by linking head directly to the next node
        self.head.next = first.next
        first.next.prev = self.head

        # Decrease count
        self.n -= 1

    def delete_last(self):
        # If list is empty
        if self.tail.prev == self.head:
            print("List is empty")
            return

        # Node to delete
        last = self.tail.prev

        # Bypass it by linking tail to the previous node
        self.tail.prev = last.prev
        last.prev.next = self.tail

        # Decrease count
        self.n -= 1

    def delete_at(self, index):
        # Check for valid index
        if index < 0 or index >= self.n:
            print("Index out of range")
            return

        # Traverse to the node at that index
        temp = self.head.next
        for _ in range(index):
            temp = temp.next

        # Bypass this node
        temp.prev.next = temp.next
        temp.next.prev = temp.prev

        # Decrease count
        self.n -= 1

    def traverse(self):
        # Start from the first real node (after head sentinel)
        temp = self.head.next

        # Traverse until we reach tail sentinel
        while temp != self.tail:
            print(temp.data, end=" ")
            temp = temp.next
        print()  # new line

    def reverse_traverse(self):
        # Start from last real node (before tail sentinel)
        temp = self.tail.prev

        # Traverse until we reach head sentinel
        while temp != self.head:
            print(temp.data, end=" ")
            temp = temp.prev
        print()

    def __getitem__(self, index):
        # Check for valid index
        if index < 0 or index >= self.n:
            raise IndexError("Index out of range")

        # Traverse from head
        temp = self.head.next
        for _ in range(index):
            temp = temp.next
        return temp.data

    def __len__(self):
        # Return number of real nodes
        return self.n

    def isempty(self):
        return self.n == 0


# Testing
L = DList()
L.insert_head(20)
L.insert_head(30)
L.insert_tail(10)
L.insert_at(1, 40)

print("List (forward): ", end="")
L.traverse()

print("List (reverse): ", end="")
L.reverse_traverse()

print("Length:", len(L))
print("Is empty?", L.isempty())
print("Element at index 2:", L[2])

L.delete_first()
print("After deleting first:", end=" ")
L.traverse()

L.delete_last()
print("After deleting last:", end=" ")
L.traverse()

L.delete_at(1)
print("After deleting index 1:", end=" ")
L.traverse()
