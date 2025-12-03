class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.n = 0
    
    def __len__(self):
        return self.n
    
    def insert_head(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.n += 1
    
    def __str__(self):
        curr = self.head
        result = ""
        while curr != None:
            result += str(curr.data) + "->"
            curr = curr.next
        result += 'None'
        return result
    
    def insert_tail(self, item):
        new_node = Node(item)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = new_node
        self.n += 1
    
    def insert_at(self, index, item):
        if 0 > index or index > self.n:
            print('index out of range')
            return
        new_node = Node(item)
        if index == 0:
            self.insert_head(item)
            return
        i = 0
        curr = self.head
        while curr != None:
            if i == index - 1:
                new_node.next = curr.next
                curr.next = new_node
                self.n += 1
                return
            curr = curr.next
            i += 1
    
    def __getitem__(self, index):
        if 0 > index or index >= self.n:
            return 'out of range'
        curr = self.head
        c = 0
        while curr != None:
            if index == c:
                return curr.data
            curr = curr.next
            c += 1
    
    def contains(self, item):
        """Check if item exists in the linked list"""
        curr = self.head
        while curr != None:
            if curr.data == item:
                return True
            curr = curr.next
        return False
    
    def display(self):
        """Display linked list contents as a list"""
        result = []
        curr = self.head
        while curr != None:
            result.append(curr.data)
            curr = curr.next
        return result

    def display_simple(self):
        """Display for the simple hash table representation"""
        if self.head is None:
            return None
        elif self.head.next is None:
            return self.head.data
        else:
            # For multiple items, return as list
            return self.display()

# Test with the same hash function that produced your output
def hash_function(value):
    sum_of_chars = 0
    for char in str(value):
        sum_of_chars += ord(char)
    return sum_of_chars % 10

print("'Bob' has hash code:", hash_function('Bob'))

# Phase 1: Simple hash table (no chaining)
my_list = [None, None, None, None, None, None, None, None, None, None]

def add_simple(name):
    index = hash_function(name)
    my_list[index] = name

add_simple('Bob')
print(my_list)

# Phase 2: Add more items (overwrites will occur)
add_simple('Pete')
add_simple('Jones')
add_simple('Lisa')
add_simple('Siri')
print(my_list)

def contains_simple(name):
    index = hash_function(name)
    return my_list[index] == name

print("'Pete' is in the Hash Table:", contains_simple('Pete'))

# Phase 3: Hash table with linked list chaining
hash_table = [LinkedList() for _ in range(10)]

def add_chaining(name):
    index = hash_function(name)
    hash_table[index].insert_tail(name)

# Add all items including Stuart
add_chaining('Bob')
add_chaining('Pete')
add_chaining('Jones')
add_chaining('Lisa')
add_chaining('Siri')
add_chaining('Stuart')

print("[", end="")
for i in range(len(hash_table)):
    if i > 0:
        print(", ", end="")
    ll_display = hash_table[i].display_simple()
    if ll_display is None:
        print("[]", end="")
    elif isinstance(ll_display, list):
        print(ll_display, end="")
    else:
        print(f"'{ll_display}'", end="")
print("]")

# Test contains with chaining
def contains_chaining(name):
    index = hash_function(name)
    return hash_table[index].contains(name)

print("\nTesting contains with chaining:")
print("'Pete' is in the Hash Table:", contains_chaining('Pete'))
print("'Lisa' is in the Hash Table:", contains_chaining('Lisa'))
print("'Stuart' is in the Hash Table:", contains_chaining('Stuart'))

# Display full linked list structure
print("\nFull linked list structure:")
for i in range(len(hash_table)):
    if hash_table[i].head is not None:
        print(f"Index {i}: {hash_table[i]}")