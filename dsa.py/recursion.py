def bineary_search(arr,high,low,x): #Olog(n) - O(1)
    if high >= low:
        mid=(high+low)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return bineary_search(arr,mid-1,low,x)
        else:
            return bineary_search(arr,high,mid+1,x)
    return -1
arr=[1,2,3,4]
x=4
result=bineary_search(arr,len(arr)-1,0,x)
if result!=-1:
    print(result)
else:
    print("No")        

def fib(n): #0,1,1,2,3,5,8,13
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
def list_fib(n):
    return [fib(i) for i in range(n)]
print(list_fib(10))

def fact(n):
    if n<=1:
        return n
    return n*fact(n-1)
print(fact(5))

def reverse_word(word): #O(n)
    if len(word) <= 1:
        return word
    return reverse_word(word[1:]) + word[0]

def reverse_each_word(sentence):
    words = sentence.split()
    return ' '.join(reverse_word(word) for word in words)
print(reverse_each_word("hello world"))

def rev(sentence):
    if len(sentence)<=1:
        return sentence
    return rev(sentence[1:])+[sentence[0]]
sentence="hello world"
word=sentence.split()
print(" ".join(rev(word)))

def sum_arr(arr,N):
    if N==0:
        return 0
    return arr[N-1]+sum_arr(arr,N-1)
arr=[1,2,3,4]
N=len(arr)
print(sum_arr(arr,N))

def sum_even_recursion(arr):
    if not arr:
        return 0
    else:
        first_element=arr[0]
        if first_element%2==0:
            return first_element+sum_even_recursion(arr[1:])
        else:
            return sum_even_recursion(arr[1:])
arr=[1,2,2,3,4,5]
print(sum_even_recursion(arr))     


    