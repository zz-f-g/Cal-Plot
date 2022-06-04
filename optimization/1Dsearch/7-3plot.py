from math import log,e
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return 8*e**(1-x) + 7*log(x)

x = np.linspace(1,2,100)
y = list(map(f,x))
fig,ax = plt.subplots(figsize=(8,6),dpi=300)
ax.plot(x,y)
ax.set_xlim([1,2])
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
plt.show()