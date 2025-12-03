class SNode:
    """ Node for singly linked list """
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return f"SNode({self.data})"


class DNode:
    """ Node for doubly linked list """
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return f"DNode({self.data})"
def count_occurrences(head, target):
    """Count how many times target appears in the list."""
    count = 0
    current = head
    while current:
        if current.data == target:
            count += 1
        current = current.next
    return count
def test_count():
    head = SNode(1, SNode(2, SNode(2, SNode(3, SNode(2)))))    
    assert count_occurrences(head, 2) == 3
    assert count_occurrences(head, 1) == 1
    assert count_occurrences(head, 5) == 0
    assert count_occurrences(None, 1) == 0
    print("Count tests passed!")
def reverse_list(head):
    """Reverse a singly linked list iteratively."""
    prev = None
    current = head
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
def test_reverse():
    head = SNode(1, SNode(2, SNode(3)))
    reversed_head = reverse_list(head)
    assert reversed_head.data == 3
    assert reversed_head.next.data == 2
    assert reversed_head.next.next.data == 1
    assert reversed_head.next.next.next is None
    assert reverse_list(None) is None
    single = SNode(5)
    assert reverse_list(single).data == 5
    print("Reverse tests passed!")

def reverse_dll(head):
    """Reverse a doubly linked list."""
    current = head
    prev = None
    while current:
        nxt = current.next
        current.next = current.prev
        current.prev = nxt
        prev = current
        current = nxt
    return prev
def test_reverse_dll():
    node1 = DNode(1)
    node2 = DNode(2)
    node3 = DNode(3)
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    reversed_head = reverse_dll(node1)
    assert reversed_head.data == 3
    assert reversed_head.next.data == 2
    assert reversed_head.next.next.data == 1
    assert reversed_head.next.next.next is None
    assert reversed_head.prev is None
    assert reversed_head.next.prev.data == 3
    assert reversed_head.next.next.prev.data == 2
    print("DLL reverse tests passed!")

def remove_duplicates_dll(head):
    """Remove duplicates from sorted doubly linked list."""
    current = head
    while current and current.next:
        if current.data == current.next.data:
            # Skip the duplicate node
            duplicate = current.next
            current.next = duplicate.next
            if duplicate.next:
                duplicate.next.prev = current
        else:
            current = current.next
    return head
def test_remove_duplicates_dll():
    node1 = DNode(1)
    node2a = DNode(2)
    node2b = DNode(2)
    node3a = DNode(3)
    node3b = DNode(3)
    node3c = DNode(3)

    node1.next = node2a
    node2a.prev = node1
    node2a.next = node2b
    node2b.prev = node2a
    node2b.next = node3a
    node3a.prev = node2b
    node3a.next = node3b
    node3b.prev = node3a
    node3b.next = node3c
    node3c.prev = node3b

    result = remove_duplicates_dll(node1)
    assert result.data == 1
    assert result.next.data == 2
    assert result.next.next.data == 3
    assert result.next.next.next is None
    assert result.next.prev.data == 1
    assert result.next.next.prev.data == 2
    print("DLL remove duplicates tests passed!")

def merge_sorted_lists(l1, l2):
    """Merge two sorted singly linked lists."""
    dummy = SNode(0)
    tail = dummy
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
    return dummy.next
def test_merge_sorted():
    l1 = SNode(1, SNode(3, SNode(5)))
    l2 = SNode(2, SNode(4, SNode(6)))
    merged = merge_sorted_lists(l1, l2)
    expected = [1, 2, 3, 4, 5, 6]
    current = merged
    for val in expected:
        assert current.data == val
        current = current.next
    assert current is None
    assert merge_sorted_lists(None, None) is None
    assert merge_sorted_lists(SNode(1), None).data == 1
    assert merge_sorted_lists(None, SNode(1)).data == 1
    print("Merge sorted tests passed!")

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

class BTS:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root==None:
            self.root = TreeNode(data)
            return

        current = self.root
        while True:
            if data < current.data:
                if current.left:
                    current = current.left
                else:
                    current.left = TreeNode(data)
                    break
            else:
                if current.right:
                    current = current.right
                else:
                    current.right = TreeNode(data)
                    break

    def khoji(self, data):

        current = self.root
        while current:
            if data == current.data:
                return True
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        return False

    def inorder_traversal(self):
        result = []          
        stack = []       
        current = self.root 
    
        while current or stack:  
            while current:       
                stack.append(current) 
                current = current.left 
        
            current = stack.pop()      
            result.append(current.data) 
        
            current = current.right    
    
        return result
    def find_min(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current.data

    def find_max(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current.data
    
    def height(self):
        if not self.root:
            return 0
        queue = [self.root]
        height = 0
        
        while queue:
            level_size = len(queue)
            height += 1
            for _ in range(level_size):
                current = queue.pop(0)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
        return height

def test_simple_bst():
    bst = BTS()
    values = [5, 3, 7, 2, 4, 6, 8]
    for v in values:
        bst.insert(v)
    assert bst.khoji(5)
    assert bst.khoji(3)
    assert bst.khoji(7)
    assert not bst.khoji(10)
    assert bst.inorder_traversal() == [2, 3, 4, 5, 6, 7, 8]
    empty = BTS()
    assert not empty.khoji(5)
    assert empty.inorder_traversal() == []
    print("BST basic tests passed!")


def test_min_max():
    bst = BTS()
    assert bst.find_min() is None
    assert bst.find_max() is None
    for v in [5, 3, 7, 2, 4, 6, 8]:
        bst.insert(v)
    assert bst.find_min() == 2
    assert bst.find_max() == 8
    print("Min/Max tests passed!")

        
def test_height():
    bst = BTS()
    assert bst.height() == 0
    bst.insert(5)
    assert bst.height() == 1
    bst.insert(3)
    bst.insert(7)
    assert bst.height() == 2
    bst2 = BTS()
    for v in [1, 2, 3, 4]:
        bst2.insert(v)
    assert bst2.height() == 4
    print("Height tests passed!")

test_count()
test_reverse()
test_reverse_dll()
test_remove_duplicates_dll()
test_merge_sorted()
test_simple_bst()
test_min_max()
test_height()