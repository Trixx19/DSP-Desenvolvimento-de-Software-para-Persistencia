import pandas as pd
import numpy as np

np.array = np.array([10, 20, 30])
#print(np.array[2])

series = pd.Series(np.array, index=['a', 'b', 'c'])
print(series["b"])