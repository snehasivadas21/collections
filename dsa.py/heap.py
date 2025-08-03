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
    def display(self):
        print(self.heap)
max=MaxHeap()
max.insert(10)
max.insert(30)
max.insert(20)
max.insert(40)
max.insert(50)
max.display()                    