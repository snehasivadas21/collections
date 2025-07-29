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