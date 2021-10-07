class Node:
    # A constructor for making a new node
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
 
# Given a perfect binary tree print its node in
# specific order
def printSpecificLevelOrder(root):
    if root is None:
        return
     
    # Let us print root and next level first
    print root.data,
     
    # Since it is perfect Binary tree,
    # one of the node is needed to be checked
    if root.left is not None :
        print root.left.data,
        print root.right.data,
     
    # Do anything more if there are nodes at next level
    # in given perfect Binary Tree
    if root.left.left is None:
        return
 
    # Create a queue and enqueue left and right
    # children of root
    q = []
    q.append(root.left)
    q.append(root.right)
     
    # We process two nodes at a time, so we need
    # two variables to store two front items of queue
    first = None
    second = None
    
    # Traversal loop
    while(len(q) > 0):
 
        # Pop two items from queue
        first = q.pop(0)
        second = q.pop(0)
 
        # Print children of first and second in reverse order
        print first.left.data,
        print second.right.data,
        print first.right.data,
        print second.left.data,
         
        # If first and second have grandchildren,
        # enqueue them in reverse order
        if first.left.left is not None:
            q.append(first.left)
            q.append(second.right)
            q.append(first.right)
            q.append(second.left)
 
# Driver program to test above function
 
# Perfect Binary Tree of Height 4
root = Node(1)
  
root.left= Node(2)
root.right   = Node(3)
  
root.left.left  = Node(4)
root.left.right = Node(5)
root.right.left  = Node(6)
root.right.right = Node(7)
  
root.left.left.left  = Node(8)
root.left.left.right  = Node(9)
root.left.right.left  = Node(10)
root.left.right.right  = Node(11)
root.right.left.left  = Node(12)
root.right.left.right  = Node(13)
root.right.right.left  = Node(14)
root.right.right.right  = Node(15)
  
root.left.left.left.left  = Node(16)
root.left.left.left.right  = Node(17)
root.left.left.right.left  = Node(18)
root.left.left.right.right  = Node(19)
root.left.right.left.left  = Node(20)
root.left.right.left.right  = Node(21)
root.left.right.right.left  = Node(22)
root.left.right.right.right  = Node(23)
root.right.left.left.left  = Node(24)
root.right.left.left.right  = Node(25)
root.right.left.right.left  = Node(26)
root.right.left.right.right  = Node(27)
root.right.right.left.left  = Node(28)
root.right.right.left.right  = Node(29)
root.right.right.right.left  = Node(30)
root.right.right.right.right  = Node(31)
  
print "Specific Level Order traversal of binary tree is"
printSpecificLevelOrder(root);
