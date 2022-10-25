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
#We need to identify the class
class Cupcake():

#This gets the price of a cupcake
    def getFlavor(self):
        return self.flavor
#This sets the price of a cupcake 
    def setPrice(self, price):
        self.validatePrice(price)
#This validates the price before we store it in the object
    def validatePrice(self, price):
        if price < 0: 
            print ("Cupcakes are not free")
        else: 
            self.price = price 
            
#This is the int
    def __init__ (self, flavor, price):  # we are ensuring that an cupcake cannot be instantiated without a flavor
        self.flavor = flavor # store the flavor in the current object 
        self.validatePrice(price)
    
    def __repr__(self):  # will return string representation of the object
        """
        return a string represenation of the object 
        """
        return "flavor = " + self.flavor 
    def __str__(self):  #does pretty much the same thing as repr
        """
        return a 'pretty' string presentaion of the Object
        """
        return "flavor = " + self.flavor + " price =" + str(self.price)
