#!/usr/bin/env python3

# Inne Lemstra
# Michiel Merkx

# server side data processing for SRA benchmarking


import gzip
import MySQLdb as mysqlclient
import re


#InFile = input('File name:\n')
InFile = 'bwa_out.txt'


MyRe = r"((\w+)_.*)"
MySearch = InFile
MyResult = re.search(MyRe, MySearch)

DataBase = MyResult.group(2)

print(DataBase)

MyClient = mysqlclient.connect( host = "localhost", user= "root", passwd= "")
MyCursor = MyClient.cursor()

DatabaseCheck = """SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{0}' """.format(DataBase) 

MyCursor.execute(DatabaseCheck)

DatabaseCheck = str(MyCursor.fetchall())

print((DatabaseCheck))

if DatabaseCheck.count(DataBase) == 0:
	print(DataBase + " bestaat niet")
else:
	print("bestaat wel")

if DatabaseCheck == DataBase:
	print('True')
else:
	print( 'False')


MyCursor.close()
MyClient.close()
