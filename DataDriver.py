import numpy as np
import pandas as pd

print('hello world')
testArray = np.zeros(5, dtype = int)
print(testArray)
df = pd.read_csv("fitbit_export_20230125.csv", index_col=0)
print(df.head())