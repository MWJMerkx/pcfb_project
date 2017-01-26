#!/usr/bin/env python3

# Inne Lemstra
# Michiel Merkx



#### Out-dated and no longer in use












# query the database and return benchmark speeds on selected short read aligners
# requires instalation of mysqlclient python module


# sra name input seperated by commas

import MySQLdb as mysqlclient


SearchTable = input('Which table to search:\n').lower().split(",")
#print(SearchTable)
SearchTable.sort()

## connects to mysql server
## queries server for data from each table mentioned in the input string.

MyClient = mysqlclient.connect( host = "localhost", user= "root", passwd= "")
MyCursor = MyClient.cursor()

UseDatabase = """USE SRA;"""

MyCursor.execute(UseDatabase)

Counter = 0

for Item in SearchTable:
	#print('\nSearching for:',SearchTable[Counter])
	print('\n')
	BenchmarkQuery = """SELECT AVG(proccess_time), AVG(align_time) FROM {0};""".format(SearchTable[Counter])
	MyCursor.execute(BenchmarkQuery)
	Benchmark = MyCursor.fetchall()
	print(SearchTable[Counter], 'benchmark:\n', 'Average proccess time:', Benchmark[0][0], 'seconds\n', 'Average align time:', Benchmark[0][1], 'seconds\n' )
	
	Counter += 1



