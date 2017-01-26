#!/usr/bin/env python3
#Inne Lemstra and Michiel Merkx

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

