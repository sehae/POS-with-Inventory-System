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
-- Table structure for table `user`
--

DROP TABLE IF EXISTS `user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `User_ID` varchar(255) NOT NULL,
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
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user`
--

LOCK TABLES `user` WRITE;
/*!40000 ALTER TABLE `user` DISABLE KEYS */;
INSERT INTO `user` VALUES ('MH2401','Villatura','Leah Desiree','Admin','Admin','09563847921','ld.kirbble@gmail.com','LV0101','b1951c955be8f1c84957e349edca2b7ed4e5c33613eb88408c521b112b420f2f2125b6b8af1349162bb3f0fefe20b92d815416599f5ef692f1f4e0fe09f3f2cd41e7d6cdea69245c48eb70a74ed06b597c4ad3fdc071f9830a89b4c62276399f','Enabled'),('MH2402','Tiamzon','Bryan Dominick','Employee','Cashier','09456123481','qbdatiamzon@tip.edu.ph','BT0202','bc04714f561b4b205eaa1453c78b85db385dce5d9d5157a6579e5523e6e5a1eece6691a07e27d57deda61b476b69e0c05ff6989ead7a80e36a10ab0fde1803c018bcc3d69185d1d887db3b08e3a64076d4fb28488f98918efa2050dd7e2d9dba','Enabled'),('MH2403','Faurillo','Ymnwl Jan','Employee','Kitchen','09454421238','qyjpfaurillo@tip.edu.ph','YF0203','d9650dd8098532ee3e2729d5233f320dc06267af3a2b35ad4b1d20cba31d01e890702b5ce8a12a6fd910f7616b36d423da5e8fbe5d40a99da737e32b0de10caecf93eee0dc322af70ea94c44d370561b97d386413c6ab6c76e4f12b4b18c8700','Enabled');
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

-- Dump completed on 2024-06-29 11:17:41
