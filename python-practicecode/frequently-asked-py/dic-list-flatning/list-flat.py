#normal list flatning
def plain(a):
    l=[]
    for i in a:
        if isinstance(i,list):
            l.extend(plain(i))
        else:
            l.append(i)
    return l
Arr = [1, 2, [3, 4, [5, 6]]]
# Arr=[[1, 2], [3, 4]]
print(plain(Arr))

# out=[1, 2, 3, 4, 5, 6]

#Flatning using generator
def gen_flat(a):
    for i in a:
        if isinstance(i,list):
            yield from (gen_flat(i))
        else:
            yield i
Arr = [1, 2, [3, 4, [5, 6]]]
print(list(gen_flat(Arr)))

#word flat
def word_flat(a):
    l=[]
    for i in a:
        if isinstance(i,list):
            l.extend( word_flat(i))
        else:
            l.append(i)
    return l

Arr=["Hello", ["world", "!"]]
print( " ".join(word_flat(Arr)))

#normal list flatning with sort
def plain_sort(a):
    l=[]
    for i in a:
        if isinstance(i,list):
            l.extend(plain_sort(i))
        else:
            l.append(i)
    return l
Arr = [[3, 2], [1], [5, 4]]
print(sorted(plain_sort(Arr)))