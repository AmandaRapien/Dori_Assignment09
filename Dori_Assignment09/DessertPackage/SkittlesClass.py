#ClassSkittles.py

#We need to identify the class
class Skittles():

#This gets the price of Skittles
    def getFlavor(self):
        return self.flavor

#This sets the price of Skittles 
    def setPrice(self, price):
        self.validatePrice(price)
#This validates the price before we store it in the object
    def validatePrice(self, price):
        if price < 0: 
            print ("Skittles are not free")
        else: 
            self.price = price 
            
#This is the int
    def __init__ (self, flavor, price):  # we are ensuring that Skittles cannot be instantiated without a flavor
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
