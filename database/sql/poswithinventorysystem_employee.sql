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
  `is_active` tinyint NOT NULL DEFAULT '1',
  PRIMARY KEY (`Employee_ID`),
  UNIQUE KEY `Email_UNIQUE` (`Email`),
  UNIQUE KEY `Contact_Number_UNIQUE` (`Contact_Number`)
) ENGINE=InnoDB AUTO_INCREMENT=27 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `employee`
--

LOCK TABLES `employee` WRITE;
/*!40000 ALTER TABLE `employee` DISABLE KEYS */;
INSERT INTO `employee` VALUES (1,'Winsom','Gerhard','Cashier','4568640866','ld.kirbble@gmail.com',0),(2,'Moger','Adelina','Kitchen','1395629063','amoger1@shutterfly.com',1),(3,'Wain','Adelina','Kitchen','7632214950','gwain2@mysql.com',1),(4,'test','test','Cashier','123','et',0),(7,'Casa','Cynthia','Kitchen','2991245977','ccasa1@altervista.org',1),(8,'Swaine','Brien','Kitchen','5593165731','bswaine2@google.com.br',1),(9,'Villatura','Leah','Kitchen','123456','feafafafea@gmail.com',1),(10,'Bautista','Patrick','Cashier','0988843','patrickb@gmail.com',1),(11,'F','Nicole','Cashier','09111233','poop@gmail.com',1),(12,'testtest','test','Cashier','12335345','testttt@gmail.com',1),(13,'ta','mon','Cashier','2146','yuo@yahu',1),(14,'s','hyy','Cashier','3141','pop@gmail.com',1),(15,'','','Cashier','','',1),(16,'a','a','Cashier','09','a',1),(17,'a','a','Cashier','09123456722','a@gmail.com',1),(18,'a','a','Cashier','09123433322','b@gmail.com',1),(20,'villatura','leah','Cashier','09563921848','why@gmail.com',1),(21,'Pal','Pro','Cashier','09124356789','poorpal@gmail.com',1),(22,'Pofewajp','NIcole','Cashier','09213456765','hi@gmail.com',1),(25,'Pofewajp','NIcole','Cashier','09213452342','rwerfwehi@gmail.com',1),(26,'laxamana','jun','Cashier','09123568790','jownjown@gmail.com',1);
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

-- Dump completed on 2024-06-13  8:20:31
