#!/usr/bin/env python3

# Inne Lemstra
# Michiel Merkx

# reformat datafile from client side speed benchmarking of short read aligner
# queries database for sra data table, if not present create table
# enters benchmark information into the relevant database table

# requires instalation of mysqlclient python module


import gzip
import MySQLdb as mysqlclient
import subprocess
import re

Qualimap = '~/Documents/qualimap_v2.2.1/qualimap'

FileName = input('File name:\n').split()


InFile = open(FileName[0], 'r')

subprocess.call("samtools sort -o sorted_output.sam {0}".format(FileName[1]),shell=True)
subprocess.call(Qualimap +" bamqc -bam sorted_output.sam -outdir qualimap_results",shell=True,executable='/bin/bash')

ResultFile = open('./qualimap_results/genome_results.txt', 'r')

Mapped = []
SearchFile = ResultFile.read()

print(type(SearchFile))
ReSearch1 = r"number of reads = (\d+,\d*)"
Search1 = re.search(ReSearch1, SearchFile)
number_reads = Search1.group(1).replace(',','')

Mapped.append(number_reads)

ReSearch2 = r"number of mapped reads = (\d+,\d*) .*"
Search2 = re.search(ReSearch2, SearchFile)
mapped_reads = Search2.group(1).replace(',','')

Mapped.append(mapped_reads)

ReSearch3 = r"mean mapping quality = (\d+.\d*)"
Search3 = re.search(ReSearch3, SearchFile)

mapped_quality = Search3.group(1)

Mapped.append(mapped_quality)


#print(Mapped)


## opens connection to MySQL server
## check for existing table in the database, else create a new one







MyClient = mysqlclient.connect( host = "localhost", user= "root", passwd= "")
MyCursor = MyClient.cursor()

UseDatabase = """USE SRA;"""

MyCursor.execute(UseDatabase)

for Line in InFile:
	
	InputData = Line.split(',')
	
	print(InputData[0],InputData[1],InputData[2],InputData[3],Mapped[0],Mapped[1],Mapped[2],InputData[5],InputData[6])
	
	InsertData = """INSERT INTO results SET
	    SRA_ID='{0}',
	    aligner_ID='{1}',
	    proccess_time={2},
	    align_time={3},
	    number_reads={4},
	    mapped_reads={5},
	    mapped_quality={6},
	    cpu='{7}',
	    ram='{8}';""".format(InputData[0],InputData[1],InputData[2],InputData[3],Mapped[0],Mapped[1],Mapped[2],InputData[5],InputData[6])
	MyCursor.execute(InsertData)
	MyClient.commit()

MyCursor.close()
MyClient.close()

print ("Data successfully added")
