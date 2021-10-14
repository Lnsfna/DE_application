import math
import numpy

from NumericalMethods import NumericalMethods
class Euler(NumericalMethods):
    def __init__(self, x0,y0, b, n):
        super().__init__( x0,y0, b, n)
        for i in range (1, self.n + 1):
            f = (self.y[i-1]/self.x[i-1]) - self.x[i-1]* pow(math.e, (self.y[i-1]/self.x[i-1]))
            self.y.append(self.y[i-1] + self.h * f)
            self.x.append(self.x[i-1] + self.h)
        self.errorCalculation()













