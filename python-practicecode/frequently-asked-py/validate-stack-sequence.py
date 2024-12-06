def validate(pushed,poped):
    stack=[]
    j=0
    for i in pushed:
        stack.append(i)
        while stack and stack[-1]==poped[j]:
            stack.pop()
            j+=1
    return stack==[]    

pushed=[1,2,3,4,5]
poped=[4,5,3,2,1]
print(validate(pushed,poped))