#!/usr/bin/env python3

# Inne Lemstra
# Michiel Merkx

# reformat datafile from client side speed benchmarking of short read aligner
# queries database for sra data table, if not present create table
# enters benchmark information into the relevant database table

# requires instalation of mysqlclient python module


import gzip
import MySQLdb as mysqlclient
import re


#InFile = input('File name:\n')
InFile = 'soap_out.txt'


MyRe = r"((\w+)_.*)"
MySearch = InFile
MyResult = re.search(MyRe, MySearch)

DataBase = MyResult.group(2)

print('Search for database:', DataBase)


## opens connection to MySQL server
## check for existing table in the database, else create a new one


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
	CreateTable = """SET sql_notes = 0;
	    CREATE TABLE IF NOT EXISTS {0}(
	    ID INTEGER NOT NULL AUTO_INCREMENT PRIMARY KEY,
	    sra_id TINYTEXT,
	    proccess_time FLOAT,
	    align_time FLOAT,
	    accuracy FLOAT,
	    cpu TINYTEXT,
	    ram INT
	    );
	    SET sql_notes = 1;""".format(DataBase)
	MyCursor.execute(CreateTable)

else:
	print("Appending to existing table")

## instert data into correct table on database

#InsertData = """INSERT INTO {0} SET
#    sra_id='{0}',
#    proccess_time={1},
#    align_time={2},
#    accuracy={3},
#    cpu='{4}',
#    ram='{5}';""".format(DataBase)

#MyCursor.execute(InsertData)

#if DatabaseCheck == DataBase:
#	print('True')
#else:
#	print( 'False')


MyCursor.close()
MyClient.close()

# print ("Data successfully added")
