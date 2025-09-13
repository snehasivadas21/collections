class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

def insert(root,data):
    if root is None:
        return TreeNode(data)
    if root.data==data:
        return root
    if root.data<data:
        root.right=insert(root.right,data)
    else:
        root.left=insert(root.left,data)
    return root                
                        
def height(root): #O(n)
    if not root:
        return -1
    left=height(root.left)
    right=height(root.right)
    return 1+max(left,right)    

def inorder(root): #O(n)
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)    

r=TreeNode(50)
insert(r,30)
insert(r,60)
print(height(r))
inorder(r)

class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

def kthsmallest(root,k):
    def inorder(node):
        if not node:
            return None
        left=inorder(node.left)
        if left is not None:
            return left
    
        inorder.count+=1
        if inorder.count==k:
            return node.val
        return inorder(node.right)    
    inorder.count=0
    return inorder(root)   
r=Node(5)
r.left=Node(4)
r.right=Node(6)
r.left.left=Node(3)
print(kthsmallest(r,2))
