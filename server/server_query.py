#!/usr/bin/env python3

# query the database and to return benchmark information on SRA's

MyClient = mysqlclient.connect( host = "localhost", user= "root", passwd= "")
MyCursor = MyClient.cursor()

UseDatabase = """USE SRA;"""

MyCursor.execute(UseDatabase)

BenchmarkQuery = """SELECT AVG(align_time), AVG(accuracy) FROM * GROUP BY ID;"""
 MyCursor.execute(BenchmarkQuery)
