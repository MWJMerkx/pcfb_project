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

print('Search for database:', DataBase)


## opening connection to MySQL server
## check for existing table in the database, else create a new one and store data


MyClient = mysqlclient.connect( host = "localhost", user= "root", passwd= "")
MyCursor = MyClient.cursor()

UseDatabase = """USE SRA;"""

MyCursor.execute(UseDatabase)

#DatabaseCheck = """SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '{0}' """.format(DataBase) 

DatabaseCheck = """SHOW TABLES LIKE '{0}';""".format(DataBase)

MyCursor.execute(DatabaseCheck)

DatabaseCheck = str(MyCursor.fetchall())

#print((DatabaseCheck))

if DatabaseCheck.count(DataBase) == 0:
	print("Creating new table")
else:
	print("Appending to existing table")

#if DatabaseCheck == DataBase:
#	print('True')
#else:
#	print( 'False')

CreateTable = """CREATE TABLE IF NOT EXISTS {0}(
    ID integer not null auto_increment primary key,
    proccess_time float,
    align_time float,
    accuracy float,
    cpu tinytext,
    ram tinytext
    );""".format(DataBase)

MyCursor.execute(CreateTable)



MyCursor.close()
MyClient.close()
