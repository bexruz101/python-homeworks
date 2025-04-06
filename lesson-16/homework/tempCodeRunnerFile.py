iris_df.columns = iris_df.columns.str.lower()
sepal_df = iris_df[['sepalLength', 'sepalWidth']]
print("\nSelected Sepal Columns:")
print(sepal_df.head())