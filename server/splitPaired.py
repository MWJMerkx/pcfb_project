#!/usr/bin/env python3

#Michiel Merx and Inne Lemstra 2017-01-25

fileName = "../test_data/sra_set.fasta"
original_handle = open(fileName, 'r')
pairs1 = ".." + fileName.strip(".fasta") + "pair_1.fasta" 
pairs1_handle = open(pairs1, 'w')
pairs2 = ".." + fileName.strip(".fasta") + "pair_2.fasta" 
pairs2_handle = open(pairs2, 'w')

counter = 0

for line in original_handle:
	if counter % 4 == 0 or counter % 4 == 1:
		pairs1_handle.write(line)
	else:
		pairs2_handle.write(line)
	counter += 1
pairs1_handle.close()
pairs2_handle.close()

			
