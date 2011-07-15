'''
Created on Jul 14, 2011

@author: moises.vega
'''

class Singleton:
    __single = None
    def __init__( self ):
        if Singleton.__single:
            raise Singleton.__single
        Singleton.__single = self

class Child( Singleton ):
    def __init__( self, name ):
        Singleton.__init__( self )
        self.__name = name
    def name( self ):
        return self.__name

class Junior( Singleton ):
    pass

def Handle( x = Singleton ):
    try:
        single = x()
    except Singleton, s:
        single = s
    return single
