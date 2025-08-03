def is_valide(s):
    stack=[]
    d={"(":")","[":"]"}
    for i in s:
        if i in d.keys():
            stack.append(i)
        else:
            if stack==[]:
                return False
            else:
                if d[stack[-1]]==i:
                    stack.pop()
                else:
                    return False
    if stack==[]:
        return True
    else:
        return False
print(is_valide("()[}]"))    

def reverse(s):
    stack=[]
    for i in s:
        stack.append(i)
    a=""
    while stack:
        a+=stack.pop()
    return a
s="hello"
print(reverse(s))     