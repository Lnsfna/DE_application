import math
import numpy

class Euler:
    def __init__(self, x0,y0, b, n):
        if(x0 == ""):
            self.a = 1
        else:
            self.a = int(x0)
        if (b == "" or b == " "):
            self.b = 8
        else:
            self.b = int(b)
        if (n == ""):
            self.n = 8
        else:
            self.n = int(n)
        if (x0 == ""):
            self.x0 = 1
        else:
            self.x0 = int(x0)
        if (y0 == ""):
            self.y0 = 0
        else:
            self.y0 = int(y0)

        self.h = (self.b - self.a) / self.n
        self.x = []
        self.y = []
        self.x.append(self.x0)
        self.y.append(self.y0)
        for i in range (1, self.n + 1):
            f = (self.y[i-1]/self.x[i-1]) - self.x[i-1]* pow(math.e, (self.y[i-1]/self.x[i-1]))
            self.y.append(self.y[i-1] + self.h * f)
            self.x.append(self.x[i-1] + self.h)








