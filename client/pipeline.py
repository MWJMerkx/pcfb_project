#!/usr/bin/env python3
#Inne Lemstra and Michiel Merkx

import subprocess
import hardware_inquire34
import preAlign
import align
import timeit

def testAlign():
	shortReadsPath = "../test_data/sra_set.fasta"
	indexOutputPath = "../test_data/index_files/index_ecoli"
	alignOutputPath = "../test_data/libtest"
	
	comAlign = "bowtie2 -f -x {0} -U {1} -S {2}".format(indexOutputPath,\
					 shortReadsPath, alignOutputPath)
	debug = align.go(indexOutputPath, shortReadsPath, alignOutputPath)

def testPreAlign():
	indexInputPath = "../test_data/e_coli_mg1655.fasta"
	indexOutputPath = "../test_data/index_files/index_ecoli"
	comIndex = "bowtie2-build -f {0} {1}"\
					.format(indexInputPath, indexOutputPath)
	debug = preAlign.go(indexInputPath, indexOutputPath)	

def testHardware():
	hardware_inquire34.getInfo()
	

#gather hardware data
hwInfo = hardware_inquire34.getInfo()
bmHardware = timeit.timeit("testHardware", \
	setup= "from __main__ import testHardware", number= 1)

#setup timers

#make index files of refernce genome and time
#make seperate module and import prealign function
indexInputPath = "../test_data/e_coli_mg1655.fasta"
indexOutputPath = "../test_data/index_files/index_ecoli"

comIndex = "bowtie2-build -f {0} {1}".format(indexInputPath, indexOutputPath)
#timePreAlign = timeit.timeit("preAlign.go(indexInputPath, indexOutputPath)"\
#	, setup = "import preAlign" , number= 1)

bmPreAlign = timeit.timeit("testPreAlign", \
		setup= "from __main__ import testPreAlign", number= 1)

#run aligner and time
#make seperate module and import align function
shortReadsPath = "../test_data/sra_set.fasta"
alignOutputPath = "../test_data/libtest"

comAlign = "bowtie2 -f -x {0} -U {1} -S {2}".format(indexOutputPath,\
					 shortReadsPath, alignOutputPath)

#SummaryAlign = align.go(indexOutputPath, shortReadsPath, alignOutputPath)
bmAlign = timeit.timeit("testAlign", \
			setup= "from __main__ import testAlign", number= 1)
print("Hardware: {0}s\nPreAlign: {1}s\nbmAlign: {2}\n".format(bmHardware, bmPreAlign, bmAlign))

benchmarkHandle = open("../test_data/benchmark.txt","w")

benchmarkHandle.write("Bowtie2,{0},{1}, NA, {2}, {3}"\
	.format(bmPreAlign, bmAlign, hwInfo[0], hwInfo[1]))

