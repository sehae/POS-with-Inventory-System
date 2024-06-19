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
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `User_ID` int NOT NULL AUTO_INCREMENT,
  `Last_Name` varchar(45) NOT NULL,
  `First_Name` varchar(45) NOT NULL,
  `User_Type` enum('Admin','Employee','System') NOT NULL,
  `Department` enum('Admin','Cashier','Kitchen') NOT NULL,
  `Contact_Number` varchar(15) NOT NULL,
  `Email` varchar(255) NOT NULL,
  `Username` varchar(45) NOT NULL,
  `Password` longtext NOT NULL,
  `is_active` enum('Enabled','Disabled') NOT NULL DEFAULT 'Enabled',
  PRIMARY KEY (`User_ID`),
  UNIQUE KEY `Contact_Number_UNIQUE` (`Contact_Number`),
  UNIQUE KEY `Email_UNIQUE` (`Email`),
  UNIQUE KEY `Username_UNIQUE` (`Username`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES (1,'Villatura','Leah Desiree','Admin','Admin','09563847921','ld.kirbble@gmail.com','LV0101','d9d6aeb5c9c61dd379c00275a1fdbac33dcb830575cdec26df851efe1d10b70dfa4c904776a993beccb5a47c481cb9a5e7b9779d860d791460ae5281cb54042c6fbc5cc8ad9bf93e87e6d63fe9ef8ec66b5179f255a3390ebe350dc86c07e114','Enabled'),(2,'Faurillo','Ymnwl Jan','Employee','Kitchen','09317264187','lpoeprwa@gmail.coekag','YF0102','dc7fcaca23ca4a498413bfec08576e79058366702cc09ce5bd71e75cac9c95b708a04d41e9c1d48f880a356593b606810b8174f4a0a36002b2033703e5ed4ba2185bb0f8b6f3af2cea72856214f6dd600c415d03b5b7b67f58411547ff76c0e6','Enabled'),(3,'Tiamzon','Bryan Dominick','Employee','Cashier','09317543534','ewareraw@geaw.comeg','BT0103','20117b7b5f8561b559c3c9822c343ab9a9538c6cb34def75f51c900350874901fcccb55e1f9f9b7ebf9c45281c2696f22846c6f76730c40b50ddfeb0ce312042dccd75cebb85f3c0cf2125ebcc47ff2b1cb7f0b2e852a28a0fc4e222da1c109f','Enabled');
/*!40000 ALTER TABLE `user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-18 23:04:44
