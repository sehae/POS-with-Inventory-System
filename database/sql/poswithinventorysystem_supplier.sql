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
-- Table structure for table `supplier`
--

DROP TABLE IF EXISTS `supplier`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `supplier` (
  `Supplier_ID` int NOT NULL AUTO_INCREMENT,
  `Supplier_Name` varchar(45) DEFAULT NULL,
  `Contact_Number` varchar(45) DEFAULT NULL,
  `Email` varchar(45) DEFAULT NULL,
  `Address` varchar(45) DEFAULT NULL,
  `Status` varchar(45) NOT NULL,
  PRIMARY KEY (`Supplier_ID`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supplier`
--

LOCK TABLES `supplier` WRITE;
/*!40000 ALTER TABLE `supplier` DISABLE KEYS */;
INSERT INTO `supplier` VALUES (1,'Fresh Foods Inc.','09456123481','info@tiamzonfoodco.com','273 Harvard Avenue, Pasig','Active'),(2,'Farm Fresh Produce','09987654321','sales@farmfreshproduce.com','5678 Rizal Avenue, Santa Cruz, Manila','Active'),(3,'Gourmet Grocers','09222345678','orders@gourmetgrocers.com','1356 Gen. Luna Street, Intramuros, Manila','Active'),(4,'Global Food Distributors','09356789101','info@globalfooddist.com','345 P. Burgos Street, Makati','Active'),(5,'Organic Harvest','09051122334','info@organicharvest.com','4827 A. Bonifacio Avenue, Cainta','Active'),(6,'Cocacococo','09183345566','info@cocacococo.com','90 E. Rodriguez Sr. Avenue, Quezon City','Disabled'),(7,'Global Fresh Seafood','09456123481','info@globalfreshseafood.com','679 Kalayaan Avenue, Makati','Active'),(8,'Tiamzon Food Supplies Co.','09456123481','info@tiamzonfoodco.com','273 Harvard Avenue, Pasig','Active'),(9,'Villatura Softdrink Supply Inc.','09123456789','info@villaturasoftdrinksup.com','693 Araneta Avenue, Cubao, Quezon City','Active'),(10,'Faurillo Fresh Vegatables Co.','09456123469','info@faurillofreshveg.com','428 Rizal Avenue, Taguig','Active'),(11,'Agagon Meat Supplier','09456123481','info@agagonmeatsupplier.com','168 Kabataan Avenue, Marikina','Disabled'),(12,'Aspas Condiments Supplier','09456123481','info@aspascondsup.com','428 Rizal Avenue, Taguig','Disabled');
/*!40000 ALTER TABLE `supplier` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-28  9:45:01
