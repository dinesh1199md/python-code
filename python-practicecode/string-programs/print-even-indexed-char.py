def even_index(s):
    # ([(i,j) for i,j in enumerate(s) if i%2==0 and i!=0])
    return "".join([j for i,j in enumerate(s) if i%2==0])
print(even_index("Automation"))
