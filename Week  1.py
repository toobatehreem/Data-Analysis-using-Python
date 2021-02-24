#Data acquisition is a process of loading and reading data into notebook from various sources.
#In the data set columns represent an attribute or feature
#Targer is another name for the variable that we want to predict

import pandas as pd

df = pd.read_csv('C:/Users/Tooba Tehreem Sheikh/Desktop/imports-85.csv', header = None)
print(df)

print('Hello')

print(df.head)

headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]

df.columns = headers
print(df.head(5))

df.dropna(subset=['price'], axis= 0)
print(df.head(10))
print(df.tail(10))

df.to_csv("automobile.csv", index=False)


print(df.dtypes) #all data types of the columns object=string
print(df.describe())    #To get the quick statistics, we use the describe method. #std is standard deviation (mean of value and check how much it deviates from actual value

#describe only take numerical values

#To enable a summary of all the columns, we could add an argument include = "all" insidethe describe function bracket.

print(df.describe(include='all'))

'''We see that for object-type columns, a different set of statistics is evaluated, like unique,
top and frequency.
"Unique" is the number of distinct objects in the column, "top" is the most frequently
occurring object, and "freq" is the number of times the top object appears in the column.
Some values in the table are shown here as "NaN", which stands for "not a number".
This is because that particular statistical metric cannot be calculated for that specific
column data type.'''

'''Another method you can use to check your dataset is the dataframe.info function.
This function shows the top 30 rows and bottom 30 rows of the dataframe.'''


print(df.info)
print(df.info())
