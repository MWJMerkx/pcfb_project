#!/usr/bin/env pyhton3
#Inne Lemstra and Michiel Merkx

#make index files of refernce genome
indexInputPath = "./e_coli_mg1655.fasta"
indexOutputPath = "./index_files/index_ecoli"

comIndex = "bowtie2-build -f {0} {1}".format(indexInputPath, indexOutputPath)

#run aligner
shortReadspath = "./sra_set.fasta"
alignOutputPath = "./index_files/index_ecoli"

comAlign = "bowtie2 -f -x {0} -U {1} -S {3}".format(indexOutputPath,\
					 shortReadspath, alignOutputPath)

