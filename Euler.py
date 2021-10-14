import math
import numpy

from NumericalMethods import NumericalMethods
class Euler(NumericalMethods):
    def __init__(self, x0,y0, b, n, n0, N):
        super().__init__( x0,y0, b, n, n0, N)
        self.x, self.y = self.calculateFunction(self.h,self.n)
        self.errorCalculation()
        self.maxErrors(self.calculateFunction)

    def calculateFunction(self,h,n):
        x = []
        y = []
        x.append(self.x0)
        y.append(self.y0)
        for i in range (1, n + 1):
            f = (y[i-1]/x[i-1]) - x[i-1]* pow(math.e, (y[i-1]/x[i-1]))
            y.append(y[i-1] + h * f)
            x.append(x[i-1] + h)
        return x,y
















