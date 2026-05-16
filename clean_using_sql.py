import pandas as pd
import sqlite3
#load the CSV file
df = pd.read_csv("netflix_titles.csv")
#create an in-memory SQLite database
conn = sqlite3.connect("cleaned_data.db")
#load DataFrame into the database
df.to_sql("my_table", conn, index=False, if_exists="replace")
# Write your SQL query
#to represent records which are not null::
# Dynamically generate the NOT NULL condition for all columns
not_null_condition = " AND ".join([f"`{col}` IS NOT NULL" for col in df.columns])
query = f"SELECT * FROM my_table WHERE {not_null_condition}"
# Run the query and store result in database named:filtered_table
result = pd.read_sql(query, conn)
result.to_sql("filtered_table", conn, index=False, if_exists="replace")

#To fill null values
df.fillna({
    "director": "Unknown",
    "cast": "Not Available",
    "country": "Unknown",
    "rating": "Unrated",
    "duration": "0",
    "date_added": "2000-01-01"
}, inplace=True)
df.to_sql("filled_table", conn, index=False, if_exists="replace")

#to find the types 
query="SELECT distinct type from my_table order by type"
res=pd.read_sql(query,conn)
print(res)
#to find count where type = movie
query="select count(*) from my_table where type='Movie'"
res=pd.read_sql(query,conn)
print(res)
# To find the data where type= tv show
query="select * from my_table where type='TV Show'"
res=pd.read_sql(query,conn)
print(res)
#to find different movies 
query="select distinct title from my_table where type='Movie'"
res=pd.read_sql(query,conn)
print(res)
res.to_sql("movies_names",conn,index=False,if_exists="replace")
#to find different tv shows
query="select distinct title from my_table where type='TV Show'"
res=pd.read_sql(query,conn)
print(res)
res.to_sql("tvshow_names",conn,index=False,if_exists="replace")
#to find distinct ratings
query1="select distinct rating from my_table"
resl=pd.read_sql(query1,conn)
print(resl)
