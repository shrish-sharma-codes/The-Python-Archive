MAX = 100
   
# A Binary Tree node
class Node:
      
    def __init__(self, data):
          
        self.left = None
        self.right = None
        self.data = data
   
# A utility function to 
# create a new Binary Tree
# Node
def newNode(item):
      
    temp = Node(item)
    return temp
   
# Function to store nodes of 
# alternate levels in an array
def storeAlternate(root, arr, 
                   index, l):
    
    # Base case
    if (root == None):
        return index;
   
    # Store elements of 
    # left subtree
    index = storeAlternate(root.left, 
                           arr, index,
                           l + 1);
   
    # Store this node only if 
    # this is a odd level node
    if(l % 2 != 0):    
        arr[index] = root.data;
        index += 1;    
   
    # Store elements of right 
    # subtree
    index=storeAlternate(root.right, 
                         arr, index, 
                         l + 1);
    return index
   
# Function to modify Binary Tree 
# (All odd level nodes are
# updated by taking elements from 
# array in inorder fashion)
def modifyTree(root, arr, index, l):
  
    # Base case
    if (root == None):
        return index;
   
    # Update nodes in left subtree
    index=modifyTree(root.left, 
                     arr, index, 
                     l + 1);
   
    # Update this node only 
    # if this is an odd level 
    # node
    if (l % 2 != 0):    
        root.data = arr[index];
        index += 1;    
   
    # Update nodes in right 
    # subtree
    index=modifyTree(root.right,
                     arr, index, 
                     l + 1);
    return index
   
# A utility function to 
# reverse an array from 
# index 0 to n-1
def reverse(arr, n):
  
    l = 0
    r = n - 1;
      
    while (l < r):        
        arr[l], arr[r] = (arr[r], 
                          arr[l]);        
        l += 1
        r -= 1
      
# The main function to reverse 
# alternate nodes of a binary tree
def reverseAlternate(root):
  
    # Create an auxiliary array 
    # to store nodes of alternate 
    # levels
    arr = [0 for i in range(MAX)]
    index = 0;
   
    # First store nodes of 
    # alternate levels
    index=storeAlternate(root, arr, 
                         index, 0);
   
    # Reverse the array
    reverse(arr, index);
   
    # Update tree by taking 
    # elements from array
    index = 0;
    index=modifyTree(root, arr, 
                     index, 0);
   
# A utility function to print
# indorder traversal of a
# binary tree
def printInorder(root):
  
    if(root == None):
        return;
    printInorder(root.left);
    print(root.data, end = ' ')
    printInorder(root.right);
      
# Driver code
if __name__=="__main__":
      
    root = newNode('a');
    root.left = newNode('b');
    root.right = newNode('c');
    root.left.left = newNode('d');
    root.left.right = newNode('e');
    root.right.left = newNode('f');
    root.right.right = newNode('g');
    root.left.left.left = newNode('h');
    root.left.left.right = newNode('i');
    root.left.right.left = newNode('j');
    root.left.right.right = newNode('k');
    root.right.left.left = newNode('l');
    root.right.left.right = newNode('m');
    root.right.right.left = newNode('n');
    root.right.right.right = newNode('o');
      
    print("Inorder Traversal of given tree")
    printInorder(root);
   
    reverseAlternate(root);
      
    print("\nInorder Traversal of modified tree")
    printInorder(root);
