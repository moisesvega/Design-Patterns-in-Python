'''
Created on Jul 16, 2011

@author: moises
'''

'''Defines the interface of objects the factory method creates'''
class Product:
    pass

'''Implements the Product interface'''
class ConcreteProductA( Product ):
    def __init__( self ):
        self.product = "Guitar"

'''Implements the Product interface'''
class ConcreteProductB( Product ):
    def __init__( self ):
        self.product = "Drums"

'''Declares the factory method, which returns an object of type Product.
 Creator may also define a default implementation of the factory method
  that returns a default ConcreteProduct object. '''

factory = {
           "Item1" : ConcreteProductA,
           "Item2" : ConcreteProductB,
           }


