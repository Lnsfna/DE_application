import math
import numpy

class ExactSolution:
    def __init__(self,x0,y0,X):
        if(x0 == "" or x0 == " "):
            self.x0 = 1
        else:
            self.x0 = int(x0)
        if(y0 == "" or y0 == " "):
            self.y0 = 0
        else:
            self.y0 = int(y0)
        if (X == "" or X == " "):
            self.X = 8
        else:
            self.X = int(X)

        self.c = self.x0 - pow(math.e, -(self.y0/self.x0))
        self.x = numpy.linspace(self.x0, self.X)
        self.y = -self.x * numpy.log(self.x - self.c)






