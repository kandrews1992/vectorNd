from vector import Vector 
import unittest 

class TestVectorAddition(unittest.TestCase):
    def testAdd(self):
        a = Vector(2, 3, 4)
        b = Vector(5, 6, 7)
        c = a + b
        d = b + a  
        self.assertTrue(c == d)
    
    def testComplexAdd(self):
        a = Vector(complex(2,3), complex(3,4))
        b = Vector(complex(4,5), complex(2,-2))
        c = a + b 
        d = b + a 
        self.assertTrue(c == d)

class TestVectorSubtraction(unittest.TestCase):
    def testSub(self):
        a = Vector(2, 3, 4)
        b = Vector(3, 4, 6)
        c = a + b
        d = b + a 
        self.assertTrue(c == d) 

class TestVectorMultiplication(unittest.TestCase):
    pass 

class TestDotProduct(unittest.TestCase):
    def testDot(self):
        a = Vector(2, 5, 6)
        b = Vector(-1, 3, -10)
        dot = a.dot(b)
        self.assertTrue(dot == -47)
    
    def testDotComplex(self):
        a = Vector(complex(-3,1), complex(1,2))
        b = Vector(complex(1,2), complex(3,4))
        dot = a.dot(b)
        self.assertTrue(dot == complex(-10, 5))

if __name__=="__main__":
    unittest.main()