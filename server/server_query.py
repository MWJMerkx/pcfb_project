#!/usr/bin/env python3

# query the database and to return benchmark information on SRA's

import MySQLdb as mysqlclient


SearchTable = input('Which table to search:\n').split(",")
#print(SearchTable)

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
