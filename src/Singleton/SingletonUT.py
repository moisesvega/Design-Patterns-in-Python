'''
Created on Jul 15, 2011

@author: moises
'''
import unittest
import Singleton

class Test( unittest.TestCase ):


    def setUp( self ):
        self.child = Singleton.Child ( 'Moises Vega' )

    def tearDown( self ):
        self.child = None
        pass


    def testSameNameAsSetUp( self ):
        self.assertEqual( self.child.name(), 'Moises Vega' )
        print 'name: ' + self.child.name()

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
