import numpy as np
import matplotlib.pyplot as plt
import simulating_anniling as s

x = np.linspace(-10, 10, 1000)
y = -1/89*x**2 + np.cos(x)**2 - np.sin(x*9)/5
s1 = s.SimulatingAnneling(500)
xbestlist, ybestlist = s1.algorithm()
print(xbestlist, ybestlist)

plt.plot(x,y)
plt.scatter(xbestlist, ybestlist)
plt.show()
    