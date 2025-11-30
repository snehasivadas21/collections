def is_valide(s):
    stack=[]
    d={"(":")","[":"]"}
    for i in s:
        if i in d.keys():
            stack.append(i)
        else:
            if stack==[]:
                return False
            else:
                if d[stack[-1]]==i:
                    stack.pop()
                else:
                    return False
    if stack==[]:
        return True
    else:
        return False
print(is_valide("()[}]")) 

put="abbaca"
stack=[]
for i in put:
    if stack and stack[-1]==i:
        stack.pop()
    else:
        stack.append(i)
print("".join(stack))        

def reverse(s):
    stack=[]
    for i in s:
        stack.append(i)
    a=""
    while stack:
        a+=stack.pop()
    return a
s="hello"
print(reverse(s))  

def palindrome(str):
    stack=[]
    for i in str:
        stack.append(i)
    for i in str:
        if i!=stack.pop():
            return False
    return True
str="madam"
print(palindrome(str))

def flat(a):
    flat_list=[]
    stack=list(reversed(a))
    while stack:
        item=stack.pop()
        if isinstance(item,list):
            stack.extend(reversed(item))
        elif item > 5:
            flat_list.append(item)
    return flat_list

a=[1,[2,3,[4,5]],6,[7]]
print(flat(a))
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Stack:
    def __init__(self):
        self.head=None
    def push(self,data):
        new_node=Node(data)
        if not new_node:
            print("stack overflow")
        new_node.next=self.head
        self.head=new_node
    def pop(self):
        if not self.head:
            print("stack underflow")
        temp=self.head
        self.head=self.head.next
        del temp
    def peek(self):
        if self.head:
            return self.head.data
        print("stack is empty")
s=Stack()
s.push(11)
s.push(12)
s.push(13)
print(s.peek())
s.pop()
print(s.peek())
    
        