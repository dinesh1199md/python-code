

def rev(s):
    t=s.split()
    print(t)
    return(" ".join([x[::-1] for x in t]))
print(rev("try coding"))