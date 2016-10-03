

# Singleton class which can be inherited from into other classes in which Singleton d.p. is to be applied.
class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls.instance = None

    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args, **kw)
        return cls.instance

# We specify the __metaclass__ of our class implementing the singleton design pattern. 
class MyClass(object):
    __metaclass__ = Singleton

    attrib1 = ""
    attrib2 = 0

    def function1(self):
        pass

    def function2(self):
        pass

# Test if the Singleton pattern has worked
if __name__ == '__main__':
    # instantiate object A
    objA = MyClass()

    # instantiate object B
    objB = MyClass()

    # investigate the memory address of two objects
    print "Object A = %d" % (id(objA))
    print "Object B = %d" % (id(objB))

    # determine if they are the same instance
    '''
         When you run this code, you should see that both memory addresses are equivalent, and "Same" 
         is printed out as a result, indicating that the Singleton design pattern has been successfully implemented.
    '''
    if id(objA) == id(objB):
        print "Same"
    else:
        print "Different"