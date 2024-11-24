import matplotlib.pyplot as plt
import numpy as np

x = int(input("Enter in the highest degree value for your function: "))
values = []
for i in range(x):
    nums = int(input("Enter Coefficient(in order from highest to lowest degree) "))
    values.append(nums)

x = int(input("Enter Left Bound "))
y = int(input("Enter Right Bound "))
z = int(input("Enter The Spacing "))

p = np.poly1d(values)
x = np.linspace(x, y, z)
y = p(x)
plt.plot(x, y)
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title("Your Graph")
plt.grid(True)
plt.show()