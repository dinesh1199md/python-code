def asski(n):
    w=["zero","one","two","three","four","five","six","seven","eight","nine"]
    new=""
    s=str(n)
    for i in s:
        new+=w[ord(i)-ord("0")]+" "
        print(ord(i),ord("0"))
    # print(new)
    return new
print(asski(129))