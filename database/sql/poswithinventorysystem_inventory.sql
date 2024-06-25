-- MySQL dump 10.13  Distrib 8.0.36, for Win64 (x86_64)
--
-- Host: localhost    Database: poswithinventorysystem
-- ------------------------------------------------------
-- Server version	8.0.37

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
-- Table structure for table `inventory`
--

DROP TABLE IF EXISTS `inventory`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `inventory` (
  `Inventory_ID` int NOT NULL AUTO_INCREMENT,
  `Product_ID` varchar(45) NOT NULL,
  `Supplier_ID` int DEFAULT NULL,
  `Selling_Cost` decimal(10,2) DEFAULT NULL,
  `Buying_cost` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`Inventory_ID`),
  KEY `fk_ProductID_inventory` (`Product_ID`),
  KEY `fk_SupplierID_inventory` (`Supplier_ID`),
  CONSTRAINT `fk_product` FOREIGN KEY (`Product_ID`) REFERENCES `product` (`Product_ID`),
  CONSTRAINT `fk_ProductID_inventory` FOREIGN KEY (`Product_ID`) REFERENCES `product` (`Product_ID`),
  CONSTRAINT `fk_supplier` FOREIGN KEY (`Supplier_ID`) REFERENCES `supplier` (`Supplier_ID`),
  CONSTRAINT `fk_SupplierID_inventory` FOREIGN KEY (`Supplier_ID`) REFERENCES `supplier` (`Supplier_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `inventory`
--

LOCK TABLES `inventory` WRITE;
/*!40000 ALTER TABLE `inventory` DISABLE KEYS */;
INSERT INTO `inventory` VALUES (1,'PRD001',3,50.00,35.00),(2,'PRD002',3,100.00,50.00),(3,'PRD003',3,100.00,50.00),(4,'PRD004',3,120.00,50.00),(5,'PRD005',1,NULL,NULL),(6,'PRD006',1,NULL,NULL),(7,'PRD007',1,NULL,NULL),(8,'PRD008',1,NULL,NULL),(9,'PRD009',1,NULL,NULL),(10,'PRD010',3,55.00,35.00),(11,'PRD011',3,60.00,35.00),(12,'PRD012',3,200.00,90.00),(13,'PRD013',3,180.00,150.00),(14,'PRD014',3,95.00,50.00),(15,'PRD015',4,50.00,35.00);
/*!40000 ALTER TABLE `inventory` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-25 20:01:52
