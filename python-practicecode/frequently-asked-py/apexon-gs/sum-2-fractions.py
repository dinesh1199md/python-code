def gcd(a, b):
    while b:
        a,b=b,a%b
    return a 

# Function to add two fractions 
def addFraction(num1, den1, num2, den2): 

    num3= num1*den2 + num2*den1
    den3=den1*den2

    com_d=gcd(num3,den3)
    print(com_d)

    num3//=com_d
    den3//=com_d

    return f"{num3}/{den3}"

# Driver Code 
num1 = 1; den1 = 2; 
num2 = 3; den2 = 2; 

print(num1, "/", den1, " + ", num2, "/", 
      den2, " is equal to ", end = "")
print(addFraction(num1, den1, num2, den2))