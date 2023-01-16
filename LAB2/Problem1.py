import pandas as pd

csv_data = pd.read_csv('train.csv')
print(csv_data.shape)
print(csv_data.dtypes)
print(csv_data.info)#Gives us no. of rows and columns and name each column and data type
print(csv_data.describe())#Describes the data to us
