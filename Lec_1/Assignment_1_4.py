import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

num_simu = 100
num_length = 10000
simu_df = pd.DataFrame()
for i in range(num_simu):
    count = 0
    temp = np.random.normal(0, 1, size=num_length)
    temp[0]=0
    temp_df = pd.DataFrame(temp)
    res_df = temp_df.cumsum()
    simu_df[i]= (res_df.iloc[:,0].tolist())

fig = plt.figure(figsize=(12,8))
plt.plot(simu_df)
plt.title("Brownian Motion, 100 Ways")
plt.xlabel("Steps")
fig.savefig("BM.jpg")

point = simu_df.diff()
fig2 = plt.figure(figsize=(12, 8))
plt.hist(point, bins = 50)
plt.title("Increments of BM, 100 Ways")
fig2.savefig("hist.jpg")


#print(stats.kstest(point[1:], 'norm', (0, 1)))


