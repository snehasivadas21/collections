# n=5
# for i in range(n):
#     for j in range(i+1):
#         print("j",end=" ")
#     print()    

# n=5
# for i in range(n):
#     for j in range(i,n):
#         print("*",end=" ")
#     for k in range(i+1):
#         print(" ",end=" ")    
#     print()    

# n=5
# for i in range(n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for k in range(i,n):
#         print("*",end=" ")    
#     print()    

# n=5
# for i in range(n,0,-1):
#     for j in range(i,0,-1):  
#         print(j,end=" ")
#     print()     

# n=5
# for i in range(n,0,-1):
#     for j in range(i,0,-1):
#         print(i,end=" ")
#     print()    

# n=5
# for i in range(n):
#     for j in range(n-i-1):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()  

# def star_pyr(rows):
#     for i in range(rows):
#         print(" "*(rows-i-1)+"*"*(2*i+1))
# star_pyr(5)       

# for i in range(5, 0, -1):
#     print(" " * (5 - i) + "*" * (2 * i - 1))

# n=5
# for i in range(n-1,-1,-1):
#     for j in range(n-i):
#         print(" ",end=" ")
#     for k in range(2*i+1):
#         print("*",end=" ")
#     print()    

# n=5
# for i in range(1,n+1):
#     for j in range(i,n+1):
#         print(j,end=" ")
#     print()  

n=6
val=1
for i in range(1,n+1):
    for j in range(i):
        print(val,end=" ")
        val+=1
    print()    