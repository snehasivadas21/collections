# def count_vowels(s):
#     vowels="aeiou"
#     return sum( 1 for i in s if i in vowels)
# print(count_vowels("sneha"))  

# def rev(s):
#     return s[::-1]    
#     return s.upper()
#     return s[0].upper()+s[1:-1]+s[-1].upper()
#     return s.replace('a','w')
#     return s.split()
# print(rev("sneha is a cute"))    

a=[1,2,3,4,"string"]
# a.append(7)
# a.extend([8,7])
# a.insert(0,0)
# a.sort(reverse=True)
# print(a)
# print(set(a))
b=[x for x in a if isinstance(x,str)]
print(b)

# l=[i**2 for i in range(1,6)]
# print(l)

d={"name":"sneha","age":23}
# b={"a":1,"b":2}
# d["grade"]="A"
# d.update({"place":"chennai","blood":"AB+"})
# print(d.keys())
del d["age"]
print(d)
# merged={**d,**b}
# print(merged)
for key,value in d.items():
    print(f"{key}-->{value}")

# try:
#     x=10/0
#     b=10/2
# except  ZeroDivisionError:
#     print("error")
# else:
#     print("success")
# finally:
#     print("cleanup")            

# for i in range(5):
#    if  i == 5:
#       break
# else:
#    print("loop completed")   