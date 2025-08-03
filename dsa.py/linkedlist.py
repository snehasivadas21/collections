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

    def reverse(self): #O(n)
        prev,cur=None,self.head
        while cur:
            new_node=cur.next
            cur.next=prev
            prev=cur
            cur=new_node
        self.head = prev    

    def duplicate(self):
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
arr=[1,2,3,4,4]
ll.insert_head(0)    
for i in arr:
    ll.insert_end(i)   
print(ll.middle())  
ll.traverse() 
ll.reverse()
ll.duplicate()
ll.traverse()  

