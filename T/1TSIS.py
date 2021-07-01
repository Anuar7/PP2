#Syntax
#1Ex
print("Hello World")
#2Ex
if 5 > 2:
      print("Five is greater than two!")

#Comments
#1Ex
#This is a comment
#2Ex
"""
This is a comment
written in 
more that just one line
"""

#Variables
#1Ex
carname = "Volvo"

#2Ex
x = 50

#3Ex
x = 5
y = 10
print(x + y)

#4Ex
x = 5
y = 10
z = x + y
print(z)

#5Ex
myfirst_name = "John"

#6Ex
x = y = z = "Orange"

#7Ex
def myfunc():
  global x      
  x = "fantastic"

#Data types
#1Ex
x = 5
print(type(x))

int

#2Ex
x = "Hello World"
print(type(x))

str

#3Ex
x = 20.5
print(type(x))

float

#4Ex
x = ["apple", "banana", "cherry"]
print(type(x))

list

#5Ex
x = ("apple", "banana", "cherry")
print(type(x))

tuple

#6Ex
x = {"name" : "John", "age" : 36}
print(type(x))

dict

#7Ex
x = True
print(type(x))

bool

#Numbers
#1Ex
x = 5
x = float(x)

#2EX
x = 5.5
x = int(x)

#3EX
x = 5
x = complex(x)

#Strings
#1Ex
x = "Hello World"
print(len(x))

#2Ex
txt = "Hello World"
x = txt[0]

#3EX
txt = "Hello World"
x = txt[2:5]

#4Ex
txt = " Hello World "
x = txt.strip()

#5Ex
txt = "Hello World"
txt = txt.upper()

#6Ex
txt = "Hello World"
txt = txt.lower()

#7Ex
txt = "Hello World"
txt = txt.replace("H", "J")

#8Ex
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
#Booleans
#1Ex
print(10 > 9)

True

#2Ex
print(10 == 9)

False

#3Ex
print(10 < 9)

False

#4Ex
print(bool("abc"))

True

#5Ex
print(bool(0))

False

#Operators
#1Ex
print(10 * 5)

#2Ex
print(10 / 2)

#3Ex
fruits = ["apple", "banana"]
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#4Ex
if 5 != 10: 
    print("5 and 10 is not equal")

#5Ex
if 5 == 10 or 4 == 4:
   print("At least one of the statements is true")

#Lists
#1Ex
fruits = ["apple", "banana", "cherry"]
print(fruits[1])
#2Ex
fruits = ["apple", "banana", "cherry"]
fruits[0] = "kiwi"

#3Ex
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")

#4Ex
fruits = ["apple", "banana", "cherry"]
fruits.insert(1, "lemon")

#5Ex
fruits = ["apple", "banana", "cherry"]
fruits.remove("banana")

#6Ex
fruits = ["apple", "banana", "cherry"]
print(fruits[-1])

#7Ex
fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(fruits[2:5])

#8Ex
ffruits = ["apple", "banana", "cherry"]
print(len(fruits))

#Tuples
#1Ex
fruits = ("apple", "banana", "cherry")
print(fruits[0])

#2Ex
fruits = ("apple", "banana", "cherry")
print(len(fruits))

#3Ex
fruits = ("apple", "banana", "cherry")
print(fruits[-1])

#4Ex
fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(fruits[2:5])

#Sets
#1Ex
fruits = {"apple", "banana", "cherry"}
if "apple" in fruits:
  print("Yes, apple is a fruit!")

#2Ex
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")

#3Ex
fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits)

#4Ex
fruits = {"apple", "banana", "cherry"}
fruits.remove("banana")

#5Ex
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")

#Dictionaries
#1Ex
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#2Ex
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#3Ex
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"

#4Ex
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#5Ex
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#If and Else
#1Ex
a = 50
b = 10
if a > b:
  print("Hello World")

#2Ex
a = 50
b = 10
if a != b:
  print("Hello World")

#3Ex
a = 50
b = 10
if a == b:
  print("Yes")
else:
  print("No")

#4Ex
a = 50
b = 10
if a == b:
  print("1")
elif a > b:
  print("2")
else:
  print("3")

#5Ex
if a == b and c == d:
  print("Hello")

#6Ex
if a == b or c == d:
  print("Hello")

#7Ex
if 5 > 2:
      print("Five is greater than two!")

#8Ex
if 5 > 2: print("Five is greater than two!")

#9Ex
print("Yes") if 5 > 2 else print("No")

#While loops
#1Ex
i = 1
while i < 6:
  print(i)
  i += 1

#2Ex
i = 1
while i < 6:
  if i == 3:
    break
  i += 1

#3Ex
i = 0
while i < 6:
  i += 1
  if i == 3:
    continue
  print(i)

#4Ex
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")

#For loops
#1Ex
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#2Ex
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)

#3Ex
for x in range(6):
  print(x)

#4Ex
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)

#Funvtions
#1Ex
def my_function():
  print("Hello from a function")

#2Ex
def my_function():
      print("Hello from a function")

my_function()

#3Ex
def my_function(fname, lname):
      print(fname)

#4EX
def my_function(x):
      return x + 5

#5Ex
def my_function(*kids):
  print("The youngest child is " + kids[2])

#6Ex
def my_function(**kid):
      print("His last name is " + kid["lname"])

#Lambda
#1Ex
x = lambda a : a

#Classes
#1Ex
class MyClass:
  x = 5

#2EX
class MyClass:
      x = 5
p1 = MyClass()

#3Ex
class MyClass:
      x = 5

p1 = MyClass()

print(p1.x)

#4Ex
class Person:
      def __init__(self, name, age):
    self.name = name
    self.age = age

#Inheritance
#1Ex
class Student(Person):

#2Ex
class Person:
      def __init__(self, fname):
    self.firstname = fname

  def printname(self):
    print(self.firstname)

class Student(Person):
  pass

x = Student("Mike")
x.printname()

#Modules
#1Ex
import mymodule

#2Ex
import mymodule as mx

#3Ex
import mymodule

print(dir(mymodule))

#4Ex
from mymodule import person1