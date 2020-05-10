from vector import Vector, VectorError 
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
    pass 

class TestVectorMultiplication(unittest.TestCase):
    pass 

if __name__=="__main__":
    unittest.main()