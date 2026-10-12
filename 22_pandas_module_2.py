import pandas as pd

# df = pd.DataFrame({
#     "Name": ["Ajay", "Vijay", "Kiran", "Sanjay"],
#     "Age": [23, 44, None, 90],
#     "Salary": [5000, 2000, 1000, None],
#     "Gender": ["Male", "male", "m", "M"]
# })
# print(df)

# Check missing values:
# print(df.isnull().sum())

# Fill missing age's with the average
# df["Age"] = df["Age"].fillna(round(df["Age"].mean(), 0))
# print(df)
# print(df.isnull().sum())

# df.drop_duplicates()
# df.duplicated().sum()


#-------------------------------------
# Grouping and Aggregation:

df = pd.DataFrame({
    "Category": ["Electronics", "Accessories", "Accessories", "Electronics", "Accessories"],
    "Price": [60000, 500, 1500, 12000, 500],
    "Quantity": [2, 10, 5, 3, 8]
})

df["Revenue"] = df["Price"] * df["Quantity"]
# print(df)

# Revenue by category:
# print(df.groupby("Category")["Revenue"].sum())

# Average Price by category:
# print(df.groupby("Category")["Price"].mean())

# Multiple Aggregations:
print(df.groupby("Category").agg({
    "Revenue": "sum",
    "Price": "mean", 
    "Quantity": "sum"
}))

