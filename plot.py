import matplotlib.pyplot as plt
import numpy as np

a = int(input("Enter Number "))
b = int(input("Enter Number "))
c = int(input("Enter Number "))

x = int(input("Enter Left Bound "))
y = int(input("Enter Right Bound "))
z = int(input("Enter The Spacing "))

p = np.poly1d([a, b, c])
x = np.linspace(x, y, z)
y = p(x)
plt.plot(x, y)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title("Your Graph")
plt.grid(True)
plt.show()