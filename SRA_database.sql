-- MySQL dump 10.13  Distrib 5.5.54, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: SRA
-- ------------------------------------------------------
-- Server version	5.5.54-0ubuntu0.14.04.1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Current Database: `SRA`
--

CREATE DATABASE /*!32312 IF NOT EXISTS*/ `SRA` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `SRA`;

--
-- Table structure for table `aligner`
--

DROP TABLE IF EXISTS `aligner`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `aligner` (
  `aligner_ID` varchar(20) NOT NULL,
  `version` tinytext,
  `set_parameters` tinytext,
  PRIMARY KEY (`aligner_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `aligner`
--

LOCK TABLES `aligner` WRITE;
/*!40000 ALTER TABLE `aligner` DISABLE KEYS */;
INSERT INTO `aligner` VALUES ('Bowtie2','V2.2.4','-f -x {0} -1 {1} -2 {2} -S {3}'),('Bwa','V0.7.12-r1039','mem -P {0} {1} > {3}');
/*!40000 ALTER TABLE `aligner` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `archives`
--

DROP TABLE IF EXISTS `archives`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `archives` (
  `SRA_ID` varchar(20) NOT NULL,
  `organism` tinytext,
  `accession_no` tinytext,
  `no_reads` int(11) DEFAULT NULL,
  `read_type` tinytext,
  PRIMARY KEY (`SRA_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `archives`
--

LOCK TABLES `archives` WRITE;
/*!40000 ALTER TABLE `archives` DISABLE KEYS */;
INSERT INTO `archives` VALUES ('E_coli_MG1655','Escherichia_coli','SRX2510268',13599935,'Paired');
/*!40000 ALTER TABLE `archives` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `results`
--

DROP TABLE IF EXISTS `results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `results` (
  `RUN_ID` int(11) NOT NULL AUTO_INCREMENT,
  `SRA_ID` tinytext,
  `aligner_ID` tinytext,
  `proccess_time` float DEFAULT NULL,
  `align_time` float DEFAULT NULL,
  `number_reads` int(11) DEFAULT NULL,
  `mapped_reads` int(11) DEFAULT NULL,
  `mapped_quality` float DEFAULT NULL,
  `cpu` tinytext,
  `ram` tinytext,
  PRIMARY KEY (`RUN_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `results`
--

LOCK TABLES `results` WRITE;
/*!40000 ALTER TABLE `results` DISABLE KEYS */;
INSERT INTO `results` VALUES (1,'E_coli_MG1655','Bowtie2',6.91383,0.622095,3000,2946,39.9925,' cpu = []',' RAM available = 255'),(2,'E_coli_MG1655','Bowtie2',4.89881,1.06036,3000,2946,39.9925,'cpu = Intel(R) Core(TM) i7-2700K CPU @ 3.50GHz','RAM available = 6848'),(3,'E_coli_MG1655','Bowtie2',6.29989,1.15116,3000,2946,39.9925,'cpu = Intel(R) Core(TM) i3-4005U CPU @ 1.70GHz','RAM available = 3313'),(4,'E_coli_MG1655','Bowtie2',13.6008,0.99178,3000,2946,39.9925,'cpu = []','RAM available = 143'),(5,'E_coli_MG1655','Bwa',3.84304,0.254034,3001,2960,57.0733,'cpu = Intel(R) Core(TM) i3-4005U CPU @ 1.70GHz','RAM available = 2866'),(6,'E_coli_MG1655','Bwa',5.04852,0.24085,3001,2960,57.0733,'cpu = []','RAM available = 329');
/*!40000 ALTER TABLE `results` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-01-26 12:52:01
