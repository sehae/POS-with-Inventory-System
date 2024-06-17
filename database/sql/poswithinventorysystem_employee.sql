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
-- Table structure for table `employee`
--

DROP TABLE IF EXISTS `employee`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `employee` (
  `Employee_ID` int NOT NULL AUTO_INCREMENT,
  `Last_Name` varchar(45) NOT NULL,
  `First_Name` varchar(45) NOT NULL,
  `Department` enum('Cashier','Kitchen') NOT NULL,
  `Contact_Number` varchar(15) NOT NULL,
  `Email` varchar(45) NOT NULL,
  `Username` varchar(45) NOT NULL,
  `Password` longtext NOT NULL,
  `is_active` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`Employee_ID`),
  UNIQUE KEY `Email_UNIQUE` (`Email`),
  UNIQUE KEY `Contact_Number_UNIQUE` (`Contact_Number`),
  UNIQUE KEY `Username_UNIQUE` (`Username`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'Laxamana','Junell','Cashier','09435345234','junlaxy@gmailll.com','JL0201','7868bf998a5e40a87b6c0a9784b276c2379fc242f86be0350739c12a053795ccddd4819d5294354ce1d1a54b70abfa583c2da5d3a3add66a1901fe394acfc01b5016faa3c6ec8860957daf4c83859f7879b2bb4d40de7d8d5052b0c7e21911b5',1),(2,'Gebala','Zek','Kitchen','09435345443','zekgebala@gmail.com','ZG0202','1a981aaf63405d7b1c67680c13f206161247d34f4fbd4ba87af1dae6bac335eaf30882a43aadacb54daf4b9f605c6673763183506ee2e3525c099048f04e198441c847addcac15f719ac931e787b1d0a53a68032da38123e9a80fab0415be2ae',1),(3,'Dom','Bry','Cashier','096544545','00@g.c','BD0203','c25a91878ced8a9d80012a5ffaeee44fd9401e656415a545dcdd76ccdec1b7fd2618508009c9adb9bbb9f93666eac437efa678c0d89e3a39f1c79b7e86751621b7686d62d8d4fd5599c65f46bd92689b24a0f3f2d78cc216afb20109481d7334',1),(4,'Follosco','Zion','Cashier','09754385435','zionf@gmail.cor','ZF0204','82d4bf32e3745eeef1cff7aec8ed3f346e2429c5ff387f8d235a96136526edc64cec5da6a94bd912dd61e2e3f32bdc40b77aa2aa35065f0f209ea04de9808f2d08d660c7fb6cabd5a86c7b6148c5d60c8addb4886342f121f47cd84d4d02fe95',1);
/*!40000 ALTER TABLE `employee` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-17 22:02:09
