import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('Income data - Ex2.csv')
print(data)

import numpy as np
data.hist(column="prestige")
data.plot(y=['income','prestige'])
plt.show()
