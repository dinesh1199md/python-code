# l=[1,2,3,4,5,6,6]
# l1=[1,2,8,6,7,6,9]

# res=[]
# for i in l:
#     if i in l1:
#         res.append(i)

# print (list(set(res)))

# counter = {} 
# counter["Key"]=1
# counter["key"]=12



# def addToCounter(country): 
# 	if country in counter: 
# 		counter[country] += 1
# 	else: 
# 		counter[country] = 1

# addToCounter('China') 
# addToCounter('Japan') 
# addToCounter('china') 

# print(counter)
# print (len(counter)) 
st="dinesh"
l=[1,2,3,4,5]
t=(1,2,3,4,5,6)

print(st[slice(-1,-1,-1)])
print(l[0:3])
'''slice and modify'''
l[1:3]=[10,20,30]
print(l)

word="goodmorning"
print(word[::])