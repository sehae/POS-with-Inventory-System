-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: 127.0.0.1    Database: poswithinventorysystem
-- ------------------------------------------------------
-- Server version	8.4.0

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
-- Table structure for table `add_on`
--

DROP TABLE IF EXISTS `add_on`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `add_on` (
  `Add_On_ID` int NOT NULL AUTO_INCREMENT,
  `Order_ID` varchar(45) DEFAULT NULL,
  `Product_Details` json DEFAULT NULL,
  PRIMARY KEY (`Add_On_ID`),
  KEY `Order_ID` (`Order_ID`),
  CONSTRAINT `add_on_ibfk_1` FOREIGN KEY (`Order_ID`) REFERENCES `order` (`Order_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `add_on`
--

LOCK TABLES `add_on` WRITE;
/*!40000 ALTER TABLE `add_on` DISABLE KEYS */;
INSERT INTO `add_on` VALUES (1,'POS20240617001','[{\"quantity\": 5, \"product_id\": \"PRD001\"}]'),(2,'POS20240617002','[{\"quantity\": 5, \"product_id\": \"PRD002\"}, {\"quantity\": 3, \"product_id\": \"PRD004\"}]'),(4,'POS20240619001','[{\"quantity\": 3, \"product_id\": \"PRD003\"}, {\"quantity\": 4, \"product_id\": \"PRD013\"}]'),(5,'POS20240618003','[{\"quantity\": 2, \"product_id\": \"PRD015\"}]');
/*!40000 ALTER TABLE `add_on` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-25  8:03:27
