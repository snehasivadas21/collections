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

def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
def list_fib(n):
    return [fib(i) for i in range(n)]
print(list_fib(5))

def fact(n):
    if n<=1:
        return n
    return n*fact(n-1)
print(fact(5))

def reverse_word(word):
    if len(word) <= 1:
        return word
    return reverse_word(word[1:]) + word[0]

def reverse_each_word(sentence):
    words = sentence.split()
    return ' '.join(reverse_word(word) for word in words)
print(reverse_each_word("hello world"))

    