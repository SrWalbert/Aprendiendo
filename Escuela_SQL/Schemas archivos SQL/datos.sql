-- MySQL dump 10.13  Distrib 8.0.43, for Win64 (x86_64)
--
-- Host: localhost    Database: datos
-- ------------------------------------------------------
-- Server version	8.4.6

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
-- Table structure for table `empleados`
--

DROP TABLE IF EXISTS `empleados`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `empleados` (
  `ID_empleado` int NOT NULL,
  `Nombre` varchar(12) DEFAULT NULL,
  `Apellido` varchar(12) DEFAULT NULL,
  `Telefono` varchar(12) DEFAULT NULL,
  `Edad` int NOT NULL,
  `Domicilio` varchar(25) DEFAULT NULL,
  `ID_Gerente` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`ID_empleado`),
  KEY `Edad_index` (`Edad`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `empleados`
--

LOCK TABLES `empleados` WRITE;
/*!40000 ALTER TABLE `empleados` DISABLE KEYS */;
INSERT INTO `empleados` VALUES (1111222,'Alberto','Barrientos','34766613',26,'Federal 233','5942572'),(2310967,'Jairo','Mira','36403810',29,'Calle 25 interior 2','5942572'),(2520477,'Egidio','Lopez','33444383',24,'Rosas 996','5942572'),(2630867,'Elena','Atehortua','35581732',37,'Sierra del tigre 299','5942572'),(3833745,'Maria','Zapata','35354455',34,'Boulevard 85','5942572'),(4245367,'Alexandra','Zapata','33467136',31,'Ingenieros 234','5942572'),(5942572,'Jesus','Agudelo','34616222',35,NULL,NULL),(6332756,'Reinaldo','Gonzalez','36642727',43,'Vallarta 711','5942572'),(6931035,'Albeiro','Villa','33631010',39,'Carniceros 233','5942572'),(9611338,'Haygnes','Ortiz','35400189',27,'General Diaz 343','5942572'),(9922377,'Alexander','Martinez','36554872',28,'Camino viejo 123','5942572');
/*!40000 ALTER TABLE `empleados` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ingredientes`
--

DROP TABLE IF EXISTS `ingredientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ingredientes` (
  `ingredientes_id` int NOT NULL AUTO_INCREMENT,
  `Ingredientes` varchar(12) DEFAULT NULL,
  `clave_ingrediente` varchar(5) DEFAULT NULL,
  `precio_porcion` int DEFAULT NULL,
  PRIMARY KEY (`ingredientes_id`),
  KEY `precio_porcion_index` (`precio_porcion`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ingredientes`
--

LOCK TABLES `ingredientes` WRITE;
/*!40000 ALTER TABLE `ingredientes` DISABLE KEYS */;
INSERT INTO `ingredientes` VALUES (1,'Pepperoni','pep',8),(2,'Cebolla','ceb',5),(3,'Pimiento','pim',10),(4,'Salchicha','sal',5),(5,'Piña','piñ',8),(6,'queso','que',5);
/*!40000 ALTER TABLE `ingredientes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `local`
--

DROP TABLE IF EXISTS `local`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `local` (
  `ID_Local` int NOT NULL,
  `Letra_zona` varchar(5) DEFAULT NULL,
  `Direccion` varchar(45) DEFAULT NULL,
  `Telefono` int NOT NULL,
  PRIMARY KEY (`ID_Local`),
  KEY `Telefono_index` (`Telefono`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `local`
--

LOCK TABLES `local` WRITE;
/*!40000 ALTER TABLE `local` DISABLE KEYS */;
INSERT INTO `local` VALUES (1,'A','Av de las Rosas 123',357894),(2,'B','Calle poniente manzana 4',377896),(3,'C','Insurgentes 558',347899),(4,'D','Rinconada de Magnolias 409',378341),(5,'E','Americas 299',0);
/*!40000 ALTER TABLE `local` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `productos`
--

DROP TABLE IF EXISTS `productos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `productos` (
  `productos_id` int NOT NULL AUTO_INCREMENT,
  `Producto` varchar(12) DEFAULT NULL,
  `clave_producto` varchar(5) DEFAULT NULL,
  PRIMARY KEY (`productos_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `productos`
--

LOCK TABLES `productos` WRITE;
/*!40000 ALTER TABLE `productos` DISABLE KEYS */;
INSERT INTO `productos` VALUES (1,'Pizza','pzz'),(2,'Calzone','clz'),(3,'Quesadilla','qsd'),(4,'Burrito','brr');
/*!40000 ALTER TABLE `productos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `tamaños`
--

DROP TABLE IF EXISTS `tamaños`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `tamaños` (
  `tamaños_id` int NOT NULL AUTO_INCREMENT,
  `Tamaño` varchar(5) DEFAULT NULL,
  `Descripcion` varchar(12) DEFAULT NULL,
  `Tamaño_en_CMS` int NOT NULL,
  PRIMARY KEY (`tamaños_id`),
  KEY `Tamaño_en_CMS_index` (`Tamaño_en_CMS`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `tamaños`
--

LOCK TABLES `tamaños` WRITE;
/*!40000 ALTER TABLE `tamaños` DISABLE KEYS */;
INSERT INTO `tamaños` VALUES (1,'P','Pequeño',20),(2,'M','Mediano',30),(3,'G','Grande',40),(4,'EG','Extra Grande',50);
/*!40000 ALTER TABLE `tamaños` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ventas`
--

DROP TABLE IF EXISTS `ventas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ventas` (
  `ventas_id` int NOT NULL AUTO_INCREMENT,
  `Fecha` datetime DEFAULT NULL,
  `ID_local` int NOT NULL,
  `clave_producto` varchar(5) DEFAULT NULL,
  `venta` int NOT NULL,
  `venta_empleado` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`ventas_id`),
  KEY `ID_local_index` (`ID_local`),
  KEY `venta_index` (`venta`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas`
--

LOCK TABLES `ventas` WRITE;
/*!40000 ALTER TABLE `ventas` DISABLE KEYS */;
INSERT INTO `ventas` VALUES (1,'2018-11-18 00:00:00',2,'pzz',1302,'2630867'),(2,'2018-09-17 00:00:00',2,'clz',953,'2310967'),(3,'2018-10-18 00:00:00',4,'brr',1286,'6931035'),(4,'2018-10-30 00:00:00',1,'brr',889,'9922377'),(5,'2018-05-16 00:00:00',1,'qsd',495,'2520477'),(6,'2018-12-15 00:00:00',3,'pzz',544,'9611338'),(7,'2018-07-28 00:00:00',4,'pzz',1444,'6332756'),(8,'2018-10-05 00:00:00',1,'pzz',435,'2520477'),(9,'2018-04-20 00:00:00',1,'qsd',1203,'9922377'),(10,'2018-06-08 00:00:00',1,'brr',1038,'6332756'),(11,'2018-08-22 00:00:00',1,'brr',404,'3833745'),(12,'2019-09-03 00:00:00',1,'pzz',1362,'5728566'),(13,'2019-07-16 00:00:00',3,'qsd',1054,'2310967'),(14,'2019-08-27 00:00:00',3,'clz',303,'3833745'),(15,'2019-12-15 00:00:00',1,'brr',871,'2520477'),(16,'2019-07-30 00:00:00',3,'brr',1062,'5728566'),(17,'2019-10-25 00:00:00',1,'pzz',1376,'6332756'),(18,'2019-12-14 00:00:00',3,'pzz',957,'2310967'),(19,'2019-08-14 00:00:00',2,'clz',972,'2310967'),(20,'2019-12-01 00:00:00',1,'pzz',1455,'2310967'),(21,'2019-06-08 00:00:00',4,'qsd',497,'5728566'),(22,'2019-07-25 00:00:00',3,'clz',1179,'2310967');
/*!40000 ALTER TABLE `ventas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `ventas_detalle`
--

DROP TABLE IF EXISTS `ventas_detalle`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `ventas_detalle` (
  `ID_venta` int NOT NULL,
  `Tipo` varchar(12) DEFAULT NULL,
  PRIMARY KEY (`ID_venta`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `ventas_detalle`
--

LOCK TABLES `ventas_detalle` WRITE;
/*!40000 ALTER TABLE `ventas_detalle` DISABLE KEYS */;
INSERT INTO `ventas_detalle` VALUES (1,'Local'),(2,'Llevar'),(3,'Llevar'),(4,'Local'),(5,'LLevar'),(6,'Local'),(7,'LLevar'),(8,'Local'),(9,'Local'),(10,'Llevar'),(11,'Llevar'),(12,'Llevar'),(13,'Local'),(14,'Local'),(15,'Llevar'),(16,'Llevar'),(17,'Llevar'),(18,'Local'),(19,'Llevar'),(20,'Llevar'),(21,'Local'),(22,'Llevar');
/*!40000 ALTER TABLE `ventas_detalle` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2025-11-18 23:08:23
