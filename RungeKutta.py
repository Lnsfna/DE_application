import math
import numpy
from NumericalMethods import NumericalMethods

class RungeKutta(NumericalMethods):
    def __init__(self, x0, y0, b, n):
        super().__init__(x0, y0, b, n)
        for i in range (1, self.n + 1):
            f1 = (self.y[i-1]/self.x[i-1]) - self.x[i-1]* pow(math.e, (self.y[i-1]/self.x[i-1]))
            f2 = ((self.y[i-1] + (self.h / 2) * f1)/ (self.x[i-1] + (self.h /2))) - (self.x[i-1] + (self.h /2)) *\
                 pow(math.e, ((self.y[i-1] + (self.h / 2) * f1)/ (self.x[i-1] + (self.h /2))))
            f3 = ((self.y[i - 1] + (self.h / 2) * f2) / (self.x[i - 1] + (self.h / 2))) - (self.x[i - 1] + (self.h / 2)) * \
                 pow(math.e, ((self.y[i - 1] + (self.h / 2) * f2) / (self.x[i - 1] + (self.h / 2))))
            f4 = ((self.y[i - 1] + self.h * f3) / (self.x[i - 1] + self.h )) - (self.x[i - 1] + self.h) * \
                 pow(math.e, ((self.y[i - 1] + self.h * f3) / (self.x[i - 1] + self.h )))

            self.y.append(self.y[i-1] + (self.h / 6) * (f1 + 2*f2 + 2*f3 + f4))
            self.x.append(self.x[i-1] + self.h)
        self.errorCalculation()


