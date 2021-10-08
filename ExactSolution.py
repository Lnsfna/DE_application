import math
import numpy

class ExactSolution:
    def __init__(self,x0 = None,y0 = None):
        if(x0 == "" or x0 == " "):
            self.x0 = 1
        else:
            self.x0 = int(x0)
        if(y0 == "" or y0 == " "):
            self.y0 = 0
        else:
            self.y0 = int(y0)
        self.c = self.x0 - pow(math.e, -(self.y0/self.x0))

        x = numpy.linspace(1, 8)
        self.x = numpy.linspace(1, 8)
        self.y = x * numpy.log(x - self.c)






