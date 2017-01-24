#! /usr/bin/env python3

#Michiel Merx and Inne Lemstra 2017-01-24
import subprocess

def go(indexOutputPath, shortReadspath, alignOutputPath):
	comAlign = "bowtie2 -f -x {0} -U {1} -S {2}".format(indexOutputPath,\
                                         shortReadspath, alignOutputPath)
	debug = subprocess.run(comAlign, shell = True)
	return(debug)

if __name__ == "main":
	indexOutputPath = "./index_files/index_ecoli"
	shortReadpath =  "./sra_set.fasta"
	alginOutputPath =  "./alignments/ecoli"
	debug = go(indexOutputPath, shortReadpath, alginOutputPath)
