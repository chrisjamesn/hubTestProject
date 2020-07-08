# Imports
import pandas as pd

import mysql

import mysql.connector

import csv

# Extracting data from CSV file and sorting data into MySQL tables named by 'threadName'
# Helpful source: https://stackoverflow.com/questions/10154633/load-csv-data-into-mysql-in-python/10154650
# Another helpful source: https://datatofish.com/import-csv-sql-server-python/

data=pd.read_csv("rawDataReceived/fourUsersResponseTime.csv")

df=pd.DataFrame(data, columns =['timeStamp', 'elapsed', 'label', 
	'responseCode', 'responseMessage', 'threadName', 'dataType', 'success', 'failureMessage', 'bytes', 
	'sentBytes', 'grpThreads', 'allThreads', 'url', 'Latency', 'SampleCount', 'ErrorCount', 'IdleTime', 
	'Connect'])

# Pandas dataframe for needed data
# Resource: https://pandas.pydata.org/docs/getting_started/intro_tutorials/03_subset_data.html
# Resource: https://stackoverflow.com/questions/15891038/change-data-type-of-columns-in-pandas#:~:text=The%20best%20way%20to%20convert%20one%20or%20more%20columns%20of,floating%20point%20numbers%20as%20appropriate.
dfs=df[['threadName','label', 'elapsed']]
# lyst=df['elapsed'].sum() # THIS WORKS!!
# print(lyst)

# dfst=dfs[dfs.threadName == 'Sixty-Four Users 7-2'] # THIS WORKS!
# print(dfst)



# Get distinct values from Pandas dataframe
# Resource: https://riptutorial.com/pandas/example/26077/select-distinct-rows-across-dataframe
threads=dfs['threadName'].unique()
# print(threads)

# Filtering data based on rows: https://datacarpentry.org/python-ecology-lesson/03-index-slice-subset/index.html
#Example testFrame=dfs[dfs.threadName=='Sixty-Four Users 7-2']
#Example print(testFrame)

tevpt=[]

f = open('dpa4.txt', 'a')

for thread in threads:
	dfst=dfs[dfs.threadName == thread]
	tev2 = dfst['elapsed'].sum()
	tev = tev2/2
	tevpt.append(tev)
	print(thread, 'Total Elapsed: ', tev)
	f.write(thread)
	f.write(' Total Elapsed: ')
	f.write(str(tev))
	f.write('\n')

def mean(lst):
	x=sum(lst)
	y=len(lst)
	return x/y
	
teva = mean(tevpt)

print('Average Total Elapsed Per Thread: ', round(teva, 2))	
f.write('Average Total Elapsed Per Thread: ')
f.write(str(round(teva, 2)))
