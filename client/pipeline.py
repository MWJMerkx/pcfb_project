#!/usr/bin/env python3
#Inne Lemstra and Michiel Merkx
"""Benchmark a short sequence aligner by calling on different subscripts
	These subscripts are stored as libraries in the same directory
ScriptFlow:
This python pipeline consist of the following steps:
	Get hardware info (using bash commands)
	Run and time the preAligment step of the aligner
	Run the alignment step of the aligner (using the output of the prestep)

OutPut:
	This script will print a short message to screen of timing of each alignment step.
These timings as wel as hardware info and info about aligner used will be written to a textfile. The name of this file is set iin the first part of the script.
	Where ans how the alignment output of the alignment program will be written is determined in the library align. (as well as output for prestep is determined in preAlign library)
	
"""
import subprocess
import hardware_inquire34
import preAlign
import align
import time


mapper = "Bowtie2"
shortReads = ["../test_data/E_coli_MG1655_1.fasta", "../test_data/E_coli_MG1655_2.fasta"]

#mapper = "Bwa"
#shortReads = "../test_data/E_coli_MG1655.fasta"

referenceGenome = "../test_data/E_coli_reference.fasta"
sra_ID = "E_coli_MG1655"
benchmarkFile = "../test_data/{0}_benchmark.txt".format(mapper)

#gather hardware data
hwInfo = hardware_inquire34.getInfo()

#Run and benchmark preAlignment step
[bmPreAlign, preAlignOutput, debugPreAlign] = preAlign.benchmark(referenceGenome)

#Run and benchmark alignment step
[bmAlign, debug] = align.benchmark(preAlignOutput, shortReads)

#print the time of the preAlignment and alignment steps to screen 
print("PreAlign: {0}s\nbmAlign: {1}s\n".format(bmPreAlign, bmAlign))

#Write results to benchmark file
benchmarkHandle = open(benchmarkFile,"w")

benchmarkHandle.write("{0},{1},{2},{3},{4},{5}"\
		.format(sra_ID, mapper, bmPreAlign, bmAlign, hwInfo[0], hwInfo[1]))

