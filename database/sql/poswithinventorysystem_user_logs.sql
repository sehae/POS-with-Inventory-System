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
  `log_date` date NOT NULL,
  `log_time` time NOT NULL,
  `parameter` longtext NOT NULL,
  PRIMARY KEY (`log_id`,`action_id`),
  KEY `action_id` (`action_id`),
  CONSTRAINT `user_logs_ibfk_1` FOREIGN KEY (`action_id`) REFERENCES `user_actions` (`action_id`)
) ENGINE=InnoDB AUTO_INCREMENT=84 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_logs`
--

LOCK TABLES `user_logs` WRITE;
/*!40000 ALTER TABLE `user_logs` DISABLE KEYS */;
INSERT INTO `user_logs` VALUES (1,1,2,'2024-06-16','15:19:18','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in \"\"'),(2,1,2,'2024-06-16','15:20:50','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in \"\"'),(3,1,2,'2024-06-16','15:25:08','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in \"None\"'),(4,1,2,'2024-06-16','15:27:10','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(5,1,2,'2024-06-16','15:53:03','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(6,1,2,'2024-06-16','15:59:16','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(7,1,2,'2024-06-16','16:21:23','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(8,1,2,'2024-06-16','16:22:42','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(9,1,2,'2024-06-16','16:24:12','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(10,1,2,'2024-06-16','16:25:37','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(11,1,2,'2024-06-16','16:29:34','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(12,1,2,'2024-06-16','16:33:04','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(13,1,2,'2024-06-16','16:37:09','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(14,1,2,'2024-06-16','16:37:39','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(15,1,2,'2024-06-16','16:39:08','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(16,1,2,'2024-06-16','16:40:51','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(17,1,2,'2024-06-16','16:42:48','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(18,1,2,'2024-06-16','16:43:58','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(19,1,2,'2024-06-16','16:45:55','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(20,1,2,'2024-06-16','16:46:41','User:\"lv0101\" using DESKTOP-P0I91HL: successfully logged in'),(21,1,2,'2024-06-16','16:47:36','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(22,1,2,'2024-06-16','16:49:30','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(23,1,2,'2024-06-16','16:51:50','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(24,1,2,'2024-06-16','16:52:49','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(25,1,2,'2024-06-16','16:55:18','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(26,1,2,'2024-06-16','16:56:50','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(27,1,2,'2024-06-16','17:00:12','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(28,1,2,'2024-06-16','17:39:23','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(29,1,2,'2024-06-16','17:40:49','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(30,1,2,'2024-06-16','17:42:13','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(31,1,2,'2024-06-16','17:50:04','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(32,1,2,'2024-06-16','17:53:41','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(33,1,2,'2024-06-16','17:57:02','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(34,1,2,'2024-06-16','17:58:37','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(35,1,2,'2024-06-16','18:00:09','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(36,1,1,'2024-06-16','18:16:45','User:\"LV0101\" using DESKTOP-P0I91HL: attempted to login'),(37,1,1,'2024-06-16','18:40:33','User:\"LV0101\" using DESKTOP-P0I91HL: attempted to login'),(38,1,2,'2024-06-16','18:41:17','User:\"None\" using DESKTOP-P0I91HL: successfully logged in \"LV0101\"'),(39,1,2,'2024-06-16','18:42:16','User:\"None\" using DESKTOP-P0I91HL: successfully logged in \"LV0101\"'),(40,1,2,'2024-06-16','18:43:40','User:\"None\" using DESKTOP-P0I91HL: successfully logged in \"LV0101\"'),(41,1,2,'2024-06-16','18:46:22','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(42,1,2,'2024-06-16','18:51:25','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(43,1,2,'2024-06-16','18:54:34','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(44,1,10,'2024-06-16','18:55:00','User:\"LV0101\" using DESKTOP-P0I91HL: added new user \"JL0106\"'),(45,1,2,'2024-06-16','18:56:48','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(46,1,2,'2024-06-16','18:57:55','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(47,1,11,'2024-06-16','18:58:04','User:\"LV0101\" using DESKTOP-P0I91HL: update LoA \"for user jownjown@gmaa.com to Staff and Cashier\"'),(48,1,2,'2024-06-16','19:03:57','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(49,1,13,'2024-06-16','19:04:03','User:\"LV0101\" using DESKTOP-P0I91HL: deactivated a user \"for user jownjown@gmaa.com to Disabled\"'),(50,1,2,'2024-06-17','14:41:03','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(51,1,2,'2024-06-17','15:10:59','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(52,1,2,'2024-06-17','15:12:43','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(53,1,2,'2024-06-17','15:28:00','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(54,1,2,'2024-06-17','15:50:17','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(55,1,2,'2024-06-17','15:54:33','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(56,1,1,'2024-06-17','15:55:57','User:\"LV0101\" using DESKTOP-P0I91HL: attempted to login'),(57,1,2,'2024-06-17','15:56:04','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(58,1,2,'2024-06-17','16:00:11','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(59,1,2,'2024-06-17','16:02:27','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(60,1,2,'2024-06-17','16:04:49','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(61,1,2,'2024-06-17','16:07:48','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(62,1,2,'2024-06-17','16:09:49','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(63,1,2,'2024-06-17','16:10:40','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(64,1,2,'2024-06-17','16:11:40','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(65,1,2,'2024-06-17','16:15:26','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(66,1,2,'2024-06-17','16:20:32','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(67,1,2,'2024-06-17','16:21:07','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(68,1,2,'2024-06-17','16:23:55','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(69,1,2,'2024-06-17','16:26:23','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(70,1,2,'2024-06-17','16:29:21','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(71,1,2,'2024-06-17','16:52:28','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(72,1,2,'2024-06-17','16:54:37','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(73,1,2,'2024-06-17','16:57:08','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(74,1,2,'2024-06-17','17:30:42','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(75,1,2,'2024-06-17','17:35:40','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(76,1,2,'2024-06-17','19:45:18','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(77,1,2,'2024-06-17','19:47:19','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(78,1,2,'2024-06-17','19:48:15','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(79,1,2,'2024-06-17','19:49:05','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(80,1,2,'2024-06-17','19:55:51','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(81,1,2,'2024-06-17','19:57:33','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(82,1,2,'2024-06-17','19:57:49','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(83,1,2,'2024-06-17','19:59:44','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in');
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

-- Dump completed on 2024-06-17 22:02:09
