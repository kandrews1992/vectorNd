class VectorError(Exception):
    pass 

class Vector(object):
    def __init__(self, *args):
        if len(args) == 0:
            self.data = [0]
        else:
            self.data = list(args)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return 
    
    def __len__(self):
        return len(self.data)
    
    def length(self):
        return self.__len__()
    
    def shape(self):
        return (self.__len__(), 1)

    def dimension(self):
        return self.shape()[0]

    def __add__(self, v):
        if self.shape() == v.shape():
            add = [a + b for a, b in zip(self.data, v.data)]
            return Vector(*add)
        else:
            raise VectorError()
    
    def __iadd__(self, v):
        if self.shape() == v.shape():
            for i in range(len(self)):
                self.data[i] += v.data[i]
            return Vector(*self)
        else:
            raise VectorError()
    
    def __sub__(self, v):
        if self.shape() == v.shape():
            sub = [a - b for a, b in zip(self.data, v.data)]
            return Vector(*sub)
        else:
            raise VectorError()
    
    def __isub__(self, v):
        if self.shape() == v.shape():
            for i in range(len(self)):
                self.data[i] -= v.data[i]
            return Vector(*self)
        else:
            raise VectorError()
    
    def dot(self, v):
        if self.shape() == v.shape():
            return sum(a * b for a, b in zip(self.data, v.data))
        else:
            raise VectorError()
    
    def inner(self, v):
        return self.dot(v)
    
    def __mul__(self, v):
        if isinstance(v, Vector):
            return self.dot(v)
        if isinstance(v, (int, float)):
            mul = [a * v for a in self.data]
            return Vector(*mul)
        else:
            raise VectorError()
    
    def __rmul__(self, v):
        return self.__mul__(v)
    
    def __iter__(self):
        return self.data.__iter__()
    
    def __getitem__(self, index):
        return self.data[index]
    
    def __setitem__(self, index, val):
        try:
            self.data[index] = val  
        except IndexError:
            raise VectorError("Index out of range")

    def __eq__(self, v):
        return self.data == v.data 
    
    def __ne__(self, v):
        return not self.__eq__(v)

    def norm(self):
        import math 
        sum = 0
        for i in range(len(self)):
            if isinstance(self.data[i], (int,float)):
                sum += self.data[i]**2
            if isinstance(self.data[i], complex):
                sum += self.data[i].real * self.data[i].imag 
        return math.sqrt(sum)
    
    def __abs__(self):
        return self.norm()
    
    def normalize(self):
        norm = self.norm()
        normed = [a/norm for a in self.data]
        return Vector(*normed) 
    