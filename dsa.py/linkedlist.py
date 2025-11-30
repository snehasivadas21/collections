class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

    def insert_head(self,data): #O(1)
        new_node=Node(data)
        new_node.next=self.head  
        self.head=new_node    

    def insert_end(self,data): #O(n)
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return 
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node

    def middle(self): #O(n)
        if not self.head:
            return None
        fast=slow=self.head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
        #     if slow==fast:
        #         return True
        # return False
        return slow.data  

    def cycle(self): #O(n)
        fast=slow=self.head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next
            if slow==fast:
        #         return True
        # return False 
                slow=self.head
                while slow != fast:
                    slow=slow.next
                    fast=fast.next
                return slow.data
        return -1       

    def reverse(self): #O(n)
        prev,cur=None,self.head
        while cur:
            new_node=cur.next
            cur.next=prev
            prev=cur
            cur=new_node
        self.head = prev 

    def palindrome(self):
        if not self.head or not self.head.next:
            return True
        fast=self.head
        slow=self.head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        prev=None
        curr=slow
        while curr:
            nxt=curr.next
            curr.next=prev
            prev=curr
            curr=nxt

        left=self.head
        right=prev
        while right:
            if left.data != right.data:
                return False
            left=left.data
            right=right.data
        return True                    

    def delete(self,n):
        fast=self.head
        slow=self.head
        for _ in range(n):
            fast=fast.next
        while fast.next is not None:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return self.head   
    
    def delete_front(self):
        if not self.head:
            return None
        self.head=self.head.next

    def deletelast(self):
        if self.head is None:
            return None
        if self.head.next is None:
            return None
        temp=self.head
        while temp.next.next is not None:
            temp=temp.next
        temp.next=None
        return self.head   

    def del_middle(self):
        if not self.head or not self.head.next:
            return None
        prev=None   
        slow=self.head
        fast=self.head
        while fast and fast.next:
            fast=fast.next.next
            prev=slow
            slow=slow.next
        prev.next=slow.next
        return self.head                         

    def traverse(self): #O(n)
        curr=self.head
        while curr:
            print(curr.data,end=" -> ")
            curr=curr.next
        print("None")                      

ll=Linkedlist()
arr=[1,2,3,4,4]
ll.insert_head(0)    
for i in arr:
    ll.insert_end(i)   
print(ll.middle())
ll.head.next.next.next.next.next = ll.head.next.next 
print(ll.cycle())  
ll.traverse() 
ll.reverse()
print(ll.palindrome())
ll.delete(2)
ll.delete_front()
ll.deletelast()
ll.del_middle()
ll.traverse()  

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self):
        self.head=None

    def insert_end(self,data): #O(n)
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return 
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node

    def second(self):
        if not self.head and not self.head.next:
            return None
        first=float('-inf')
        second=float('-inf')
        curr=self.head
        while curr:
            if first < curr.data:
                second=first
                first=curr.data
            elif second < curr.data and first != curr.data:
                second=curr.data
            curr=curr.next
        return second   
    
    def remove_odd(self):
        while self.head and self.head.data %2 !=0:
            self.head=self.head.next
        if not self.head:
            return None
        prev=self.head
        curr=prev.next
        while curr:
            if curr.data % 2!=0:
                prev.next=curr.next
            else:
                prev=curr
            curr=curr.next
        return self.head  
    
    def remove_dup(self):
        cur=self.head
        while cur.next:
            if cur.data == cur.next.data:
                cur.next=cur.next.next
            else:
                cur=cur.next   

    def traverse(self): #O(n)
        curr=self.head
        while curr:
            print(curr.data,end=" -> ")
            curr=curr.next
        print("None")                      

ll=Linkedlist()
arr=[1,2,3,4,4,5,6]
for i in arr:
    ll.insert_end(i)  
ll.traverse()
print(ll.second())
ll.remove_odd()
ll.remove_dup()
ll.traverse()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None

def insert_beg(head,data):
    new_node=Node(data)
    new_node.next=head
    if head:
        head.prev=new_node
    return new_node

def insert_after(node,data):
    if not node:
        print("error")
        return 
    new_node=Node(data)
    new_node.prev=node
    new_node.next=node.next
    if node.next:
        node.next.prev=new_node
    node.next=new_node

def insert_before(node,data):
    if not node:
        print("error")
        return 
    new_node=Node(data)
    new_node.prev=node.prev
    new_node.next=node
    if node.prev:
        node.prev.next=new_node
    node.prev=new_node

def insert_end(head,data):
    new_node=Node(data)
    if not head:
        return new_node
    curr=head
    while curr.next:
        curr=curr.next
    curr.next=new_node
    new_node.prev=curr
    return head

def traverse(head):
    curr=head
    while curr:
        print(curr.data,end="<-->")
        curr=curr.next
    print("None") 
    
head=None
head=insert_beg(head,1)

node2=Node(2)
node3=Node(3)
head.next=node2
node2.prev=head
node2.next=node3
node3.prev=node2
traverse(head)

insert_after(node2,10)
insert_before(node3,20)

head=insert_end(head,4)
traverse(head)
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Cll:
    def __init__(self):
        self.head=None

    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=new_node
            return
        curr=self.head
        while curr.next != self.head:
            curr=curr.next
        curr.next=new_node
        new_node.next=self.head
        self.head=new_node

    def display(self):
        if not self.head:
            return 
        curr=self.head
        while True:
            print(curr.data,end=" ")
            curr=curr.next
            if curr==self.head:
                break
        print()

cl=Cll()
first=Node(2)
first.next=Node(3)
first.next.next=Node(4)
last=first.next.next
last.next=first
cl.head=first
cl.insert_end(5)
cl.insert_end(6)
cl.display()

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class CDll:
    def __init__(self):
        self.head=None
    def insert_end(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            new_node.next=new_node
            new_node.prev=new_node
            return 
        last=self.head.prev
        last.next=new_node
        new_node.prev=last
        new_node.next=self.head
        self.head.prev=new_node

    def display_forward(self):
        if self.head is None:
            return 
        curr=self.head
        while True:
            print(curr.data,end=" ")
            curr=curr.next
            if curr==self.head:
                break
        print()

    def display_back(self):
        if self.head is None:
            return 
        curr=self.head.prev
        while True:
            print(curr.data,end=" ")
            curr=curr.next
            if curr==self.head.prev:
                break
        print() 
        
cd=CDll()
head=Node(10)
head.next=Node(20)
head.next.prev=head
head.next.next=Node(30)
head.next.next.prev=head.next
head.next.next.next=head
head.prev=head.next.next
cd.head=head
cd.insert_end(5)
cd.insert_end(15)
cd.display_forward()
cd.display_back()


    
    
