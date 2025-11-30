def merge_sort(arr):
    if len(arr)<=1:
        return arr
    mid=len(arr)//2
    left_half=merge_sort(arr[:mid])
    right_half=merge_sort(arr[mid:])
    return merge(left_half,right_half)

def merge(left,right):
    sorted_arr=[]
    i=j=0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            sorted_arr.append(left[i])
            i+=1
        else:
            sorted_arr.append(right[j])
            j+=1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr
arr=["apple","cherry","blueberry"]
arr=[67,9,3]
print(merge_sort(arr))   

# def bubble_sort(arr):
#     while(True):
#         a=True
#         for i in range(0,len(arr)-1):
#             if arr[i]>arr[i+1]:
#                 arr[i],arr[i+1]=arr[i+1],arr[i]
#                 a=False
#         if a==True:
#             break
# arr=[2,33,1,4,20] 
# bubble_sort(arr)
# for i in arr:
#     print(i,end=" ")  

# def insertion_sort(arr):
#     if len(arr)<=1:
#         return 
#     for i in range(1,len(arr)):
#         key=arr[i]
#         j=i-1
#         while j>=0 and key<arr[j]:
#             arr[j+1]=arr[j]
#             j-=1
#         arr[j+1]=key
# arr=[20,30,10,9]
# insertion_sort(arr)
# print(arr) 

def selection(arr):
    for i in range(len(arr)-1):
        midx=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[midx]:
                midx=j
        arr[i],arr[midx]=arr[midx],arr[i]
    return arr    
arr=[34,22,14,89]
selection(arr)
for i in arr:
    print(i,end=" ") 

def quick_sort(arr):
    if len(arr)<=1:
        return arr
    pivot=arr[0]
    left=[i for i in arr[1:] if i <= pivot]
    right=[i for i in arr[1:] if i > pivot]
    return quick_sort(left)+[pivot]+quick_sort(right)
arr=[22,33,11,66,55,44]
print(quick_sort(arr))        