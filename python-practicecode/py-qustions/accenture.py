'''processing and threading'''
'''lamda and map, fillter'''

# 2 dict ---->> 1 dict if same key value 
# lamda 
# generator object.... yield.....iterator
# dict iterator
# recurrsion   
#file with open and without open
# sorting


'''tcs questions'''

'''
1. what is suit in python 
2. data types in python
3. functions in python
4. slicing 
5. define class and function then call the variables 
6.  
'''


'''
sorting  ---> buble sort, selection, insertion
linkedlist
stack 
queue
array
'''

class employee:
    def __init__(self,id,name):
        self.id=id
        self.name=name
    def empdetails(self): 
        print(self.name,self.id)
    def passchekc(self):
        print("inside pass block")
        pass
emp=employee(122,"Dinesh")
emp.empdetails()
emp.passchekc()
print(emp.id)



