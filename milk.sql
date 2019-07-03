-- MySQL dump 10.13  Distrib 5.7.26, for Linux (x86_64)
--
-- Host: localhost    Database: milk
-- ------------------------------------------------------
-- Server version	5.7.26-0ubuntu0.16.04.1

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
-- Table structure for table `credentials`
--

DROP TABLE IF EXISTS `credentials`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `credentials` (
  `username` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `designation` int(11) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `credentials`
--

LOCK TABLES `credentials` WRITE;
/*!40000 ALTER TABLE `credentials` DISABLE KEYS */;
INSERT INTO `credentials` VALUES ('bharathi','54667',1),('lakshman','997810',1),('rama','1234',1);
/*!40000 ALTER TABLE `credentials` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `milk_purchase`
--

DROP TABLE IF EXISTS `milk_purchase`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `milk_purchase` (
  `date` date NOT NULL,
  `shift` int(11) NOT NULL,
  `sup_code` int(11) NOT NULL,
  `sup_name` varchar(50) NOT NULL,
  `qty` float(10,2) NOT NULL,
  `fat` float(10,2) NOT NULL,
  `snf` float(10,2) NOT NULL,
  `rate` float(10,2) NOT NULL,
  `amount` float(10,2) NOT NULL,
  PRIMARY KEY (`date`,`shift`,`sup_code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `milk_purchase`
--

LOCK TABLES `milk_purchase` WRITE;
/*!40000 ALTER TABLE `milk_purchase` DISABLE KEYS */;
INSERT INTO `milk_purchase` VALUES ('2019-04-24',0,2,'bharath',20.00,6.20,5.50,30.33,606.60);
/*!40000 ALTER TABLE `milk_purchase` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `milk_supplier`
--

DROP TABLE IF EXISTS `milk_supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `milk_supplier` (
  `sup_code` int(11) NOT NULL AUTO_INCREMENT,
  `sup_name` varchar(50) NOT NULL,
  PRIMARY KEY (`sup_code`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `milk_supplier`
--

LOCK TABLES `milk_supplier` WRITE;
/*!40000 ALTER TABLE `milk_supplier` DISABLE KEYS */;
INSERT INTO `milk_supplier` VALUES (2,'Radha'),(3,'Rukmani'),(4,'Bama'),(5,'Sudhama'),(6,'Seetha');
/*!40000 ALTER TABLE `milk_supplier` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `rate`
--

DROP TABLE IF EXISTS `rate`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `rate` (
  `fat` float(10,2) NOT NULL,
  `snf` float(10,2) NOT NULL,
  `rate` float(10,2) NOT NULL,
  PRIMARY KEY (`fat`,`snf`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `rate`
--

LOCK TABLES `rate` WRITE;
/*!40000 ALTER TABLE `rate` DISABLE KEYS */;
INSERT INTO `rate` VALUES (5.70,4.20,21.78),(6.20,5.50,30.33),(6.20,5.55,25.85);
/*!40000 ALTER TABLE `rate` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2019-07-03 23:01:47
