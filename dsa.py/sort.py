def merge_sort_reverse(s):
        indexed_chars = [(char,i) for i,char in enumerate(s)]

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
        
        sorted_char=merge_sort(indexed_chars)
        reversed_string="".join([char for char,_ in sorted_char])
        return reversed_string

# arr=["apple","cherry","blueberry"]
# arr=[67,9,3]
# print(merge_sort(arr))   
s="hello"
print(merge_sort_reverse(s)) 

def bubble_sort(arr):
    while(True):
        a=True
        for i in range(0,len(arr)-1):
            if arr[i]>arr[i+1]:
                arr[i],arr[i+1]=arr[i+1],arr[i]
                a=False
        if a==True:
            break
arr=[2,33,1,4,20] 
bubble_sort(arr)
for i in arr:
    print(i,end=" ")            