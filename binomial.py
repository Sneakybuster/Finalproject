import scipy.stats as stats
import matplotlib.pyplot as plt
import numpy as np

n = int(input("Number of Successes: "))
p = int(input("Probability: "))
x = np.arange(0, n + 1)
pmf = stats.binom.pmf(x, n, p)

plt.bar(x, pmf)
plt.xlabel('Number of Successes')
plt.ylabel('Probability')
plt.title('Binomial Distribution (n={}, p={})'.format(n, p))
plt.show()