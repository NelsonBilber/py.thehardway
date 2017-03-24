
# coding: utf-8

# In[8]:

# python the hardway https://learnpythonthehardway.org/book/index.html

# Exercise 1 - Hello world
import sys
print ("Hello Snake")


# In[13]:

# Exercise 2 - simple math operations
 
print ("5 + 2 = ", 5 + 2)
print ("5 > 2 ? ", 5 > 2)
print ("7 / 4 = ", 7/4)
# print ("7 % 4 = ", 7%4)


# In[2]:

# Exercise 3 - variables and names

my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print ("Let's talk about %s." % my_name)
print ("He's %d inches tall." % my_height)
print ("He's %d pounds heavy." % my_weight)
print ("Actually that's not too heavy.")
print ("He's got %s eyes and %s hair." % (my_eyes, my_hair))
print ("His teeth are usually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get it exactly right
print ("If I add %d, %d, and %d I get %d." % ( my_age, my_height, my_weight, my_age + my_height + my_weight))


# In[8]:

# Exercise 4 - input from console
   
age = input()
print ("What's your age ? ", age)


# In[4]:

#Exercise 13 using parameters

from sys import argv

program_name = argv
print ("second = ", program_name)


# In[23]:

# Exercise 15 - Read files

from sys import argv

file = open("t.txt","r")
for line in file:
    print(line.rstrip())
file.close()


# In[26]:

# Exercise 16 - Write file

from sys import argv

file = open("t.txt","r")
out = open("t2.txt","w")
for line in file:
    out_line = line.rstrip()
    print (out_line)
    out.write(out_line)
file.close()


# In[34]:

#Exercise 18 -  functions

def print_two(*args):
    arg1, arg2 = args
    print ("arg1: %r, arg2: %r" % (arg1, arg2))
   
def print_twoV2(arg1, arg2):
    print ("arg1: %r, arg2: %r" % (arg1, arg2))
    
print_two("Zed", "Ned")    
print_twoV2("Zed", "Ned")


# In[37]:

# Exercise 19 - functions continue ...

def add(num1, num2):
    return (num1 + num2)

print (add(1,2))
print (add(5+5,10+10))
    


# In[41]:

# Exercise 28 - Booleans

True and True
False and True
"test" == "test"
3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))


# In[51]:

#Exercise 29 - If conditions

people = 30
cars = 40
trucks = 15

if cars > people:
    print ("We should take the cars.")
elif cars < people:
    print ("We should not take the cars.")
else:
    print ("We can't decide.")
    


# In[56]:

# Exercise 32 - Loop and List

numbers = [1, 2, 3]
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for num in numbers:
    print (num)
    
for i in change:
    print("I got %r" % i)


# In[61]:

# Exercise 33 -  while loops
i = 0
numbers = []

while i < 6:
    print ("At the top i is %d" % i)
    numbers.append(i)

    i = i + 1
    print ("Numbers now: ", numbers)
    print ("At the bottom i is %d" % i)


print ("The numbers: ")

for num in numbers:
    print (num)


# In[63]:

# Exercise 34 - access list elems

animals = ['bear', "wolf"]

animals[1]


# In[73]:

# Exercise 39 -  Dictionaries

stuff = {'name': 'Nelson',  'age' : 33}

print (stuff['name'])

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

print (states)

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

print ("Testing ....", cities[states['California']])


# print every state abbreviation
for state, abbrev in states.items():
    print ("%s is abbreviated %s" % (state, abbrev))


# In[77]:

# Exercise 40 - Object Oriented Programming

class Song(object):
    def __init__(self,lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)
            
happy_bday = Song(["tada ttttt tada ..."])            

happy_bday.sing_me_a_song()



# In[79]:

## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## ??
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name

## ??
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

## ??
class Fish(object):
    pass

## ??
class Salmon(Fish):
    pass

## ??
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

## ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()


# In[85]:

# Exercise 44 - Inheritance vs Composition



#Implicit ineritance
class Parent(object):

    def implicit(self):
        print ("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()



#Override explicit
class Parent(object):

    def override(self):
        print ("PARENT override()")

class Child(Parent):

    def override(self):
        print ("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()


# Altered 

class Parent(object):

    def altered(self):
        print ("PARENT altered()")

class Child(Parent):

    def altered(self):
        print ("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print ("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()


# In[5]:

# Exercise 47 - Automated Testing

from nose.tools import *

class Room(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}
        
    def go(self, direction):
        return self.paths.get(direction, None)
    
    def add_paths(self, paths):
        self.paths.update(paths)
        
        
def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a
                door to the north.""")
    
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})
    
