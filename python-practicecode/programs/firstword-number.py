
st="5dinehs"
print(st[0].isdigit())

print(st[:1] in '0123456789')

import  re

print(bool(re.match(r'^\s*[0-9]', st)))



# check1 = ['Learn', 'Quiz', 'Practice', 'Contribute'] 
# check2 = check1 
# check3 = check1[:] 
  
# check2[0] = 'Code'
# check3[1] = 'Mcq'
  
# count = 0
# for c in (check1, check2, check3): 
#     if c[0] == 'Code': 
#         count += 1
#     if c[1] == 'Mcq': 
#         count += 10
  
# print (count) 
# print(check1,check2,check3)

a = [1, 2, 3]
b = [7, 8, 9]

l3=[(x+y) for x,y in zip(a,b)]
l4=[(x,y) for x in a for y in b]
# print(l3)
# print(l4)

'''flating the multiple diementions'''
l=[[10,20,30],[40,50,60],[70,80,90]]
# l2=[]
# for temp in l:
#     for x in temp:
#         l2.append(x)
# print(l2)
out=[ x for temp in l for x in temp ]
print(out)


