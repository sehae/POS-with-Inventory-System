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
-- Table structure for table `product`
--

DROP TABLE IF EXISTS `product`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `product` (
  `Product_ID` int NOT NULL AUTO_INCREMENT,
  `Name` varchar(45) DEFAULT NULL,
  `Quantity` int DEFAULT NULL,
  `Threshold_Value` int DEFAULT NULL,
  `Expiry_Date` varchar(45) DEFAULT NULL,
  `Availability` varchar(45) DEFAULT NULL,
  `Category` varchar(45) DEFAULT NULL,
  `Status` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`Product_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `product`
--

LOCK TABLES `product` WRITE;
/*!40000 ALTER TABLE `product` DISABLE KEYS */;
INSERT INTO `product` VALUES (1,'Coca-Cola',12,10,'2024-08-07','In Stock','Beverage','Active'),(2,'San Miguel Light',5,5,'2024-11-08','Low Stock','Beverage','Active'),(3,'San Miguel Apple',36,10,'2024-09-08','In Stock','Beverage','Active'),(4,'San Miguel Pale Pilsen',0,10,'2024-08-12','Out of Stock','Beverage','Disabled'),(5,'Shrimp (200g)',23,5,'2024-07-27','In Stock','Ingredient','Active'),(6,'Scallop (480g)',36,5,'2024-08-03','In Stock','Ingredient','Active'),(7,'Fish cake (1 kg)',0,7,'2024-12-15','Out of Stock','Ingredient','Active'),(8,'Squid (500g)',43,8,'2024-12-23','In Stock','Ingredient','Active'),(9,'Fish Fillet (900g)',9,10,'2024-11-11','Low Stock','Ingredient','Active'),(10,'Coke Zero',69,10,'2024-12-27','In Stock','Beverage','Active'),(11,'Diet Coke',13,10,'2024-10-23','In Stock','Beverage','Active'),(12,'Jinro Soju Strawberry 360ml',30,8,'2024-09-26','In Stock','Beverage','Active'),(13,'Heineken Can 300ml',21,8,'2024-11-26','In Stock','Beverage','Active'),(14,'Tanduay Ice 300ml',37,7,'2024-09-26','In Stock','Beverage','Active');
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

-- Dump completed on 2024-06-13  8:20:31
