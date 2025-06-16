import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Sample data
data = {'category': [1, 3, 5, 2, 4, 1, 2]}
df = pd.DataFrame(data)

# Initialize OneHotEncoder
encoder = OneHotEncoder(categories=[[1, 2, 3, 4, 5]], sparse_output=False)

# Fit and transform the data
encoded_data = encoder.fit_transform(df[['category']])

# Create a new DataFrame with the encoded values
encoded_df = pd.DataFrame(encoded_data, columns=['category_1', 'category_2', 'category_3', 'category_4', 'category_5'])

# Concatenate the encoded data with the original DataFrame (optional)
df = pd.concat([df, encoded_df], axis=1)

print(df)