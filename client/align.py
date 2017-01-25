#! /usr/bin/env python3

#Michiel Merx and Inne Lemstra 2017-01-24
import subprocess
import time

def benchmark(outputPreStep, shortReads):
	output = "../test_data/latest_alignment.sam"
	startTime = time.time()
	debug = go(outputPreStep, shortReads, output)
	endTime = time.time()
	bmAlign = endTime - startTime
	return([bmAlign, debug])

def go(indexOutputPath, shortReadspath, alignOutputPath):
	comAlign = "bowtie2 -f -x {0} -U {1} -S {2}".format(indexOutputPath,\
                                         shortReadspath, alignOutputPath)
	debug = subprocess.call(comAlign, shell = True)
	return(debug)

if __name__ == "main":
	indexOutputPath = "./index_files/index_ecoli"
	shortReadpath =  "./sra_set.fasta"
	alginOutputPath =  "./alignments/ecoli"
	debug = go(indexOutputPath, shortReadpath, alginOutputPath)
