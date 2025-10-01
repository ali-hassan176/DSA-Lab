#class node is create first to give us data and value for each item given to stack
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
#class stack and basic functions
class Stack:
    def __init__(self):
        self.top = None
#Is empty function is used to check whether our stack is empty or not
    def isempty(self):
        return self.top is None
#push function first create new node and then add it in the stack
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
#This function is used to display the stack element
    def traverse(self):
        temp = self.top
        while temp is not None: #Check the condition whether temp(current) is None or not and then traverse to the next
            print(temp.data)
            temp = temp.next
#This one is used to give the element at the top
    def peek(self):
        if self.isempty():
            return 'Stack is Empty'
        else:
            return self.top.data
#This one is used to remove and also return the top value(item)
    def pop(self):
        if self.isempty():
            return 'Stack is Empty'
        else:
            popped = self.top.data
            self.top = self.top.next
            return popped


# Palindrome check
l = 'dad'
s = Stack()
#Add the items of given word to the stack
for i in l:
    s.push(i)


n = '' #An empty string

for i in range(len(l)):
    #Add the top item to the new string n  and then check whether this one is equal to given string or not
    n += s.pop()  

if n == l:
    print('Is palindrome')
else:
    print('Not palindrome')
