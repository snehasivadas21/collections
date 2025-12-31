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

def search(root,data):
    if root is None or root.data==data:
        return root
    if root.data>data:
        return search(root.left,data)
    return search(root.right,data)                  
                        
def height(root): #O(n)
    if not root:
        return -1
    left=height(root.left)
    right=height(root.right)
    return 1+max(left,right) 

def isBalanced(root):
    if root is None:
        return True
    lHeight=height(root.left)
    rHeight=height(root.right)
    if abs(lHeight-rHeight)>1:
        return False
    return isBalanced(root.left) and isBalanced(root.right)

def maximum(root):
    if root is None:
        return float('-inf')
    left=maximum(root.left)
    right=maximum(root.right)
    return max(root.data,left,right)

def minimum(root):
    if root.left is None:
        return root.data
    return minimum(root.left)

def inorder(root): #O(n)
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)    

r=TreeNode(50)
insert(r,30)
insert(r,60)
print("found" if search(r,90) else "not found")
print(height(r))
print("True" if isBalanced(r) else "False")
inorder(r)
print(maximum(r))
print(minimum(r))  

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

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def inorder(root,prev):
    if root is None:
        return True
    if not inorder(root.left,prev):
        return False
    if prev[0]>=root.data:
        return False
    prev[0]=root.data
    return inorder(root.right,prev)
def isbst(root):
    return inorder(root,[float('-inf')])

r=Node(10)
r.left=Node(9)
r.right=Node(11)
r.left.left=Node(7)
print(isbst(r))

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def lca(root,n1,n2):
    if root is None:
        return None
    if n1<root.data and n2<root.data:
        return lca(root.left,n1,n2)
    elif n1>root.data and n2>root.data:
        return lca(root.right,n1,n2)
    else:  
        return root

def isidential(r1,r2):
    if r1 is None or r2 is None:
        return False
    if r1 is None and r2 is None:
        return True
    return (r1.data==r2.data and isidential(r1.left,r2.left) and isidential(r1.right,r2.right)) 
   
r = Node(20)
r.left = Node(10)
r.right = Node(30)
r.left.left = Node(5)
r.left.right = Node(15)
print(lca(r,5,15).data)

r1=Node(20)
r1.left=Node(10)
r1.right=Node(30)
if isidential(r,r1):
    print("yes")
else:
    print("no") 

class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def arrtoBst(arr,start,end):
    if start>end:
        return None
    mid=start+(end-start)//2
    root=Node(arr[mid])
    
    root.left=arrtoBst(arr,start,mid-1)
    root.right=arrtoBst(arr,mid+1,end)
    return root
def Bst(arr):
    return arrtoBst(arr,0,len(arr)-1)
arr=[1, 5, 9, 14, 23, 27]
r=Bst(arr)
print(r.data)
    
class TreeNode:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
def find_k_largest(root,k):
    result=[]
    def rev_inorder(node):
        if not node or len(result)>=k:
            return 
        rev_inorder(node.right)
        if len(result)<k:
            result.append(node.val)
        rev_inorder(node.left)
    rev_inorder(root)
    return result
def delete(root,key):
    if not root:
        return None
    if key<root.val:
        root.left=delete(root.left,key)
    elif key>root.val:
        root.right=delete(root.right,key)
    else:
        if not root.left and not root.right:
            return None
        if not root.right:
            return root.left
        elif not root.left:
            return root.right
        temp=root.right
        while temp.left:
            temp=temp.left
        root.val=temp.val
        root.right=delete(root.right,temp.val)
    return  root
def remove_k_largest(root,k):
    largest_val=find_k_largest(root,k)
    for val in largest_val:
        root=delete(root,val)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val,end=" ")
        inorder(root.right)
        
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(10)
root.right.left = TreeNode(7)

inorder(root)
root = remove_k_largest(root, 3)     
inorder(root)
            
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
def isLeaf(node):
    if node is None:
        return False
    if node.left is None and node.right is None:
        return True
    return False
def sumofLeft(root):
    result=0
    if root is not None:
        if isLeaf(root.left):
            result+=root.left.data
        else:
            result+=sumofLeft(root.left)
        result+=sumofLeft(root.right)
    return result
tree=TreeNode(50)
tree.left=TreeNode(30)
tree.right=TreeNode(60)
tree.right.left=TreeNode(40)
print(sumofLeft(tree))

        