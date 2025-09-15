# def non_repeating(s):
#     d={}
#     for i in s:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     for i in reversed(s):
#         if d[i]==1:
#             return i    
# print(non_repeating("abbc"))    

# def char_freq(s):
#     d={}
#     for i in s:
#         if i in d:
#             d[i]+=1
#         else:
#             d[i]=1
#     return d
# print(char_freq("hello world")) 

def remove(s):
    seen=set()
    result=[]
    for i in s:
        if i  not in seen:
            seen.add(i)
            result.append(i)
    return "".join(result)
s="geeksforgeeks"
print(remove(s))

def is_anagram(s1,s2):
    if len(s1)!=len(s2):
        return False
    count={}
    for i in s1:
        if i not in count:
            count[i]=1
        else:
            count[i]+=1
    for i in s2:
        if i not in count:
            return False
        count[i]-=1
    for i in count.values():
        if i!=0:
            return False
    return True
s1="triangle"
s2="integral"
print(is_anagram(s1,s2))
