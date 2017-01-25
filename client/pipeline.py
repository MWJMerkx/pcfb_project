#!/usr/bin/env python3
#Inne Lemstra and Michiel Merkx

import subprocess
import hardware_inquire34
import preAlign
import align
import time
import cProfile

shortReads = ["../test_data/sra_sepair_1.fasta", "../test_data/sra_sepair_2.fasta"]
referenceGenome = "../test_data/e_coli_mg1655.fasta"
alignmentOutput = "../test_data/newest_alignment.sam"
#preAlignOutput = "../test_data/index_files/indexPipeline"	
sra_ID = "E_coli_MG1655"


#gather hardware data
hwInfo = hardware_inquire34.getInfo()
#bmHardware = timeit.timeit("testHardware", \
#	setup= "from __main__ import testHardware", number= 1)

#setup timers

#make index files of refernce genome and time
#make seperate module and import prealign function

#comIndex = "bowtie2-build -f {0} {1}".format(referenceGenome, preAlignOutput)
[bmPreAlign, preAlignOutput, debugPreAlign] = preAlign.benchmark(referenceGenome)

#bmPreAlign = timeit.timeit("testPreAlign", \
#		setup= "from __main__ import testPreAlign", number= 1)

#run aligner and time
#make seperate module and import align function
#shortReadsPath = "../test_data/sra_set.fasta"
#alignOutputPath = "../test_data/libtest"

#comAlign = "bowtie2 -f -x {0} -U {1} -S {2}".format(indexOutputPath,\
#					 shortReadsPath, alignOutputPath)

[bmAlign, debug] = align.benchmark(preAlignOutput, shortReads)
#bmAlign = timeit.timeit("testAlign", \
#			setup= "from __main__ import testAlign", number= 1)
print("Hardware: {0}s\nPreAlign: {1}s\nbmAlign: {2}s\n".format("NA", bmPreAlign, bmAlign))

benchmarkHandle = open("../test_data/benchmark.txt","w")

benchmarkHandle.write("{0},Bowtie2,{1},{2}, NA, {3}, {4}"\
	.format(sra_ID,bmPreAlign, bmAlign, hwInfo[0], hwInfo[1]))

