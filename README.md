
![Travis-CI](TravisCI.png)


[![Build Status](https://travis-ci.org/MWJMerkx/pcfb_project.svg?branch=master)](https://travis-ci.org/MWJMerkx/pcfb_project)


# pcbf_project

## Short read archive mapper benchmarking tool and database

#### Inne Lemstra and Michiel Merkx

### Goal:

To create a tool to allow benchmarking of various mappers (eg. bowtie2, bwa) on a standardised dataset,
and store the results in an easily accessible database.

#### part1 Client side:

Python tool to run the selected mapper, and benchmark the preformance.

Data collected:

Index construction time

Mapping time

CPU model

RAM available

#### part 2 Server side:

Python tool for checking the quality of the mapping, and import it into the MySQL database.

Quality control done using SAMtools and QualiMap.

### Structure:

#### Front page:

SRA_database.sql is the most recent database backup created from the MySQL server.

#### Downloads:

.tar.gz archives wich contain the files required to execute the benchmarks for the names mapper.

#### Client:

Contains all the individual scripts required to preform the benchmarking on the client pc.

#### Server:

Contains all the individual scripts pertaining to database structure, quality controll and database additions.

#### Test_data:

Contains the sample data sets used to preform intial tests of client and server side processes. 

## Function:

For use of the SRA benchmarking tool, download the required package from the downloads folder and run the run_benchmark.sh file.
Please be aware that pre-instalation of the selected tool is required (eg. Bowtie2). 
Generated output files can then be quality controlled using the parser_benchmark_v2.py script foun in the server folder. 
Please note that for this SAMtools, QualiMap, and access to a suitably setup database is required.

## Database structure:

The database is made up of three tables, 
1: Results, contains the benchmark results for all tools and data sets.
2: Archives, contains information on the datasets used for benchmarking.
3: Aligner, contains information on aligner version and parameters used during benchmarking.

## Required software:

#### Client side:

Bowtie2 (http://bowtie-bio.sourceforge.net/bowtie2/index.shtml)

Bwa (http://bio-bwa.sourceforge.net/)

#### Server side:

mysqlclient (https://pypi.python.org/pypi/mysqlclient)

SAMtools (http://samtools.sourceforge.net/)

QualiMap (http://qualimap.bioinfo.cipf.es/)

MySQL (https://dev.mysql.com/downloads/mysql/)
