import math

import numpy


class NumericalMethods:
    def __init__(self, x0,y0, b, n, n0, N):
        if(x0 == ""):
            self.a = 1
            self.x0 = 1
        else:
            self.a = int(x0)
            self.x0 = int(x0)
        if (b == "" or b == " "):
            self.b = 8
        else:
            self.b = int(b)
        if (n == ""):
            self.n = 10
        else:
            self.n = int(n)
        if (y0 == ""):
            self.y0 = 0
        else:
            self.y0 = int(y0)
        if (n0 == ""):
            self.n0 = 1
        else:
            self.n0 = int(n0)
        if (N == ""):
            self.N = 10
        else:
            self.N = int(N)

        self.h = (self.b - self.a) / self.n
        self.x = []
        self.y = []
        self.x.append(self.x0)
        self.y.append(self.y0)
        self.t = []
        self.t.append(0)
        self.max_t = []
        self.maxErrors_x = range(self.n0, self.N + 1)


    def errorCalculation(self):
        c = self.x0 - pow(math.e, -(self.y0 / self.x0))
        for i in range(self.n):
            t = abs((-1*self.x[i+1] * numpy.log(self.x[i+1] - c)) - self.y[i+1] - self.h * (self.y[i+1]/self.x[i+1]) - self.x[i+1]* pow(math.e, (self.y[i+1]/self.x[i+1])))
            self.t.append(t)

    def maxErrors(self,f):
        c = self.x0 - pow(math.e, -(self.y0 / self.x0))
        for j in range (self.n0, self.N + 1):
            a = []
            h = (self.b - self.a) / j
            x, y = f(h,j)
            for i in range(j + 1):
                t = abs((-1*x[i] * numpy.log(x[i] - c)) - y[i] - h * (y[i]/x[i]) - x[i]* pow(math.e, (y[i]/x[i])))
                a.append(t)
            self.max_t.append(max(a))



