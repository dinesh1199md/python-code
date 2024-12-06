def addDigits(num: int) -> int:
        while(num>=9):
            num=int(str(num)[0])+int(str(num)[1])
        return num
print(addDigits(10))

