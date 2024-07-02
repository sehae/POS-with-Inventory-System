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
  `Payment_Method` varchar(45) NOT NULL,
  `Cash_Amount` decimal(10,2) DEFAULT NULL,
  `reference_id` varchar(45) DEFAULT NULL,
  `Discount_Type` varchar(45) DEFAULT NULL,
  `Priority_Order` varchar(45) DEFAULT NULL,
  `Subtotal_Amount` decimal(10,2) DEFAULT NULL,
  `VAT_Amount` decimal(10,2) DEFAULT NULL,
  `Discount_Amount` decimal(10,2) DEFAULT NULL,
  `Change_Amount` decimal(10,2) DEFAULT NULL,
  `Package_Total_Amount` decimal(10,2) DEFAULT NULL,
  `Add_Ons_Total_Amount` varchar(45) DEFAULT NULL,
  `Cash_Register` varchar(45) DEFAULT NULL,
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
INSERT INTO `order` VALUES ('POS20240630001','2024-06-30','22:58','2539.04','Completed',2,NULL,'Bryan','None',3,NULL,'Package','Cash',3000.00,NULL,'Regular','Non-priority',2267.00,272.04,0.00,460.96,2127.00,'140.00',NULL),('POS20240630002','2024-06-30','23:04',NULL,'Cancelled',1,NULL,'Francesca','Tomato soup',2,NULL,'Package','Pending',NULL,NULL,NULL,'Non-priority',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('POS20240630003','2024-06-30','23:05','1588.16','Completed',1,NULL,'Lebron','Plain soup',2,NULL,'Package','Cash',3000.00,NULL,'Regular','Non-priority',1418.00,170.16,0.00,1411.84,1418.00,'0.00',NULL),('POS20240630004','2024-06-30','23:05','168.00','Completed',NULL,NULL,'Leo','',NULL,NULL,'Add-ons only','Cash',300.00,NULL,'Regular','Priority',150.00,18.00,0.00,132.00,0.00,'150.00',NULL),('POS20240630005','2024-06-30','23:06','2762.19','Completed',3,2,'Leah','Mala soup',3,NULL,'Package','Cash',3000.00,NULL,'PWD','Non-priority',3027.00,290.59,605.40,237.81,3027.00,'0.00',NULL),('POS20240630006','2024-06-30','23:07','4923.52','Completed',3,NULL,'Sukuna','Plain soup',4,NULL,'Package','Cash',5000.00,NULL,'Regular','Priority',4396.00,527.52,0.00,76.48,4036.00,'360.00',NULL),('POS20240701001','2024-07-01','05:30','2382.24','Completed',2,1,'Dessi','',3,NULL,'Package','Cash',2400.00,NULL,'Regular','Priority',2127.00,255.24,0.00,17.76,2127.00,'0.00',NULL),('POS20240701002','2024-07-01','05:33','2382.24','Completed',1,1,'Test','Mala soup',3,NULL,'Package','Cash',2400.00,NULL,'Regular','Non-priority',2127.00,255.24,0.00,17.76,2127.00,'0.00',NULL),('POS20240701003','2024-07-01','05:40','3390.24','Completed',3,1,'Josie','Plain soup',3,NULL,'Package','Cash',3400.00,NULL,'Regular','Non-priority',3027.00,363.24,0.00,9.76,3027.00,'0.00',NULL),('POS20240701004','2024-07-01','05:42','3849.22','Completed',3,1,'Jote','Plain soup',4,NULL,'Package','Cash',4000.00,NULL,'PWD','Priority',4296.00,412.42,859.20,150.78,4036.00,'260.00',NULL),('POS20240701005','2024-07-01','05:43','2382.24','Completed',2,1,'Kendrick','',3,NULL,'Package','Cash',2400.00,NULL,'Regular','Priority',2127.00,255.24,0.00,17.76,2127.00,'0.00',NULL),('POS20240701006','2024-07-01','05:45','794.08','Completed',1,1,'Aubrey','Plain soup',1,NULL,'Package','Cash',800.00,NULL,'Regular','Priority',709.00,85.08,0.00,5.92,709.00,'0.00',NULL),('POS20240701007','2024-07-01','08:45','3390.24','Completed',3,1,'Yohan','Suan la soup',3,NULL,'Package','Cash',3500.00,NULL,'Regular','Non-priority',3027.00,363.24,0.00,109.76,3027.00,'0.00',NULL),('POS20240701008','2024-07-01','08:49','1588.16','Completed',1,1,'Tim','Mala soup',2,NULL,'Package','Cash',1600.00,NULL,'Regular','Non-priority',1418.00,170.16,0.00,11.84,1418.00,'0.00',NULL),('POS20240701009','2024-07-01','08:56','2260.16','Completed',3,1,'Santoes','Suan la soup',2,NULL,'Package','Cash',2300.00,NULL,'Regular','Non-priority',2018.00,242.16,0.00,39.84,2018.00,'0.00',NULL),('POS20240701010','2024-07-01','09:01','3390.24','Completed',3,1,'Lil Pump','Plain soup',3,NULL,'Package','Cash',3400.00,NULL,'Regular','Priority',3027.00,363.24,0.00,9.76,3027.00,'0.00',NULL),('POS20240701011','2024-07-01','09:09','2360.16','Completed',3,3,'Karren','Mala soup',2,NULL,'Package','Cash',2400.00,NULL,'Regular','Non-priority',2018.00,242.16,0.00,39.84,2018.00,'0.00',NULL),('POS20240701012','2024-07-01','09:18','3390.24','Completed',3,NULL,'Bulok Pc','Mala soup',3,NULL,'Package','Cash',3400.00,NULL,NULL,'Non-priority',3027.00,363.24,0.00,9.76,3027.00,'0.00',NULL),('POS20240701013','2024-07-01','09:20','794.08','Completed',1,1,'Yohan','Tomato soup',1,NULL,'Package','Cash',800.00,NULL,'Regular','Non-priority',709.00,85.08,0.00,5.92,709.00,'0.00',NULL),('POS20240701014','2024-07-01','09:29','1588.16','Completed',1,1,'Cheska','Plain soup',2,NULL,'Package','Cash',1600.00,NULL,'Regular','Non-priority',1418.00,170.16,0.00,11.84,1418.00,'0.00',NULL),('POS20240702001','2024-07-02','02:32',NULL,'Cancelled',NULL,NULL,'Bryan Tiamzon','',NULL,NULL,'Add-ons only','Pending',NULL,NULL,NULL,'Priority',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('POS20240702002','2024-07-02','05:22',NULL,'Pending',2,NULL,'Leah','',3,NULL,'Package','Pending',NULL,NULL,NULL,'Priority',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('POS20240702003','2024-07-02','05:27',NULL,'Pending',3,NULL,'Aspas','Suan la soup',3,NULL,'Package','Pending',NULL,NULL,NULL,'Priority',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('POS20240702004','2024-07-02','06:16',NULL,'Waiting for Timer',3,NULL,'Cheska','Tomato soup',3,NULL,'Package','Pending',NULL,NULL,NULL,'Non-Priority',NULL,NULL,NULL,NULL,NULL,NULL,NULL),('POS20240702005','2024-07-02','06:16',NULL,'Pending',NULL,NULL,'Aubrey','',NULL,NULL,'Add-ons only','Pending',NULL,NULL,NULL,'Non-Priority',NULL,NULL,NULL,NULL,NULL,NULL,NULL);
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

-- Dump completed on 2024-07-02  7:48:49
