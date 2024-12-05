from scipy.stats import poisson
import numpy as np
import matplotlib.pyplot as plt

x = int(input("Enter X-Axis Left Bound: "))
y = int(input("Enter X-Axis Right Bound: "))

array = np.arange(x, y, 0.5)

mu = int(input("Enter in mu: "))
loc = int(input("Enter in location: "))

graph = poisson.pmf(array, mu, loc)
plt.plot(array, graph)
plt.show()