def product_except(l):
    f=[1]*len(l)
    for i in range(len(l)):
        print(i)
    for i in range(len(l)-1,-1,-1):
        print("rev",i)    

    return f
print(product_except([1,2,3,4]))