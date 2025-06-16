import pandas as pd

dataset1 = pd.read_csv("Iris.csv")
dataset1

dataset2 = pd.read_csv("cars.csv")
dataset2.head()
dataset2.info()
dataset2.describe()

# pd.merge()
# pd.concat()
# df.sort_values()
# df.groupby()
# df.agg()
# df.head()
# df.duplicated()
# duplicate rows = df[df.duplicated()]
# df.drop_duplicates()
# df.drop_duplicates(keep='last')
# df.drop_duplicates(keep='first')
# df.drop_duplicates(keep=False)