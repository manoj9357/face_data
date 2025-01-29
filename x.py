import requests

base_url=f"https://pokeapi.co/api/v2/"

def get_pokemon_info():
    url=f"https://cat-fact.herokuapp.com/facts/"
    response=requests.get(url)
    print(response)

get_pokemon_info()


##Multithreading

# import threading
# import time

# def walk_dog():
#     time.sleep(8)
#     print("dog walked")

# def throw_trash():
#     time.sleep(2)
#     print("trash thrown")

# def get_mail():
#     time.sleep(4)
#     print("mail received")

# # walk_dog()
# # throw_trash()
# # get_mail()

# chore1=threading.Thread(target=walk_dog)
# chore1.start()

# chore2=threading.Thread(target=throw_trash)
# chore2.start()

# chore3=threading.Thread(target=get_mail)
# chore3.start()

# chore1.join()
# chore2.join()
# chore3.join()

# print("all activities are completed")



# import datetime
# date=datetime.date(2025,9,11)
# today=datetime.date.today()
# time=datetime.time(12,30,0)
# now=datetime.datetime.now()
# now=now.strftime("%H:%M:%S %m-%d-%y")
# target=datetime.datetime(2030,12,13,2,12,3 )
# print(target)



# import json
# import csv
# file_path="y.txt"
# file_path="y.csv"

# with open(file_path,"r") as file:
#     content=file.read()
#     print(content)
# with open(file_path,"r") as file:
#     content=json.load(file)
#     print(content["name"])
# with open(file_path,"r") as file:
#     content=csv.reader(file)
#     for line in content:
#         print(line[0])

# if __name__=="__main__":
#     print("manoj")


###writing files

# text_data="I like me"
# # employees=["m","a","n"]
# # employees={"name":"m",
# #            "age":6,
# #            "job":"cook"}
# employees=[["name","age","job"],
#            ["m",35,"cook"],
#            ["a",67,"manager"]]
# # file_path="y.py"
# # file_path="y.json"
# file_path="y.csv"

# # import json
# import csv
# try:
#     with open(file_path,"w",newline="") as file:
#         writer=csv.writer(file)
#         for row in employees:
#             writer.writerow(row)
#         # for employee in employees:
#             # file.write(employee+" ")
#         # json.dump(employees,file,indent=4)
#         print(f"'{file_path}' created")
# except FileExistsError:
#     print(f"{file_path} not created")


###file detection


# import os

# # file_path="C:\\Users\\MPradha8\\OneDrive - JNJ\Desktop\\DOCS\\manoj.py"
# file_path="C:/Users/MPradha8/OneDrive - JNJ/Desktop/DOCS"
# # file_path="manoj.py"

# if os.path.exists(file_path):
#     print(f"loc exists ")
#     if os.path.isfile(file_path):
#         print("it is a file")
#     elif os.path.isdir(file_path):
#         print("it is a directory/folder")
# else:
#     print("not exist")



# try:
#     x=int(input("enter a number: "))
#     print(1/x)
# except ZeroDivisionError:
#     print("0 not allowed")
# except ValueError:
#     print("integer only") 
# except Exception:
#     print("something went wrong")  
# finally:
#     print("Do some clean up")      
   




# 1/0
# 1+"1"
# int("p")


##decorator
# def add_sprinkles(func):
#     def wrapper(*args, **kwargs):
#         print("you added sprinkles")
#         func(*args, **kwargs)
#     return wrapper
# def add_fudge(func):
#     def wrapper(*args, **kwargs):
#         print("you added fudge")
#         func(*args, **kwargs)
#     return wrapper
    
# @add_sprinkles
# @add_fudge
# def get_ice_cream(flavour):
#     print(f"here is your {flavour} ice cream")

# get_ice_cream("vanilla")



##@property
# class Rectangle:
#     def __init__(self,width,height):
#         self._width=width
#         self._height=height
#     @property
#     def width(self):
#         return f"{self._width:.1f}cm"
#     @width.setter
#     def width(self,new_width):
#         if new_width>0:
#             self._width=new_width
#         else:
#             print("width could not be 0 or less")

#     @width.deleter
#     def width(self):
#         del self._width
#         print("width is deleted")
# rect=Rectangle(3,4)
# print(rect.width)
# rect.width=-1
# print(rect.width)
# rect.width=6
# print(rect.width)
# del rect.width


# #Magic Methods
# class Book:
#     def __init__(self,title,author,pages):
#         self.title=title
#         self.author=author
#         self.pages=pages
#     def __str__(self):
#         return f"'{self.title}' by {self.author}"
#     def __eq__(self,other):
#         return self.title==other.title and self.author==other.author
#     def __lt__(self,other):
#         return self.pages<other.pages
#     def __gt__(self,other):
#         return self.pages>other.pages
#     def __add__(self,other):
#         return f"{self.pages+other.pages} pages"
#     def __contains__(self,keyword):
#         return keyword in self.title or keyword in self.author
#     def __getitem__(self,key):
#         if key=='title':
#             return self.title
#         elif key=='author':
#             return self.author
#         elif key=='pages':
#             return self.pages
#         else:
#             return f"key not found"
    
    
# book1=Book("th","tkr",172)
# book4=Book("th","tkr",72)
# book2=Book("wg","sjs",93)
# book3=Book("yu","se",210)

# print(book1.pages)
# print(book1)
# print(book1==book4)
# print(book1==book2)
# print(book2<book1)
# print(book1>book2)
# print(book1+book2)
# print("tk" in book1)
# print(book1['title'])
# print(book4['pages'])
# print(book3['author'])
# print(book1['audio'])







##classmethod
# class Student:
#     count=0
#     total_gpa=0
#     def __init__(self,name,gpa):
#         self.name=name
#         self.gpa=gpa
#         Student.count += 1
#         Student.total_gpa += gpa
#     def get_info(self):
#         return f"{self.name}{"'s gpa is":^25}{self.gpa}"
#     @classmethod
#     def get_count(cls):
#         return f"{cls.count}"
#     @classmethod
#     def get_avg(cls):
#         return f"{cls.total_gpa/cls.count:.2f}"

# student1=Student("Manoj",7.9)
# student2=Student("rahul",6.9)
# student3=Student("srinjoy",5.9)

# print(student1.get_info())
# print(student1.count)
# print(student1.get_count())
# print(Student.get_count())
# print(Student.get_avg())



##Static Method
# class Employee:
#     def __init__(self,name,position):
#         self.name=name
#         self.position=position
#     def get_info(self):
#         return f"{self.name}={self.position}"
#     @staticmethod
#     def is_valid_position(position):
#         valid_positions=["manager","cook","cashier","janitor"]
#         return position in valid_positions
# employee1=Employee("nugene","Manager")
# print(employee1.get_info())
# print(Employee.is_valid_position("cook"))


##Duck typing
# class Animal:
#     alive=True
# class Dog(Animal):
#     def speak(self):
#         print("woof")

# class Cat(Animal):
#     def speak(self):
#         print("meow")
# # animals=[Dog(),Cat()]

# # for animal in animals:
# #     animal.speak()

# # class Car:
# #     alive=False
# #     def horn(self):
# #         print("Honk")

# # animals=[Dog(),Cat(),Car()]

# # for animal in animals:
# #     animal.speak()
# class Car:
#     alive=False
#     # def horn(self):
#     def speak(self):
#         print("Honk")
# animals=[Dog(),Cat(),Car()]

# for animal in animals:
#     animal.speak()
#     print(animal.alive)        


##Polymorphism
# from abc import ABC, abstractmethod

# class Shape:
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self,radius):
#         self.radius=radius
#     def area(self):
#         return 3.14 * self.radius ** 2

# class Square(Shape):
#     def __init__(self,width):
#         self.width=width
#     def area(self):
#         return self.width ** 2
# class Pizza(Circle):
#     def __init__(self,topping,radius):
#         self.topping=topping
#         super().__init__(radius)

# shapes=[Circle(4),Square(5),Pizza("pepperoni",5)]

# for shape in shapes:
#     print(f"{shape.area()} cm^2")




##Super()
# class Shape:
#     def __init__(self,color,is_filled):
#         self.color=color
#         self.is_filled=is_filled
#     def desc(self):
#         print(f"it is {self.color} and {"filled" if self.is_filled else "not filled"}")
# class Circle(Shape):
#     def __init__(self,color,is_filled,radius):
#         super().__init__(color,is_filled)
#         self.radius=radius

#     def desc(self):
#         super().desc()
#         print(f"it is a circle anf the area is {3.14 * self.radius * self.radius}")


# circle=Circle(color="red",is_filled=True,radius=5)

# print(circle.radius)
# circle.desc()




# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def eat(self):
#         print(f"{self.name} is eating")
# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} Woof!")
    

# dog=Dog("scooby")
# print(dog.name)
# dog.eat()
# dog.speak()

# class Student:
#     class_year=2024
#     num_of_std=0
#     def __init__(self,name):
#         self.name=name
#         Student.num_of_std += 1

# std1=Student("manoj")
# print(std1.name)
# print(Student.num_of_std)
# std1=Student("manoj")
# print(Student.num_of_std)



# for x in range(5,0,-1):
#     print(x,end="")

# class Car:
#     def __init__(self,model,year,color,for_sale):
#         self.model=model
#         self.year=year
#         self.color=color
#         self.for_sale=for_sale

#     def drive(self):
#         print(f"drive {self.color} {self.model}")

#     def stop(self):
#         print(f"stop {self.color} {self.model}")

# car1=Car("mustang",2024,"red",False)
# car2=Car("ford",2025,"blue",True)
# car1.drive()

# print(car1.model)
# print(car2.color)




# print(f"{"Order":^26}")
# print(help(str),end=" ")



# class Car:



# from manoj import *
# favourite_food("chawal")




# import manoj

# print(manoj.pi)
# print(manoj.square(2))
# print(manoj.cube(2))
# print(manoj.circumference(2))
# print(manoj.area(2))

# print(help("manoj"))



# def is_weekend(day):
#     day=day.lower()
#     match day:
#         case "monday"|"tuesday"|"wednesday"|"thursday"|"friday":
#             return False
#         case "saturday"|"sunday":
#             return True
#         case _:
#             return False
# print(is_weekend("Saturday"))




# x=[1,2,3,4,5,7,9]

# x=[n for n in x if n%2==0]
# print(x)




# x={'A':(1,2),'B':2,'C':3,'D':4}
# for l in x:
#     print(f"{l}={x[l]}")

# print(x[A][0])
# x.update({'F':1})
# x.pop("A ")
# print(x)
# for a in x:
#     print(a)
# a=1
# b=2
# c="fgg"
# print(a,b,c,c+"2",a+b)

# def add(*nums):
#     total=0
#     for num in nums:
#         total=total+num
#     return total
# print(add(2,272,98262,733))

# def print_add(*args,**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
#     print()
#     print(f"{kwargs.get("street")},{kwargs.get("city")}")
#     print()
#     for arg in args:
#         print(arg,end=" ")
    
# print_add("Manoj",
# "kumar",
# "pradhan",
# street="bhimpura",
# city="balasore",
# state="odisha")





# def hello(greet,title,last,first="bro"):
#     print(f"{greet} {title} {first} {last}")
# hello("hello","mr","code","manoj")





# import time
# def count(end,start=0):
#     for x in range(start,end+1):
#         print(x)
#         time.sleep(1)
#     print("done")
# count(30,15)


# def net_price(list_price,discount=0,tax=0.05):
#     return list_price*(1-discount)*(1+tax)
# print(net_price(500,tax=0))




# def create_name(first,last):
#     first=first.capitalize()
#     last=last.capitalize()
#     return first+" "+last
# print(create_name("bro","code"))


# def h_b(name,age):
#     print(f"{name},{age}")
# h_b("bro",20)
# def add(x,y):
#     z=x+y
#     return z
# l=add(5,10)
# print(l)



# import random
# print(random.randint(1,6))

# print(random.random())
# options=('rock','paper','scissors')
# print(random.choice(options))
# cards=['2','3','4','5','6','7','8','9','10','k','j','q','a']
# random.shuffle(cards)
# print(cards)
# print(cards)

# capitals=       {'us':'wdc',
#                 'in':'nd',
#                 'ch':'b',
#                 'ru':'mo'}
# items=capitals.items()
# print(items)
# for key,value in capitals.items():
#     print(f"{key}:{value}")





# capitals=       {'us':'wdc',
#                 'in':'nd',
#                 'ch':'b',
#                 'ru':'mo'}

# print(capitals.get('us'))
# print(capitals.get('ja'))
# capitals.update({'ge':'be'})
# capitals.pop('ch')
# capitals.popitem()
# capitals.clear()
# keys=capitals.keys()
# print(keys)
# print(capitals)
# for key in capitals.keys():
#     print(key,end=' ')
# values=capitals.values()
# print(values)
# for value in capitals.values():
#     print(value,end=' ')








# fruits=["apple","orange","banana","coconut","coconut"]
# veg=['potato','tomato','onion']
# meat=['chicken','mutton','fish']
# groceries=[fruits,veg,meat]
# print(groceries[0][0])

# groceries=[["apple","orange","banana","coconut","coconut"],
# ['potato','tomato','onion'],
# ['chicken','mutton','fish']]
# print(groceries)
# for collection in groceries:
#     for food in collection:
#         print(food,end=' ')
#     print()
    # print(collection)


# print(fruits)
# print(len(fruits))
# print(fruits.index("apple"))
# fruits.remove("orange")
# fruits.pop()
# fruits.clear()
# print(fruits.index("coconut"))
# print(fruits.count("banana"))

# print(fruits[0])
# print(fruits[::2])
# print(fruits[::-1])
# print(len(fruits))
# print('apple' in fruits)
# # fruits[1]="pineapple"

# print(fruits)
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0,"pear")
# print(len(fruits))
# fruits.sort()
# fruits.reverse()
# # fruits.clear()
# fruits.index("ap")
# print(fruits)

# x=13
# y=bin(x)[2:]
# print(y)
# x="Manoj Kumar Pradhan"
# t=[]
# for l in x:
#     t.append(l)
# print(t)

# print(x.index("a"))
# y=enumerate(x)
# print(y)
# for idx,char in enumerate(x):
    # print(f"{idx},{char}")
    # t.append[char,]
#     t.append(idx)
# print(t)



# for x in reversed(range(11)):
#     print(x,end=" ")
# print()
# for x in range(11):
#     print(x,end=" ")
# import time
# for x in range(10,0,-1):
#     print(x)
#     time.sleep(1)
# print("times up")
# h=int(3601/3600)
# m=int(3601/60)%60
# s=3601%60

# print(f"{h:02}:{m:02}:{s:02}")

# for x in range(3):
#     for y in range(1,11):
#         print(y,end=" ")
#     print()