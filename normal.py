import numpy as np
import matplotlib.pyplot as plt

Mean = int(input("Enter in the mean: "))

Standard_Deviation = int(input("Enter in Standard Deviation: "))

Size = int(input("Enter in size of graph: "))

data = np.random.normal(Mean, Standard_Deviation, Size)

plt.hist(data, 100)
plt.axvline(data.mean(), color = 'k', linestyle = 'dashed', linewidth = 2)
plt.show()