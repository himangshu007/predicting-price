import pandas as pd

data = pd.read_csv('test.csv')
print(data.head())

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(data[['Version ']] , data[['Price']])
print(model.predict([[14]]))
