#!/usr/bin/env python3

# query the database and to return benchmark information on SRA's

import MySQLdb as mysqlclient


SearchTable = input('Which table to search:').split(",")
#print(SearchTable)

MyClient = mysqlclient.connect( host = "localhost", user= "root", passwd= "")
MyCursor = MyClient.cursor()

UseDatabase = """USE SRA;"""

MyCursor.execute(UseDatabase)

Counter = 0

for Item in SearchTable:
	BenchmarkQuery = """SELECT sra_id, AVG(proccess_time), AVG(align_time) FROM {0};""".format(SearchTable[Counter])
	MyCursor.execute(BenchmarkQuery)
	Benchmark = MyCursor.fetchall()
	print(Benchmark)
	
	Counter += 1
