#!/usr/bin/env python3

#Michiel Merx and Inne Lemstra 2017-01-24
#example of a prealign function, this is SRA dendent. The server should select
#which sra specific code is used and package it as preAlign.py

#Bowtie2 example

import subprocess

def go(indexInputPath, indexOutputPath): 
	comIndex = "bowtie2-build -f {0} {1}".format(indexInputPath,\
						indexOutputPath)
	debug = subprocess.call(comIndex, shell=True)
	return(debug)

if __name__ == "main":
	indexInputPath = "../test_data/e_coli_mg1655.fasta"
	indexInputPath	= "../test_data/index_files/libTest"
	debug = go(indexInputPath, indexOutputPath)

