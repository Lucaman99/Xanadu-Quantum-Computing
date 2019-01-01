import numpy as np
import strawberryfields as sf
from strawberryfields.ops import *
from matplotlib import pyplot as plt

data_set = []
y_values = [0, 0, 0, 0, 0]

x_values = [0, 1, 2, 3, 4]

def run():
    eng, q = sf.Engine(4, hbar=0.5)

    with eng:
        Coherent(1+0j) | q[0]
        Measure | q[0]

    state = eng.run('fock', cutoff_dim=5)

    return q[0]

for i in range (0, 1000):
    data_set.append(run().val)

for k in range (0, len(data_set)):
    if (int(data_set[k]) < 5):
        y_values[int(data_set[k])] = y_values[int(data_set[k])] + 1

plt.title('Graph 1')
plt.bar(x_values, y_values)
plt.show()
