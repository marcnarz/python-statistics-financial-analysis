import pandas as pd
import matplotlib.pyplot as plt

# read file
cmr = pd.read_csv('data/comarch.csv', index_col=0)

# read first n rows
cmr.head()

# read last n rows
cmr.tail()

# draw chart
cmr['Close'].plot()
plt.show()

# moving average 200
cmr['MA200'] = cmr['Close'].rolling(200).mean()

# draw MA200 and Close price in the chart
plt.figure(figsize=(10, 8))
cmr['MA200'].plot(label='MA200')
cmr['Close'].plot(label='Close')
plt.legend()
plt.show()

# prepare Close1
cmr['Close1'] = cmr['Close'].shift(-1)

# calculate profit
cmr['Diff'] = cmr['Close1'] - cmr['Close']

# simple trading strategy
cmr['MA50'] = cmr['Close'].rolling(50).mean()
cmr['MA200'] = cmr['Close'].rolling(200).mean()
cmr['Shape'] = [1 if cmr.loc[ei, 'MA50'] > cmr.loc[ei, 'MA200'] else 0 for ei in cmr.index]

cmr['Profit'] = [cmr.loc[ei, 'Close1'] - cmr.loc[ei, 'Close'] if cmr.loc[ei, 'Shape'] == 1 else 0 for ei in cmr.index]
cmr['Profit'].plot()
plt.axhline(y=0, color='red')
plt.show()

cmr['Wealth'] = cmr['Profit'].cumsum()

cmr.tail()

cmr['Wealth'].plot()
plt.show()