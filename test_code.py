import numpy as np
import pandas as pd
# Create list for {tournament place : ranking points}. This would allow different point schemes.

x = list([1000] + [600] + [360] * 2 + [180] * 4 + [90] * 8 + [45] * 16 + [25] * 32 + [10] * 64)

a = np.array(x)
b = x

for y in range(1, 6):
    np.random.shuffle(b)
    a.append(b)

print(a)

#arr = np.arange(10)
#np.random.shuffle(arr)
#arr

#for i in range(1,10):
#    print('x')
