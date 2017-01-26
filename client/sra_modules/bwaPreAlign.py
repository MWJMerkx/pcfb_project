#!/usr/bin/env python3
"""
Module for benchmarking Bwa prealigner step (index making)
by Michiel Merx and Inne Lemstra 2017-01-24

#example of a align function, this is SRA dendent. The server should select
#which SRA specific code is used and package it as preAlign.py

Module is split into 2 functions for easy modifiction:
benchmark:
        Will be called from parent script pipeline.
        Function sets all needed parameters
        Time the execution of the prealignment step.
        Returns to parent script the prealignment time and debug information from
        the system call in align.
align:
        Does the system call with the preAlign statement. Command is first stored
        in a string, afterwards this variable is run via subprocess. This two step
        aproach is to improve readability.
        Returns a debug object from the subprocess call.
"""

import subprocess
import time

def benchmark(inputFile):
	'''Time the function of preAlign and return this and also a debug object'''
	output = "../test_data/index_files/bwa_index"
	#if absent make a new directory to store index files
	subprocess.call("mkdir -p ../test_data/index_files", shell= True) 
	
	startTime = time.time()
	debug = preAlign(inputFile, output)
	endTime = time.time()
	
	#calculate the elapsed time
	bmPreAlign = endTime - startTime	#bm stands for benchmark
	return([bmPreAlign, output, debug]) #bmPreAlign == time in seconds,
	# output what needs to be included as argument for next step.


def preAlign(indexInputPath, indexOutputPath):
	'''Call the preAlign step of Bwa which uses as input the referenceGenome and the path were the ouput should be written. It outputs an indexed version of the reference genome in multiple files.'''
	comIndex = "bwa index -p {0} -a is {1}".format(indexOutputPath,\
						indexInputPath)
	debug = subprocess.call(comIndex, shell=True)
	#debug is a subprocess object
	return(debug)

if __name__ == "main":
	#only run when library is called directly. (not the primary purpose)
	indexInputPath = "../test_data/e_coli_mg1655.fasta"
	indexOutputPath	= "../test_data/index_files/libTest"
	debug = preAlign(indexInputPath, indexOutputPath)
