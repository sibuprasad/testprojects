class shape:

    def area(self):
        pass

    def perimeter(self):
        pass


class circle(shape):

    def __init__(self,r):
        self.r = r

    def area(self):
        return ((22/7) * (self.r**2))

    def perimeter(self):
        return (2*(22/7)*self.r)


class rectangle(shape):

    def __init__(self,l,b):
        self.l=l
        self.b=b

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return (2 * (self.l + self.b))