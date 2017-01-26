#! /usr/bin/env python3
"""
Module for benchmarking bwa alignment
by Michiel Merx and Inne Lemstra 2017-01-24

Module is split into 2 functions for easy modifiction:
benchmark:
        Will be called from parent script pipeline.
        Function sets all needed parameters, next to what is provided in parent 
	script. 
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
	output = "../test_data/Bwa_alignment_paired.sam"
	
	startTime = time.time()
	debug = align(outputPreStep, shortReads, output)
	endTime = time.time()
	
	#calculate the elapsed time
	bmAlign = endTime - startTime	#bm stands for benchmark
	return([bmAlign, debug])

def align(indexOutputPath, shortReadspath, alignOutputPath):
	'''Call the align step of Bwa which uses as input the output of the prealinment, shortreadfile (a list of paired reads each part of the pair following eachother), and the path were the ouput should be written.'''
	comAlign = "bwa mem -P {0} {1} > {3}"\
		.format(indexOutputPath, shortReadspath,\
			 shortReadspath[1], alignOutputPath)
	debug = subprocess.call(comAlign, shell = True)
	return(debug)

if __name__ == "main":
	#only run when library is called directly. (not the primary purpose)
	indexOutputPath = "./index_files/index_ecoli"
	shortReadpath =  "./sra_set.fasta"
	alginOutputPath =  "./alignments/ecoli"
	debug = align(indexOutputPath, shortReadpath, alginOutputPath)
