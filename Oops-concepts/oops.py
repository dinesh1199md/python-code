# https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-object-oriented-programming-system-oops-part-1/



class Author:  #The name of the class in Python follows Pascal Case. It is a naming convention
                # where each word starts with a capital letter without any special characters used.

    type ="freelancer" #class variables 

    def __init__(self, author_name, num_articles):
        self._author_name = author_name         #instance/object variables
        self.num_articles = num_articles
        print("Created new author object")



    def show(self):
        """This method prints the details of the author"""
        print("In show method")
        print(f"Author Name: {self.author_name}nNum of published articles: {self.num_articles}nType of Work: {Author.type}")


    def update(self, num_articles):
        """This method updates the number of published articles"""
        print("In update method")
        self.num_articles = num_articles


    def total_articles(self, draft):
        total = self.num_articles + draft  #local variables 
        print(f"Total articles are: {total}")


    @classmethod
    def return_type(cls):
        return cls.type

    @staticmethod
    def stat_method():
        print("I am a static method")


# creating instance of the classs
obj1=Author("dinesh",24)

#Accessing attributes and Calling methods
# print(obj1.author_name)
# print(obj1.num_articles)
'''Calling Methods: The two ways of calling 
methods are ClassName.method(object) or object.method()'''

# obj1.show()
# obj1.update(50)
# obj1.show()
# obj1.total_articles(10)

# Author.show(obj1)
# Author.update(obj1,50)
# Author.show(obj1)
# Author.total_articles(obj1,20)

'''calling the class method'''
# print(Author.return_type())

'''Calling Static method: ClassName.method()'''
# Author.stat_method()

'''protected'''
# print(obj1._author_name)


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def __str__(self):
        return f"Person:{self.name}, age: {self.age}"
print(Person("Dinesh",24))


#inheritance
class Animal:
    def __init__(self,name) :
        self.name=name
    def display(self):
        print(f"this is from animal {self.name}")
    def barka(self):
        print(f"{self.name} bark from base class!")     

class Dog(Animal):
    def bark(self):
        print(f"{self.name} bark!")            


# lucky=Dog("Dommy")
lucky=Animal("Dommy")    
obj2=Dog("Dommy2")
# lucky.bark()    
lucky.display()    
obj2.bark()

