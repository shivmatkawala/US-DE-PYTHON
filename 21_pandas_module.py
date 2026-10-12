# Pandas:
    # Used for tabular data analysis
    # Works with labelled rows and columns
    # Great for CSV, Excel, Any business dataset

import pandas as pd

    # Series:
        # One Diamensional labeled data
s = pd.Series([1, 2, 3, 4, 5 ,6])
# print(s)
# print(type(s))

    # Dataframe:
        # Two diamensional tabular data

df = pd.DataFrame({
    "Name": ["Amisha", "Naga", "Harsh", "Beniwal"],
    "Marks": [45, 56, 78, 89],
    "Fees": [100, 200, 120, 230]
})

# print(df)
# print(type(df))


ecom_df = pd.read_csv("./data/ecommerce_orders.csv")
# print(ecom_df)

# print(ecom_df.head(3))
# print(ecom_df.tail(3))
# print(ecom_df.shape)
# print(ecom_df.dtypes)
# print(ecom_df.info())
# print(ecom_df.describe())

# ----------- Select Columns and filter rows:

# print(ecom_df["product_name"])
# print(ecom_df[["product_name", "customer_name", "total_amount"]])
# result = ecom_df[ecom_df["total_amount"] > 2000]
# print(result)

# res = ecom_df[(ecom_df["total_amount"] > 2000) & (ecom_df["payment_method"]=="UPI")]
# print(res)


#---------------------------------
# Select Rows by position:

# print(ecom_df.iloc[0:3])

# Select using a condition and named column
# print(ecom_df.loc[ecom_df["category"] == "Electronics", ["product_name", "unit_price"]])


