class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Queue:
    def __init__(self):
        self.head=None
    def enqueue(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return 
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=new_node
    def dequeue(self):
        if not self.head:
            return None
        self.head=self.head.next
    def display(self):
        curr=self.head
        while curr:
            print(curr.data,end="-->")
            curr=curr.next
        print("None")
q=Queue()
arr=[1,2,3,4]
for i in arr:
    q.enqueue(i)
q.display()
q.dequeue()
q.display()                                           

def stack_queue(stack):
    queue=[]
    while stack:
        queue.append(stack.pop())
    return queue    
stack=[10,20,30]
queue=stack_queue(stack)
print(queue)

from collections import deque

q=deque([10,20,30])
stack=[]
while q:
    stack.append(q.popleft())
print(stack)
print(stack.pop())

class Queue:
    def __init__(self,c):
        self.l=[None]*c
        self.cap=c
        self.size=0
        self.front=0
    def getfront(self):
        if self.size==0:
            return None
        return self.l[self.front]
    def getrear(self):
        if self.size==0:
            return None
        rear=(self.front+self.size -1)%self.cap
        return self.l[rear]
    def enqueue(self,x):
        if self.size==self.cap:
            return 
        rear=(self.front+self.size)%self.cap
        self.l[rear]=x
        self.size+=1
    def dequeue(self):
        if self.size==0:
            return 
        res=self.l[self.front]
        self.front=(self.front+1)%self.cap
        self.size-=1
        return res
q=Queue(5)
q.enqueue(15)
q.enqueue(16)
q.enqueue(17)
print(q.getfront())
print(q.getrear())
q.dequeue()
print(q.getfront())
print(q.getrear())


    