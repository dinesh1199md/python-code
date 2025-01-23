"""class"""
class Dog1:
    pass

"""Object"""
class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age

#creating classs object
my_dog= Student("Dinesh",20)

"""Inheritance"""
class Animal:
    def __init__(self,name):
        self.name=name
    def sound(self):
        print("Animal sound",self.name)
    def namechec(self):
        print("name :",self.name)    
class Dog(Animal):
    def sound(self):
        print("this is sound of dog:", self.name)

obj=Dog("dog")
obj.sound()
obj.namechec()


"""encapsulation"""
class Person:
    def __init__(self,name,age,id):
        self.name=name
        self._age=age
        self.__id=id
    def get_name(self):
        print("Name :",self.name)
    def get_age(self): 
        print("age :",self._age)
    def get_id(self):
        print("id :",self.__id) 
         
obj1=Person("dinesh",25,151610530)
obj1.get_name()
obj1.get_age()
obj1.get_id()