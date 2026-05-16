import pandas as pd
#to read csv file
data=pd.read_csv("netflix_titles.csv")
#to see the first rows of dataset
print(data.head(5))
#to see the last rows of dataset
print(data.tail(5))
#to find if null values are present
null=data.isnull()
print(null)
#to how many null values are present in each column
print(null.sum())
#to find total null values in dataset
print("Total Null Values: ",end=" ")
print(null.sum().sum())
#to show the only columns with null values
print(data[data.columns[data.isnull().any()]])
#to fill null values
data.fillna({
    "director": "Unknown",
    "cast": "Not Available",
    "country": "Unknown",
    "rating": "Unrated",
    "duration": "0",
    "date_added": "2000-01-01"
}, inplace=True)
data.to_csv("CLEANED_DATA.csv",index=False)
print("Data successfully saved into csv file")