#!/usr/bin/env python3
#Inne Lemstra and Michiel Merkx

import subprocess
import hardware_inquire34
import preAlign
import align

#gather hardware data
hwInfo = hardware_inquire34.getInfo()

#setup timers

#make index files of refernce genome and time
#make seperate module and import prealign function
indexInputPath = "../test_data/e_coli_mg1655.fasta"
indexOutputPath = "../test_data/index_files/index_ecoli"

comIndex = "bowtie2-build -f {0} {1}".format(indexInputPath, indexOutputPath)
SummaryPreAlign = preAlign.go(indexInputPath, indexOutputPath)

#run aligner and time
#make seperate module and import align function
shortReadsPath = "../test_data/sra_set.fasta"
alignOutputPath = "../test_data/libtest"

comAlign = "bowtie2 -f -x {0} -U {1} -S {2}".format(indexOutputPath,\
					 shortReadsPath, alignOutputPath)

SummaryAlign = align.go(indexOutputPath, shortReadsPath, alignOutputPath)


