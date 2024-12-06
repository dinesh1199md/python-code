def leafyear(y):
    if y%400==0 and y%100==0:
        return f"{y}: is Leap year"
    elif(y%400==0 and y%100!=0):
        return f"{y}: is Leap year"
    else:
        return f"{y}: not a is Leap year"
    
print(leafyear(2000))
