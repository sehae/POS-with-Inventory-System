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
-- Table structure for table `user_logs`
--

DROP TABLE IF EXISTS `user_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_logs` (
  `log_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `action_id` int NOT NULL,
  `user_type` enum('employee','admin','system') NOT NULL,
  `log_date` date NOT NULL,
  `log_time` time NOT NULL,
  `parameter` longtext NOT NULL,
  PRIMARY KEY (`log_id`,`action_id`),
  KEY `action_id` (`action_id`),
  CONSTRAINT `user_logs_ibfk_1` FOREIGN KEY (`action_id`) REFERENCES `user_actions` (`action_id`)
) ENGINE=InnoDB AUTO_INCREMENT=34 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_logs`
--

LOCK TABLES `user_logs` WRITE;
/*!40000 ALTER TABLE `user_logs` DISABLE KEYS */;
INSERT INTO `user_logs` VALUES (1,1,2,'admin','2024-06-13','14:39:24','{username} Has logged in successfully.'),(2,1,1,'admin','2024-06-13','14:43:02','{username} Has failed to log in.'),(3,1,2,'admin','2024-06-13','18:33:49','successfully logged in None'),(4,1,2,'admin','2024-06-13','18:34:51','LV0101 successfully logged in None'),(5,1,2,'admin','2024-06-13','18:41:52','LV0101 successfully logged in admin'),(6,1,2,'admin','2024-06-13','19:36:00','LV0101 successfully logged in admin'),(7,1,2,'admin','2024-06-13','19:49:18','LV0101 successfully logged in admin'),(8,1,1,'system','2024-06-13','20:19:26','LV0101 attempted to login system'),(9,0,1,'system','2024-06-13','20:20:31','lv0101 attempted to login system'),(10,1,2,'admin','2024-06-13','21:09:28','LV0101 successfully logged in admin'),(11,1,2,'admin','2024-06-14','00:46:55','LV0101 successfully logged in admin'),(12,1,2,'admin','2024-06-14','00:58:51','LV0101 successfully logged in admin'),(13,1,2,'admin','2024-06-14','01:00:32','LV0101 successfully logged in admin'),(14,1,2,'admin','2024-06-14','01:07:44','LV0101 successfully logged in admin'),(15,1,2,'admin','2024-06-14','01:10:01','LV0101 successfully logged in admin'),(16,1,2,'admin','2024-06-14','01:10:29','LV0101 successfully logged in admin'),(17,1,2,'admin','2024-06-14','01:16:02','LV0101 successfully logged in admin'),(18,1,2,'admin','2024-06-14','01:18:45','LV0101 successfully logged in admin'),(19,1,2,'admin','2024-06-14','01:20:11','LV0101 successfully logged in admin'),(20,1,2,'admin','2024-06-14','01:22:55','LV0101 successfully logged in admin'),(21,1,2,'admin','2024-06-14','01:25:51','LV0101 successfully logged in admin'),(22,1,2,'admin','2024-06-14','01:26:59','LV0101 successfully logged in admin'),(23,1,2,'admin','2024-06-14','01:28:16','LV0101 successfully logged in admin'),(24,1,2,'admin','2024-06-14','01:30:51','LV0101 successfully logged in admin'),(25,1,1,'system','2024-06-14','01:32:14','LV0101 attempted to login system'),(26,1,2,'admin','2024-06-14','01:32:18','LV0101 successfully logged in admin'),(27,1,2,'admin','2024-06-14','01:33:35','LV0101 successfully logged in admin'),(28,1,2,'admin','2024-06-14','01:47:57','LV0101 successfully logged in admin'),(29,1,1,'system','2024-06-14','02:07:44','LV0101 attempted to login system'),(30,1,2,'admin','2024-06-14','02:07:52','LV0101 successfully logged in admin'),(31,1,1,'system','2024-06-14','02:11:29','LV0101 attempted to login system'),(32,1,1,'system','2024-06-14','02:12:40','LV0101 attempted to login system'),(33,1,2,'admin','2024-06-14','10:49:38','LV0101 successfully logged in admin');
/*!40000 ALTER TABLE `user_logs` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-06-14 10:53:05
