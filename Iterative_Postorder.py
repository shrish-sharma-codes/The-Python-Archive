class Node:
     
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
 
# An iterative function to do postorder
# traversal of a given binary tree
def postOrderIterative(root):
 
    if root is None:
        return       
     
    # Create two stacks
    s1 = []
    s2 = []
     
    # Push root to first stack
    s1.append(root)
     
    # Run while first stack is not empty
    while s1:
         
        # Pop an item from s1 and
        # append it to s2
        node = s1.pop()
        s2.append(node)
     
        # Push left and right children of
        # removed item to s1
        if node.left:
            s1.append(node.left)
        if node.right:
            s1.append(node.right)
 
        # Print all elements of second stack
    while s2:
        node = s2.pop()
        print node.data,
 
# Driver program to test above function
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
postOrderIterative(root)
