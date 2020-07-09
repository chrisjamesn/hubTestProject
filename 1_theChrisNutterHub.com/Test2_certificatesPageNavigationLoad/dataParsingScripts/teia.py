# Imports
import pandas as pd

import mysql

import mysql.connector

import csv

# Extracting data from CSV file and sorting data into MySQL tables named by 'threadName'
# Helpful source: https://stackoverflow.com/questions/10154633/load-csv-data-into-mysql-in-python/10154650
# Another helpful source: https://datatofish.com/import-csv-sql-server-python/

data=pd.read_csv("dpaTotals.csv")

df=pd.DataFrame(data, columns =['threadTrial', 'averageTotalPerUser'])

f = open('totalElapsedIncreaseAverage.txt', 'a')


threads=df['threadTrial'].unique()

totals=[]

for thread in threads:
	dfd=df[df.threadTrial == thread]
	atpu = dfd['averageTotalPerUser'].sum()
	totals.append(atpu)
	
indexes=[]

for total in totals:
	index=totals.index(total)
	indexes.append(index) 
	
differences=[]

for index in indexes:
	differenceValue = totals[index]-totals[index-1]
	difference = round(differenceValue, 2)
	if index > 0:
		differences.append(difference)	
		
print(differences)

def mean(lst):
	x=sum(lst)
	y=len(lst)
	return x/y
	
aroc = str(round(mean(differences), 2))

f = open('totalElapsedIncreaseAverage.txt', 'a');

f.write('Average Rate of Change From Least to Greatest Number of Users: ')
f.write(aroc)
