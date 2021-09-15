import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

price = pd.read_csv('price.csv',index_col=0)
fig1 = plt.figure(figsize=(12, 8))
plt.plot(price)
plt.title("Stock Price")
fig1.savefig("price.jpg")


data = pd.read_csv('ret.csv', index_col=0)
data = data.fillna(0)
print(data)

fig2 = plt.figure(figsize=(12, 8))
plt.hist(data, bins = 30)
plt.title("Log Return of Stock Price")
fig2.savefig("hist2.jpg")