
def median(num1,num2):
    l=sorted(num1+num2)
    n=len(l)
    mid=n//2
    if n%2==0:
        median=(l[mid]+l[mid-1])/2
        return median
    else:
        median=l[mid]
        return median

num1=[1,3]
num2=[2]
print(median(num1,num2))
num1=[1,2]
num2=[3,4]
print(median(num1,num2))