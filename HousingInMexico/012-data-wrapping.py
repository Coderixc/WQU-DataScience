import pandas as pd
# from IPython.display import VimeoVideo

# The first part of any data science project is preparing your data, which means making sure its in the right place and format for you to conduct your analysis. The first step of any data preparation is importing your raw data and cleaning it.

# If you look in the small-data directory on your machine, you'll see that the data for this project comes in three CSV files: mexico-real-estate-1.csv, mexico-real-estate-2.csv, and mexico-real-estate-3.csv.


# Task 1.2.1: Read these three files into three separate DataFrames named df1, df2, and df3, respectively.
df1 = pd.read_csv("data/mexico-real-estate-1.csv")
df2 = pd.read_csv("data/mexico-real-estate-2.csv")
df3 = pd.read_csv("data/mexico-real-estate-3.csv")

# df1.shape
# df1.info()
# df1.head(10) by feault 5


# df1.info
# tranform df1["price_usd"] = 
df1["price_usd"] = =df1["price_usd"].astype(str).str.replace("$", "",regex= False).str.replace(",","").astype(float).head()



# crate a `"price_usd"`  col
df2["price_usd"] =(df2["price_mxn"] /19).round(2)

# Drop "price_max" col
df2.drop(columns=["price_mxn"], inplace=True)

# Task 1.2.5: Drop rows with NaN values in df3. Then use the split method to create two new columns from "lat-lon" named "lat" and "lon", respectively.
# Drop 'Nan'
df3.dropna(inplace=True)

df3[["lat","lon"]]= df3["lat-lon"].str.split(",",expand = True).head()

df3.head()