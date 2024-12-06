# n=5
# for i in range(n,0,-1):
#     # print(i)
#     for k in range(0,n-i):
#         print(end=" ")
    # for j in range(0,i):
    #     print("*",end=" ")
    # print()  

n=5
for i in range(0,n+1):
    # print(i)
    for k in range(0,n-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()  