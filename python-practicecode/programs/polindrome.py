string = "Madam"


def check_palindrome(string):
    newstr = ''.join([i.lower() for i in string])
    # return string == string[::-1]
    return newstr == newstr[::-1]


def normal(string):
    newstr = ""
    for i in range(len(string)-1, -1, -1):
        newstr += string[i]
    # for i in string:
    #     newstr=i+newstr
    print(string)
    print(newstr)
    return newstr.lower() == string.lower()

def number_polindrome(n):
    rev=0
    n2=n
    while n2>0:
        digit=n2%10
        rev=rev*10+digit
        n2=n2//10
    print(n)
    print(rev)  
    return n==rev

def ignorespecialchar(ss):
    stra=''
    for i in ss:
        if i.isalnum(): #.isalnumm --> num & char
            stra= i+stra
            print(stra)     
    return stra.lower()

# print(ignorespecialchar("1AMMA1%"))
check1=ignorespecialchar("Mom9 - 9Mom")

if check1==(ignorespecialchar(check1)):
    print("given str is palindrom")
else:
    print("given str is not a palindrom")


# print("number polindrome",number_polindrome(121))
# print(normal(string))
# print(check_palindrome(string))



'''SWAP'''
# def swap(a, b):
#     a, b = (a+b-a), (a+b-b)
#     print(a, b)
#     # a, b = b, a
#     return a, b
# print(swap(10, 20))


def isPalindrome(s: str) -> bool:
        print("".join([i.lower() for i in s if i.isalpha() or i.isalnum()]))
        if s==" ": return True
        org="".join([i.lower() for i in s if i.isalpha() or  i.isalnum()])
        print(org)
        print(org[::-1])
        return org==org[::-1]
print(isPalindrome("0PP"))