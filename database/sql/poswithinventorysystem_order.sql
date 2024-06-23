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
INSERT INTO `order` VALUES ('POS20240617001','2024-06-17','11:15',NULL,'Pending',2,NULL,'Vanessa Kang',NULL,1,NULL,'Package'),('POS20240617002','2024-06-17','11:43',NULL,'Pending',1,2,'Kim Minji','Mala soup',4,NULL,'Package'),('POS20240617003','2024-06-17','11:50',NULL,'Pending',3,NULL,'Hanni Pham','Mala soup',3,NULL,'Package'),('POS20240617004','2024-06-17','11:55',NULL,'Pending',1,1,'Lee Hyein','Suan la soup',4,NULL,'Package'),('POS20240617005','2024-06-17','12:19',NULL,'Pending',1,NULL,'Danielle Marsh','Plain soup',6,NULL,'Package'),('POS20240617006','2024-06-17','12:27',NULL,'Pending',3,NULL,'Yoo Ji Min','Suan la soup',2,NULL,'Package'),('POS20240617007','2024-06-17','12:38',NULL,'Pending',1,NULL,'Uchinaga Aeri','Tomato soup',3,NULL,'Package'),('POS20240617008','2024-06-17','12:46',NULL,'Pending',1,NULL,'Kim Jeong','Mala soup',4,NULL,'Package'),('POS20240617009','2024-06-17','12:52',NULL,'Pending',2,NULL,'Ning Yizhuo',NULL,3,NULL,'Package'),('POS20240617010','2024-06-17','13:03',NULL,'Pending',3,2,'Hwang Yeji','Mala soup',5,NULL,'Package'),('POS20240617011','2024-06-17','13:15',NULL,'Pending',1,NULL,'Shin Ryujin','Suan la soup',2,NULL,'Package'),('POS20240617012','2024-06-17','13:22',NULL,'Pending',1,1,'Shin Yuna','Mala soup',4,NULL,'Package'),('POS20240617013','2024-06-17','20:31',NULL,'Pending',2,NULL,'Bryan Tiamzon','',3,NULL,'Package'),('POS20240617014','2024-06-17','20:35',NULL,'Pending',3,NULL,'Leah Villatura','Tomato soup',5,NULL,'Package'),('POS20240617015','2024-06-17','20:48',NULL,'Pending',1,NULL,'Ymnwl Faurillo','Plain soup',1,NULL,'Package'),('POS20240617016','2024-06-17','20:48',NULL,'Pending',2,NULL,'Jose Tan','',2,NULL,'Package'),('POS20240617017','2024-06-17','20:51',NULL,'Pending',2,NULL,'Nathan Paje','',5,NULL,'Package'),('POS20240617018','2024-06-17','20:57',NULL,'Cancelled',2,NULL,'Jao Agagon','',3,NULL,'Package'),('POS20240618001','2024-06-18','04:41',NULL,'Pending',2,NULL,'Robert Balite','',2,NULL,'Package'),('POS20240618002','2024-06-18','06:13',NULL,'Pending',1,NULL,'Harvey Hernandez','Mala soup',3,NULL,'Package'),('POS20240618003','2024-06-18','16:02',NULL,'Pending',3,NULL,'Kim Seokjin','Suan la soup',7,NULL,'Package'),('POS20240619001','2024-06-19','08:59',NULL,'Pending',3,NULL,'Karren Lara','Suan la soup',5,NULL,'Package'),('POS20240619002','2024-06-19','11:08',NULL,'Pending',1,NULL,'Yohan Santos','Mala soup',5,NULL,'Package'),('POS20240619003','2024-06-19','11:13',NULL,'Pending',3,NULL,'Narpim Ngek','Suan la soup',6,NULL,'Package');
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

-- Dump completed on 2024-06-23 13:08:21
