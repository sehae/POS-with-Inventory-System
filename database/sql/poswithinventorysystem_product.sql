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
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `Product_ID` varchar(45) NOT NULL,
  `Date` varchar(45) DEFAULT NULL,
  `Time` varchar(45) DEFAULT NULL,
  `Name` varchar(45) DEFAULT NULL,
  `Quantity` int DEFAULT NULL,
  `Threshold_Value` int DEFAULT NULL,
  `Expiry_Date` varchar(45) DEFAULT NULL,
  `Availability` varchar(45) DEFAULT NULL,
  `Category` varchar(45) DEFAULT NULL,
  `Status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Product_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES ('PRD001','2024-06-20','11:15','Coca-Cola (330ml)',52,10,'2024-11-25','In Stock','Beverage','Active'),('PRD002','2024-06-20','11:17','San Miguel Light (330ml)',64,10,'2024-12-09','In Stock','Beverage','Active'),('PRD003','2024-06-20','11:22','San Miguel Apple (330ml)',75,10,'2024-10-14','In Stock','Beverage','Active'),('PRD004','2024-06-20','11:34','San Miguel Pale Pilsen (330ml)',32,10,'2024-09-17','In Stock','Beverage','Disabled'),('PRD005','2024-06-20','13:22','Shrimp (200g)',50,10,'2024-07-08','In Stock','Ingredient','Active'),('PRD006','2024-06-21','15:07','Scallop (480g)',50,10,'2024-07-03','In Stock','Ingredient','Active'),('PRD007','2024-06-21','16:22','Fish cake (1kg)',50,10,'2024-07-01','In Stock','Ingredient','Active'),('PRD008','2024-06-21','16:24','Squid (500g)',50,10,'2024-06-28','In Stock','Ingredient','Active'),('PRD009','2024-06-21','16:28','Fish Fillet (900g)',50,10,'2024-06-29','In Stock','Ingredient','Active'),('PRD010','2024-06-21','17:54','Coke Zero (330ml)',7,10,'2025-05-03','Low Stock','Beverage','Active'),('PRD011','2024-06-22','09:30','Diet Coke (330ml)',4,10,'2025-02-22','Low Stock','Beverage','Disabled'),('PRD012','2024-06-22','09:56','Jinro Soju Strawberry (360ml)',0,10,'2024-08-06','Out of Stock','Beverage','Active'),('PRD013','2024-06-22','10:32','Heineken Can (330ml)',39,10,'2024-07-09','In Stock','Beverage','Active'),('PRD014','2024-06-22','11:02','Tanduay Ice (330ml)',0,10,'2024-07-19','Out of Stock','Beverage','Active'),('PRD015','2024-06-22','11:07','Mountain Dew (350ml)',44,10,'2024-12-05','In Stock','Beverage','Active');
/*!40000 ALTER TABLE `product` ENABLE KEYS */;
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
