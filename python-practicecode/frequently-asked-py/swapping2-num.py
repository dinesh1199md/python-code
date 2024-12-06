
def swapnum1(num1,num2):
    print("Before swaping"+"Num1 :",num1,"Num2 :" ,num2)
    temp=num1
    num1=num2
    num2=temp
    print("After swaping "+" Num1 :",num1,"Num2 :" ,num2)
def swapnum2(num1,num2):
    print("Before swaping"+"Num1 :",num1,"Num2 :" ,num2)
    num1,num2=num2,num1
    print("After swaping "+" Num1 :",num1,"Num2 :" ,num2)    

def swapnum3(num1,num2):
    print("Before swaping"+"Num1 :",num1,"Num2 :" ,num2)
    num1=num1+num2
    num2=num1-num2
    num1=num1-num2
    print("After swaping "+" Num1 :",num1,"Num2 :" ,num2)    


swapnum1(10,20)
swapnum1(100,200)
swapnum3(100,200)