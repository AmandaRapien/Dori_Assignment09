#main.py
from DessertPackage.CupcakeClass import *
from DessertPackage.SkittlesClass import *
from DessertPackage.BrowniesClass import *

cupcake = Cupcake("vanilla", 2)
print(cupcake.__str__())

print(cupcake.flavor) 

#Negative Test Cupcake
cupcake.setPrice(-3)
#Positive Test Cupcake
cupcake.setPrice(3)
print(cupcake.__str__())

#This gets the cupcake flavor 
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