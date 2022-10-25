'''
Created on Oct 24, 2022
Name: Amanda Rapien, Aaron Paulson, Ben Truax, Matthew Lamb
email: Lambmj@mail.uc.edu, rapienaa@mail.uc.edu, paulsoar@mail.uc.edu,truaxbp@mail.uc.edu
Assignment: Assignment 09
Course: IS 4010
Semester/Year: Fall 2022
Brief Description: This project demonstrates that we can develop an Eclipse project 
modeling something in the real world, and collaborate on GitHub.
Citations: N/A
Anything else that's relevant:
'''
from DessertPackage.CupcakeClass import *
from DessertPackage.SkittlesClass import *
from DessertPackage.BrowniesClass import *

cupcake = Cupcake("vanilla", 2)
print(cupcake.__str__())

print(cupcake.flavor) 

#Negative Test
cupcake.setPrice(-3)
#Positive Test
cupcake.setPrice(3)
print(cupcake.__str__())

#This gets the flavor 
cupcake.getFlavor()
print(cupcake.flavor)

skittles = Skittles("Original", 2)
print(skittles.__str__())

print(skittles.flavor) 

#Negative Test
skittles.setPrice(-3)
#Positive Test
skittles.setPrice(3)
print(skittles.__str__())

#This gets the flavor 
skittles.getFlavor()
print(skittles.flavor)

brownies = Brownies("Chocolate", 2)
print(brownies.__str__())

print(brownies.flavor) 

#Negative Test
brownies.setPrice(-3)
#Positive Test
brownies.setPrice(3)
print(brownies.__str__())

#This gets the flavor 
brownies.getFlavor()
print(brownies.flavor)