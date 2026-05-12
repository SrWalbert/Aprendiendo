-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: periodos
-- ------------------------------------------------------
-- Server version	8.0.26

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `periodo1`
--

DROP TABLE IF EXISTS `periodo1`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `periodo1` (
  `periodo1_id` int NOT NULL AUTO_INCREMENT,
  `Fecha` datetime DEFAULT NULL,
  `ID_Empleado` varchar(12) DEFAULT NULL,
  `Local` varchar(5) DEFAULT NULL,
  `Turno_completo` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`periodo1_id`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `periodo1`
--

LOCK TABLES `periodo1` WRITE;
/*!40000 ALTER TABLE `periodo1` DISABLE KEYS */;
INSERT INTO `periodo1` VALUES (1,'2019-09-03 00:00:00','5728566','A','SI'),(2,'2019-07-16 00:00:00','9611338','A','NO'),(3,'2019-08-27 00:00:00','3833745','B','NO'),(4,'2019-12-15 00:00:00','5942572','D','NO'),(5,'2019-07-30 00:00:00','4245367','C','SI'),(6,'2019-10-25 00:00:00','6332756','C','SI'),(7,'2019-12-14 00:00:00','5942572','B','SI'),(8,'2019-08-14 00:00:00','9922377','C','SI'),(9,'2019-12-01 00:00:00','6931035','B','SI'),(10,'2019-06-08 00:00:00','6931035','B','SI'),(11,'2019-07-25 00:00:00','2310967','B','SI');
/*!40000 ALTER TABLE `periodo1` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `periodo2`
--

DROP TABLE IF EXISTS `periodo2`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `periodo2` (
  `periodo2_id` int NOT NULL AUTO_INCREMENT,
  `Fecha` datetime DEFAULT NULL,
  `ID_Empleado` int NOT NULL,
  `Local` varchar(5) DEFAULT NULL,
  `Turno_completo` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`periodo2_id`),
  KEY `ID_Empleado_index` (`ID_Empleado`)
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `periodo2`
--

LOCK TABLES `periodo2` WRITE;
/*!40000 ALTER TABLE `periodo2` DISABLE KEYS */;
INSERT INTO `periodo2` VALUES (1,'2018-11-18 00:00:00',1111222,'A','SI'),(2,'2018-09-17 00:00:00',9922377,'A','NO'),(3,'2018-10-18 00:00:00',3833745,'B','NO'),(4,'2018-10-30 00:00:00',2520477,'D','NO'),(5,'2018-05-16 00:00:00',9611338,'C','SI'),(6,'2018-12-15 00:00:00',4245367,'C','SI'),(7,'2018-07-28 00:00:00',5942572,'B','SI'),(8,'2018-10-05 00:00:00',2630867,'C','SI'),(9,'2018-04-20 00:00:00',2310967,'B','SI'),(10,'2018-06-08 00:00:00',6931035,'B','SI'),(11,'2018-08-22 00:00:00',6332756,'B','SI');
/*!40000 ALTER TABLE `periodo2` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-05 13:48:08
