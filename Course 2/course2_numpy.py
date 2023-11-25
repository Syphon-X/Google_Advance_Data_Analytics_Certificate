
# Introduction to NumPy / Multi-Function Arrays and Matrices
# Vectorization enables operations to be performed on multiple components of a data object at the same time.

import numpy as np  # np is aliasing
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

list_a = [1, 2, 3]
list_b = [2, 4, 6]

array_a = np.array(list_a)
array_b = np.array(list_b)

result = array_a * array_b
print(result)

# Pandas
print('----------------------------')

# Use pd.DataFrame() function to create a dataframe from a dictionary.
data = {'col1': [1, 2], 'col2': [3, 4]}
df = pd.DataFrame(data=data)
print(df)

df2 = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]), columns=['a', 'b', 'c'], index=['x', 'y', 'z'])
print(df2)

# Pandas groupby()

clothes = pd.DataFrame({'type': ['pants', 'shirt', 'shirt', 'pants', 'shirt', 'pants'],
                        'color': ['red', 'blue', 'green', 'blue', 'green', 'red'],
                        'price_usd': [20, 35, 50, 40, 100, 75],
                        'mass_g': [125, 440, 680, 200, 395, 485]})


clothes_grouped = clothes.groupby((['type', 'color'])).min()
print(clothes_grouped)
print('----------------------------')

clothes_agg = clothes[['price_usd', 'mass_g']].agg(['sum', 'mean'])
print(clothes_agg)
print('----------------------------')
# groupby() w/ agg() together
clothes_color = clothes.groupby('color').agg({'price_usd': ['mean', 'max'], 'mass_g': ['mean', 'max']})
print(clothes_color)
print('----------------------------')
# multindex example: The inputed arguments have become hierarchical indices
clothes_multindex = clothes.groupby(['color', 'type']).agg(['mean', 'min'])
print(clothes_multindex)



