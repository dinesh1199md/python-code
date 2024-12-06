'''Symbol	Matches
+	One or More of the preceding group
*	Zero or More of preceding group
?	Zero or One of preceding group
^name	String must begin with the name
name$	String must end with the name
.	Any character except \n
{n}	Exactly n of preceding group
{n, }	>= n of preceding group
{,n}	[0, m] of preceding group
{n, m}	[n, m] of preceding group
*?	Non Greedy matching of the preceding group
[abc]	Any character enclosed in the brackets
[^abc]	Any character not enclosed in the brackets
\d, \w, \s	Digit, word, or space respectively.
\D, \W, \S	Anything except digit, word, or space respectively '''

import re

'''findall()'''
#The findall() function returns a list containing all matches.
fdstr="this dinesh salem sa , saazure with python devloper"
print(re.findall("sa",fdstr))

txt = "The rain in Spain"
x = re.findall("ai", txt)
print("findall()",x)


''' search()'''
'''The search() function searches the string for a match, and returns a Match object if there is a match.
If there is more than one match, only the first occurrence of the match will be returned:
If no matches are found, the value None is returned'''

"""The Match object has properties and methods used to retrieve information about the search, and the result:

.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function 
.group() returns the part of the string where there was a match"""

fdstr="this dinesh salem sa , saazure with python devloper"
print(re.search("ravi",fdstr))

txt = "The rain in Spain"
x = re.search("rain", txt)
print("search()",(x.group()))


'''split()'''
"""The split() function returns a list where the string has been split at each match:"""
txt = "The rain in Spain"
x = re.split("\s", txt)
print("split()",x)

"""You can control the number of occurrences by specifying the maxsplit parameter"""
txt2 = "The:rain:in:Spain"
x = re.split(":", txt2,2)
print("split()",x)


'''sub()'''
"""The sub() function replaces the matches with the text of your choice:"""

txt = "The rain in Spain"
x = re.sub("\s", "9", txt)
print("sub()",x)

"""You can control the number of replacements by specifying the count parameter"""
txt = "The rain in Spain"
x = re.sub("\s", "9", txt,2)
print("sub()",x)

'''match()'''

import re 
word1="0ab2123" 
word="ab2123" 
print(bool(re.match('^[0-9]',word1))) #starting as 0
print(bool(re.match('[A-Za-z0-9]+$',word))) #alphanum


'''Ip match code'''
def is_ip(ip):
    pattern="^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    isvalid=re.match(pattern,ip)
    tempip= ip.split(".")
    print(tempip)
    ipcount=0
    if isvalid:
        for i in tempip:
            if int(i)>=0 and int(i)<=255:
                ipcount+=1
    # if ipcount!=4:
    #     return False
    # else:
    #     return True 
    return True if ipcount==4 else False   
print("check validip",is_ip("234.45.88.77"))   
    
def is_ip2(ip):
    pattern="^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$"
    isvalid=re.match(pattern,ip)
    if isvalid:
        tempip= [int(i) for i in ip.split(".") if int(i)<=255 and int(i)>=0]
        print(tempip)
        return len(tempip)==4 if True else False
    else:
        return F"pattern mismatch",False
print(is_ip2("234.45.88"))






