# Linear Regression with SciKitLearn
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from sklearn.metrics import mean_squared_error, r2_score

data = pd.read_csv("housing_data.csv")
print(data.head())

#EDA of the data

print(data.describe())

#Visualize distributions

import matplotlib.pyplot as plt
plt.hist(data(['price']), color="red")
plt.title("Price based on Age of Property")
plt.ylabel("Age of Property")
plt.xlabel("Price of Property")
plt.show()

#Clean Data
#check for missing values
print(data.isnull().sum())

#Handle missing values

data = data.dropna()

#Create aa new feature "age" by subtracting year_built from current year
data['age'] = 2025 - data['year_built']

### Run a predictive model

X = data[['bedrooms', 'bathrooms', 'sqft_living', 'age']] # Features
y = data['price']  #Target variable

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

plt.scatter(y_pred, y_pred, c='r', marker='s', label="Prediction")
plt.scatter(y,y,c='b', marker='x', label="Actual")

plt.legend(loc='upper left')
plt.title("Actual vs Predicted Data")
plt.show()

#Acquire Accuracy scores
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error: ", mse)
print("R-squared: ", r2)