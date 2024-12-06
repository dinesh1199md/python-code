

def amstrong(n):
    resut=str(n)
    am=0
    for i in resut:
        am=am+pow(int(i),3)
    if n==am:
        print(f"given number {n} is Amstrong")   
    else:
        print(f"given number {n} is not Amstrong")      

amstrong(153)