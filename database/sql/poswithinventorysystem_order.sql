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
-- Table structure for table `order`
--

DROP TABLE IF EXISTS `order`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `order` (
  `Order_ID` varchar(45) NOT NULL,
  `Date` varchar(45) DEFAULT NULL,
  `Time` varchar(45) DEFAULT NULL,
  `Total_Amount` varchar(45) DEFAULT NULL,
  `Payment_Status` varchar(45) DEFAULT NULL,
  `Package_ID` int DEFAULT NULL,
  `Leftover_ID` int DEFAULT NULL,
  `Customer_Name` varchar(45) DEFAULT NULL,
  `Soup_Variation` varchar(45) DEFAULT NULL,
  `Guest_Pax` int DEFAULT NULL,
  `Time_Status` varchar(45) DEFAULT NULL,
  `Order_Type` varchar(45) DEFAULT NULL,
  `Payment_Method` varchar(45) NOT NULL,
  `Cash_Amount` decimal(10,2) DEFAULT NULL,
  `Reference_ID` int DEFAULT NULL,
  `Discount_Type` varchar(45) DEFAULT NULL,
  `Priority_Order` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Order_ID`),
  KEY `fk_Package_ID` (`Package_ID`),
  KEY `fk_leftover_id` (`Leftover_ID`),
  CONSTRAINT `fk_leftover_id` FOREIGN KEY (`Leftover_ID`) REFERENCES `leftover` (`Leftover_ID`),
  CONSTRAINT `fk_Package_ID` FOREIGN KEY (`Package_ID`) REFERENCES `package` (`Package_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `order`
--

LOCK TABLES `order` WRITE;
/*!40000 ALTER TABLE `order` DISABLE KEYS */;
INSERT INTO `order` VALUES ('POS20240626001','2024-06-26','17:51','4889.12','Completed',3,3,'Jose Tan','Plain soup',5,'Completed','Package','Cash',6000.00,NULL,'Senior/PWD',NULL),('POS20240626002','2024-06-26','17:52','179.2','Completed',NULL,1,'Leah Villatura',NULL,NULL,'Completed','Add-ons only','Cash',200.00,987654321,'Senior/PWD',NULL),('POS20240626003','2024-06-26','19:11','112.0','Completed',NULL,NULL,'Aspas Zeyk',NULL,NULL,'Completed','Add-ons only','GCash',120.00,987654321,NULL,NULL),('POS20240626004','2024-06-26','19:17','280.0','Completed',NULL,NULL,'Yohan Santos',NULL,NULL,'Completed','Add-ons only','Pending',NULL,NULL,NULL,NULL),('POS20240626005','2024-06-26','19:23','616.00','Completed',NULL,NULL,'Post Malone',NULL,NULL,'Completed','Add-ons only','Cash',700.00,NULL,NULL,NULL),('POS20240626006','2024-06-26','19:24','224.00','Completed',NULL,NULL,'Aubrey Graham',NULL,NULL,'Completed','Add-ons only','GCash',0.00,987654321,NULL,NULL),('POS20240626007','2024-06-26','20:19',NULL,'Pending',1,2,'Leah Villatura','Plain soup',2,NULL,'Package','Cash',2400.00,NULL,'Senior/PWD',NULL),('POS20240626008','2024-06-26','21:07',NULL,'Pending',1,NULL,'Bryan Tiamzon','Tomato soup',2,NULL,'Package','Pending',NULL,NULL,NULL,NULL);
/*!40000 ALTER TABLE `order` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-27 10:51:32
