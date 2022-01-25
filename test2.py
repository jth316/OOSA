import numpy as np
import matplotlib.pyplot as plt

filename='data1.txt'
x,y=np.loadtxt(filename, unpack=True, dtype=float,comments='#',usecols=(0,1))

plt.scatter(x, y)
plt.show()

