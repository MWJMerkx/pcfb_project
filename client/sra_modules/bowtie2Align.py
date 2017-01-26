#! /usr/bin/env python3
"""
Module for benchmarking bowtie2 aligner
by Michiel Merx and Inne Lemstra 2017-01-24

#example of a align function, this is SRA dendent. The server should select
#which SRA specific code is used and package it as preAlign.py

Module is split into 2 functions for easy modifiction:
benchmark:
	Will be called from parent script pipeline.
	Function sets all needed parameters
	Time the execution of the alignment step.
	Returns to parent script the alignment time and debug information from
	the system call in align.
align:
	Does the system call with the align statement. Command is first stored
	in a string, afterwards this variable is run via subprocess. This two step
	aproach is to improve readability.
	Returns a debug object from the subprocess call.	
"""

import subprocess
import time

def benchmark(outputPreStep, shortReads):
	'''Time the function of align and return this and also a debug object'''
	output = "../test_data/Bowtie2_alignment_paired.sam"
	
	startTime = time.time()
	debug = align(outputPreStep, shortReads, output)
	endTime = time.time()
	
	#calculate the elapsed time
	bmAlign = endTime - startTime	#bm stands for benchmark
	return([bmAlign, debug])

def align(indexOutputPath, shortReadspath, alignOutputPath):
	'''Call the align step of Bowtie2 which uses as input the output of the prealinment, shortreadfile (a list with path to the to paired end read files), and the path were the ouput should be written.'''
	comAlign = "bowtie2 -f -x {0} -1 {1} -2 {2} -S {3}"\
		.format(indexOutputPath, shortReadspath[0],\
			 shortReadspath[1], alignOutputPath)
	debug = subprocess.call(comAlign, shell = True)	
	#debug is a subprocess object
	return(debug)

if __name__ == "main":
	#only run when library is called directly. (not the primary purpose)
	indexOutputPath = "./index_files/index_ecoli"
	shortReadpath =  "./sra_set.fasta"
	alginOutputPath =  "./alignments/ecoli"
	debug = align(indexOutputPath, shortReadpath, alginOutputPath)
