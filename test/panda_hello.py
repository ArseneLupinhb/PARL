import pandas
import numpy

path = r'C:\Users\AL\Desktop\test.csv'
data = pandas.read_csv(path)
print(data.count())
print(data.head())
