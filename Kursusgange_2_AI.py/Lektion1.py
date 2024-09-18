import sys
import pandas as pd
import sklearn as sk
import matplotlib as mpl

# 1. Read Data
df = pd.read_csv(r"C:\Users\alext\Downloads\iris.csv")



# 2. Head & Tail
print("First 5 rows:")
print(df.head())
print("\nLast 5 rows:")
print(df.tail())

# 3. Info
print("\nData Information:")
df.info()

# 4. Descriptive statistics
df.describe()

# 5. Handling Missing Values
df_dropna = df.dropna()

df_fillna = df.fillna(0)  # Filling missing values with 0




# 6. Selecting Columns
selected_columns = df[['column1', 'column2']]

# 7. Filtering
filtered_df = df[df['column'] > 10]

# 8. Group By
grouped_df = df.groupby('column').agg({'column2': 'mean'})

# 9. Merge & Concatenate
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [7, 8, 9], 'B': [10, 11, 12]})

merged_df = pd.merge(df1, df2, on='A')

# 10. Applying Functions
df['new_column'] = df['column'].apply(lambda x: x * 2)
