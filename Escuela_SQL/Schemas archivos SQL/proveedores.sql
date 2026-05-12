-- MySQL dump 10.13  Distrib 8.0.26, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: proveedores
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
-- Table structure for table `auditoria_pagos`
--

DROP TABLE IF EXISTS `auditoria_pagos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auditoria_pagos` (
  `auditoria_pagos_id` int NOT NULL AUTO_INCREMENT,
  `ID_pago` varchar(255) DEFAULT NULL,
  `Orden` varchar(255) DEFAULT NULL,
  `Fecha` varchar(255) DEFAULT NULL,
  `Cantidad` varchar(255) DEFAULT NULL,
  `accion_tipo` varchar(255) DEFAULT NULL,
  `accion_fecha` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`auditoria_pagos_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auditoria_pagos`
--

LOCK TABLES `auditoria_pagos` WRITE;
/*!40000 ALTER TABLE `auditoria_pagos` DISABLE KEYS */;
/*!40000 ALTER TABLE `auditoria_pagos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `orden`
--

DROP TABLE IF EXISTS `orden`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `orden` (
  `orden_id` int NOT NULL AUTO_INCREMENT,
  `Fecha` datetime DEFAULT NULL,
  `Orden` int NOT NULL,
  `ID_Proveedor` int NOT NULL,
  `Descripcion` varchar(25) DEFAULT NULL,
  `Total` int NOT NULL,
  `Balance` int NOT NULL,
  PRIMARY KEY (`orden_id`),
  KEY `Orden_index` (`Orden`),
  KEY `ID_Proveedor_index` (`ID_Proveedor`),
  KEY `Total_index` (`Total`),
  KEY `Balance_index` (`Balance`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `orden`
--

LOCK TABLES `orden` WRITE;
/*!40000 ALTER TABLE `orden` DISABLE KEYS */;
INSERT INTO `orden` VALUES (1,'2019-03-16 00:00:00',6788,5969,'Cubeta Masa tipo C',699,0),(2,'2019-05-01 00:00:00',6789,5142,'Verduras mix pack 3',1400,0),(3,'2019-03-31 00:00:00',6790,7045,'Plancha',7800,0),(4,'2019-04-23 00:00:00',6791,9144,'Lacteos varios',1600,0),(5,'2019-03-12 00:00:00',6792,5142,'Verduras temporada pack 5',899,0);
/*!40000 ALTER TABLE `orden` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `pago_orden`
--

DROP TABLE IF EXISTS `pago_orden`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `pago_orden` (
  `pago_orden_id` int NOT NULL AUTO_INCREMENT,
  `Fecha` datetime DEFAULT NULL,
  `ID_pago` int NOT NULL,
  `Orden` int NOT NULL,
  `Cantidad` int NOT NULL,
  PRIMARY KEY (`pago_orden_id`),
  KEY `ID_pago_index` (`ID_pago`),
  KEY `Orden_index` (`Orden`),
  KEY `Cantidad_index` (`Cantidad`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `pago_orden`
--

LOCK TABLES `pago_orden` WRITE;
/*!40000 ALTER TABLE `pago_orden` DISABLE KEYS */;
INSERT INTO `pago_orden` VALUES (1,'2019-03-30 00:00:00',444,6788,150),(2,'2019-04-05 00:00:00',466,6790,600),(3,'2019-04-15 00:00:00',477,6788,150),(4,'2019-04-30 00:00:00',488,6788,150);
/*!40000 ALTER TABLE `pago_orden` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `proveedores`
--

DROP TABLE IF EXISTS `proveedores`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `proveedores` (
  `ID_Proveedor` int NOT NULL,
  `Nombre` varchar(25) DEFAULT NULL,
  `Ciudad` varchar(12) DEFAULT NULL,
  `Estado` varchar(25) DEFAULT NULL,
  `Direccion` varchar(25) DEFAULT NULL,
  `Telefono` bigint NOT NULL,
  `email` varchar(45) DEFAULT NULL,
  `termino_pago` int NOT NULL,
  PRIMARY KEY (`ID_Proveedor`),
  KEY `Telefono_index` (`Telefono`),
  KEY `termino_pago_index` (`termino_pago`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `proveedores`
--

LOCK TABLES `proveedores` WRITE;
/*!40000 ALTER TABLE `proveedores` DISABLE KEYS */;
INSERT INTO `proveedores` VALUES (5142,'Verdurax','Colima','Colima','Jacarandas 33',3124879863,'verdurasfrescas@verdurax.com',15),(5969,'Masas de Occidente','Guadalajara','Jalisco','Av del Roble 233',3366889944,'ventas_as@masasdeoc.com',30),(6425,'Tijuana Lacto','Tijuana','Baja California','Calle Central 209',6648796333,'ventas_clientes@tijuanalacto.com',15),(7045,'Aceros MEX','Monterrey','Nuevo Leon','Boulevard 9000',8147898966,'atencion@acerosmex.com',45),(7271,'Restamarket','Queretaro','Queretaro','Av Mexico 3023',4426669747,'contacto@restamarket.com',30),(8288,'La Planteria','Puebla','Puebla','Carranza 4932',2225553315,'representante33@laplanteria.com',15),(9144,'TOTOA','Tepatitlan','Jalisco','Juarez 11',3784445211,'clientes@TOTOA.com',30);
/*!40000 ALTER TABLE `proveedores` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-07-05 13:31:57
