'''
Load and Explore the Data
'''
#Import the required Python library and load dataset.
import pandas as pd
df = pd.read_csv("house_prices.csv")

#Display the First 5 Rows
df.head()

# Display column names and data types
df.info()

# Summary statistics of numerical columns
df.describe()

# Observe data types of df
df.dtypes

'''
Data Preprocessing
'''
#Show where and how many missing values are in data set
df.isnull()
df.isnull().sum()

# Fill missing values in “condition” with median
the_median = df["condition"].median()
df["condition"].fillna(the_median, inplace=True)

# Show dataframe with filled values in “condition”
df
df.describe()

# Select relevant features and target variable
df['age'] = df['date'] - df['yr_built']
X = df[['sqft_living', 'bedrooms', 'bathrooms','age']]
y = df['price']

# One-hot encoding for 'condition' feature
from sklearn.preprocessing import OneHotEncoder
df_encoded = pd.get_dummies(df, columns=['condition'])

# Show dataframe with one-hot encoding
df = pd.concat([df, df_encoded], axis=1)
df

#Split the Data
from sklearn.model_selection import train_test_split

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

'''
Build and Train a Linear Regression Model
'''
#Import LinearRegression from sklearn.linear_model. 
from sklearn.linear_model import LinearRegression

'''
Make Predictions and Evaluate the Model
'''
# Create an instance of the LinearRegression model
model = LinearRegression()

# Fit the model to the training data
model.fit(X_train, y_train)

#Use the trained model to make predictions on the testing data. Make predictions on the test set
y_pred = model.predict(X_test)
print(y_pred)

#Evaluate the Model. Calculate the Mean Squared Error (MSE) as mse and R-squared value as r_squared to evaluate the model's performance. 

from sklearn.metrics import mean_squared_error, r2_score

# Calculate MSE and R-squared
mse = mean_squared_error(y_test, y_pred)
r_squared = r2_score(y_test, y_pred)

print(f"(MSE): {mse}")
print(f"R-squared: {r_squared}")

'''
Experiment with a Different Regression Algorithm DecisionTreeRegressor or RandomForestRegressor
'''

from sklearn.tree import DecisionTreeRegressor

# Create and train a DecisionTreeRegressor
model2 = DecisionTreeRegressor()
model2.fit(X_train, y_train)
y_pred2 = model2.predict(X_test)

# Evaluate the DecisionTreeRegressor
tree_mse = mean_squared_error(y_test, y_pred2)
tree_r2 = r2_score(y_test, y_pred2)

# Print to check results
print(f"DecisionTreeRegressor Mean Squared Error (MSE): {tree_mse}")
print(f"DecisionTreeRegressor R-squared: {tree_r2}")