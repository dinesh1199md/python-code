def count_num(s):
    l=s.split()
    # print(len(l))
    return len(l)
print(count_num("Welcome to Python world"))

def count_num_occarance(s):
    l=s.split()
    d={}
    for i in l:
        if i in d:
            d[i]+=1
        else:
            d[i]=1
    return d            
print(count_num_occarance("Welcome to Python world to world"))