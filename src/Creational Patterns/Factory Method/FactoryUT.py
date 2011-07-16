'''
Created on Jul 16, 2011

@author: moises
'''
import unittest
import Factory

class Test( unittest.TestCase ):


    def setUp( self ):
        self.factory = {
                   "Item1" : Factory.ConcreteProductA,
                   "Item2" : Factory.ConcreteProductB,
                   }


    def tearDown( self ):
        self.factory = None


    def testDefaultValues( self ):
        self.assertEqual( self.factory["Item1"]().product, 'Guitar' )
        self.assertEqual( self.factory["Item2"]().product, 'Drums' )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
