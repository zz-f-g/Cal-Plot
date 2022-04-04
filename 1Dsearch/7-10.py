def SecantMethod(f, x1, x2, precision):
    def GetNullPoint(f, x1, x2):
        return (f(x2)*x1-f(x1)*x2)/(f(x2)-f(x1))
    PointLog = [x1, x2]
    while (abs(x2-x1)>precision*abs(x1)):
        temp = x2
        x2 = GetNullPoint(f, x1, x2)
        x1 = temp
        PointLog.append(x2)
    return PointLog

g = lambda x: (2*x-1)**2 + 4*(4-1024*x)**4 - 2
x = SecantMethod(g, 0, 1, 1e-5)
x0 = x[-1]
print("x0=%.5g,g(x0)=%.5g"%(x0, g(x0)))
