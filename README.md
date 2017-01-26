
![Travis-CI](TravisCI.png)


[![Build Status](https://travis-ci.org/MWJMerkx/pcfb_project.svg?branch=master)](https://travis-ci.org/MWJMerkx/pcfb_project)


# pcbf_project

#### Inne Lemstra and Michiel Merkx



## Short read archive mapper benchmarking tool and database

### Goal:

To create a tool to allow benchmarking of various mappers (eg. bowtie2, bwa) on a standardised dataset,
and store the results in an easily accessible database.

### part1:

Client side:

Python tool to run the selected mapper, and benchmark the preformance.

Data collected:

Index construction time

Mapping time

CPU model

RAM available

### part 2

Server side:

Python tool for checking the quality of the mapping, and import it into the MySQL database.

Quality controll done using SAMtools and QualiMap.

