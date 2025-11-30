def heapify(arr,n,i): #O(nlogn)
    largest=i
    l=2*i+1
    r=2*i+2
    if l<n and arr[l]>arr[largest]:
        largest=l
    if r<n and arr[r]>arr[largest]:
        largest=r
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)
def heapsort(arr):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        arr[0],arr[i]=arr[i],arr[0]
        heapify(arr,i,0)
def printarr(arr):
    for i in arr:
        print(i,end=" ") 
    print()

# arr=[23,1,4,2,50]
arr=["a","l","a","b"]
heapsort(arr)
printarr(arr)    

class MinHeap:
    def __init__(self):
        self.heap=[]
    def insert(self,value):
        self.heap.append(value)
        self.heapifyup(len(self.heap)-1)
    def heapifyup(self,index):
        parent=(index-1)//2
        if index>0 and self.heap[index]<self.heap[parent]:
            self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
            self.heapifyup(parent)
    def display(self):
        print(self.heap)
max=MinHeap()
max.insert(10)
max.insert(30)
max.insert(20)
max.insert(40)
max.insert(50)
max.display()  

class MaxHeap:
    def __init__(self):
        self.heap=[]
    def insert(self,value):
        self.heap.append(value)
        self.heapifyup(len(self.heap)-1)
    def heapifyup(self,index):
        parent=(index-1)//2
        if index>0 and self.heap[index]>self.heap[parent]:
            self.heap[index],self.heap[parent]=self.heap[parent],self.heap[index]
            self.heapifyup(parent)
    def heapifydown(self,i):
        largest =i
        n=len(self.heap)
        l=2*i+1
        r=2*i+2
        if l<n and self.heap[l]>self.heap[largest]:
            largest=l
        if r<n and self.heap[r]>self.heap[largest]:
            largest=r
        if largest != i:
            self.heap[i],self.heap[largest]=self.heap[largest],self.heap[i]
            self.heapifydown(largest)
    def delete(self):
        if not self.heap:
            return None
        if len(self.heap)==1:
            return self.heap.pop()
        max_item=self.heap[0]
        self.heap[0]=self.heap.pop()
        self.heapifydown(0)
        return max_item
        
    def display(self):
        print(self.heap)
heap=MaxHeap()
heap.insert(40)
heap.insert(20)
heap.insert(70)
heap.display()
print(heap.delete())
heap.display()

def heapify(arr,n,i):
    largest=i 
    l=2*i+1 
    r=2*i+2 
    if l<n and arr[l]>arr[largest]:
        largest=l 
    elif r<n and arr[r]>arr[largest]:
        largest=r  
    if largest!=i:
        arr[i],arr[largest]=arr[largest],arr[i]
        heapify(arr,n,largest)
def largest(arr,k):
    # largest_element=[]
    kth=None

    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i) 
    for _ in range(k):
        # largest_element.append(arr[0])
        kth=arr[0]
        arr[0],arr[n-1]=arr[n-1],arr[0]
        n-=1 
        heapify(arr,n,0)
    # return largest_element 
    return kth
    
arr=[2,11,4,12]
k=2 
print(largest(arr,k))

        