
def bin_deci(s):
    deci=0
    for i in range(len(s)):
        deci+=int(s[len(s)-1-i])*(2**(i))
    return deci

print(bin_deci("1011"))