#!/usr/bin/env pyhton3
#Inne Lemstra and Michiel Merkx

import subproccess
import hardware_inquire

#gather hardware data
[infoCPU, infoRAM] = hardware_inquire.getInfo()

#setup timers

#make index files of refernce genome and time
#make seperate module and import prealign function
indexInputPath = "./e_coli_mg1655.fasta"
indexOutputPath = "./index_files/index_ecoli"

comIndex = "bowtie2-build -f {0} {1}".format(indexInputPath, indexOutputPath)

#run aligner and time
#make seperate module and import align function
shortReadspath = "./sra_set.fasta"
alignOutputPath = "./index_files/index_ecoli"

comAlign = "bowtie2 -f -x {0} -U {1} -S {2}".format(indexOutputPath,\
					 shortReadspath, alignOutputPath)

