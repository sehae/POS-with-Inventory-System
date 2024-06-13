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
-- Table structure for table `user_logs`
--

DROP TABLE IF EXISTS `user_logs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user_logs` (
  `log_id` int NOT NULL AUTO_INCREMENT,
  `user_id` int NOT NULL,
  `user_type` enum('employee','admin') NOT NULL,
  `log_date` date NOT NULL,
  `log_time` time NOT NULL,
  `action` varchar(255) NOT NULL,
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_logs`
--

LOCK TABLES `user_logs` WRITE;
/*!40000 ALTER TABLE `user_logs` DISABLE KEYS */;
INSERT INTO `user_logs` VALUES (1,12,'admin','2024-06-11','04:59:21','Login'),(2,12,'admin','2024-06-11','05:00:55','Login'),(3,12,'admin','2024-06-11','05:01:16','Login'),(4,12,'admin','2024-06-11','14:00:16','Login'),(5,26,'employee','2024-06-11','14:00:29','Login'),(6,26,'employee','2024-06-11','14:14:16','Login'),(7,12,'admin','2024-06-11','14:14:47','Login'),(8,26,'employee','2024-06-11','21:15:53','Login'),(9,26,'employee','2024-06-11','21:16:40','Login'),(10,12,'admin','2024-06-11','21:20:34','Login'),(11,26,'employee','2024-06-11','21:26:47','Login'),(12,26,'employee','2024-06-11','21:42:20','Login'),(13,26,'employee','2024-06-11','23:09:15','Login'),(14,26,'employee','2024-06-11','23:12:34','Login'),(15,26,'employee','2024-06-11','23:15:13','Login'),(16,26,'employee','2024-06-12','06:05:44','Login'),(17,12,'admin','2024-06-12','06:07:51','Login'),(18,12,'admin','2024-06-12','06:33:59','Login'),(19,12,'admin','2024-06-12','06:45:11','Login'),(20,12,'admin','2024-06-12','06:45:48','Login'),(21,12,'admin','2024-06-12','06:52:43','Login'),(22,12,'admin','2024-06-12','06:58:08','Login'),(23,12,'admin','2024-06-12','06:59:24','Login'),(24,12,'admin','2024-06-12','07:01:13','Login'),(25,12,'admin','2024-06-12','07:02:05','Login'),(26,12,'admin','2024-06-12','07:26:23','Login'),(27,26,'employee','2024-06-12','08:56:33','Login'),(28,26,'employee','2024-06-12','09:47:16','Login'),(29,26,'employee','2024-06-12','09:48:11','Login'),(30,26,'employee','2024-06-12','09:52:24','Login'),(31,26,'employee','2024-06-12','09:53:08','Login'),(32,26,'employee','2024-06-12','09:57:30','Login'),(33,26,'employee','2024-06-12','10:10:30','Login'),(34,26,'employee','2024-06-12','10:11:30','Login'),(35,26,'employee','2024-06-12','10:15:06','Login'),(36,26,'employee','2024-06-12','10:16:49','Login'),(37,26,'employee','2024-06-12','10:29:51','Login'),(38,26,'employee','2024-06-12','10:43:39','Login'),(39,26,'employee','2024-06-12','10:49:45','Login'),(40,26,'employee','2024-06-12','10:51:23','Login'),(41,26,'employee','2024-06-12','10:57:44','Login'),(42,26,'employee','2024-06-12','11:34:09','Login'),(43,12,'admin','2024-06-12','13:19:06','Login'),(44,12,'admin','2024-06-12','14:07:04','Login'),(45,12,'admin','2024-06-12','14:27:40','Login'),(46,26,'employee','2024-06-12','17:00:31','Login'),(47,26,'employee','2024-06-12','17:04:57','Login'),(48,26,'employee','2024-06-12','17:06:48','Login'),(49,12,'admin','2024-06-12','17:07:42','Login'),(50,26,'employee','2024-06-12','17:08:37','Login'),(51,12,'admin','2024-06-12','17:09:39','Login'),(52,26,'employee','2024-06-12','17:12:37','Login'),(53,26,'employee','2024-06-12','17:15:04','Login'),(54,26,'employee','2024-06-12','17:18:33','Login'),(55,12,'admin','2024-06-12','17:22:20','Login'),(56,12,'admin','2024-06-12','17:32:24','Login'),(57,12,'admin','2024-06-12','17:34:16','Login'),(58,12,'admin','2024-06-12','17:34:50','Login'),(59,12,'admin','2024-06-12','17:36:16','Login'),(60,12,'admin','2024-06-12','17:53:24','Login'),(61,12,'admin','2024-06-12','18:00:05','Login'),(62,12,'admin','2024-06-12','18:01:05','Login'),(63,12,'admin','2024-06-12','18:01:51','Login'),(64,12,'admin','2024-06-12','18:03:38','Login'),(65,12,'admin','2024-06-12','18:04:02','Login'),(66,12,'admin','2024-06-12','18:29:39','Login'),(67,12,'admin','2024-06-12','18:33:04','Login'),(68,12,'admin','2024-06-12','18:36:26','Login'),(69,12,'admin','2024-06-12','23:10:29','Login'),(70,12,'admin','2024-06-12','23:19:23','Login'),(71,12,'admin','2024-06-12','23:21:12','Login'),(72,12,'admin','2024-06-12','23:23:21','Login'),(73,12,'admin','2024-06-12','23:24:28','Login'),(74,12,'admin','2024-06-13','03:59:11','Login'),(75,12,'admin','2024-06-13','04:13:00','Login'),(76,12,'admin','2024-06-13','04:25:31','Login'),(77,12,'admin','2024-06-13','04:44:17','Login'),(78,12,'admin','2024-06-13','04:48:25','Login'),(79,12,'admin','2024-06-13','04:50:41','Login'),(80,12,'admin','2024-06-13','04:57:41','Login'),(81,12,'admin','2024-06-13','05:00:48','Login'),(82,12,'admin','2024-06-13','05:02:59','Login'),(83,12,'admin','2024-06-13','05:13:08','Login'),(84,12,'admin','2024-06-13','05:16:10','Login'),(85,12,'admin','2024-06-13','05:18:27','Login'),(86,12,'admin','2024-06-13','05:21:12','Login'),(87,12,'admin','2024-06-13','05:24:30','Login'),(88,26,'employee','2024-06-13','05:28:30','Login'),(89,12,'admin','2024-06-13','05:58:13','Login'),(90,12,'admin','2024-06-13','06:01:54','Login'),(91,12,'admin','2024-06-13','06:16:01','Login'),(92,12,'admin','2024-06-13','06:19:00','Login'),(93,12,'admin','2024-06-13','06:22:25','Login'),(94,12,'admin','2024-06-13','06:43:19','Login'),(95,12,'admin','2024-06-13','06:46:11','Login'),(96,12,'admin','2024-06-13','06:59:33','Login'),(97,12,'admin','2024-06-13','07:07:35','Login'),(98,26,'employee','2024-06-13','07:12:13','Login'),(99,12,'admin','2024-06-13','07:23:46','Login'),(100,26,'employee','2024-06-13','07:24:30','Login'),(101,12,'admin','2024-06-13','07:24:49','Login'),(102,26,'employee','2024-06-13','07:25:10','Login'),(103,26,'employee','2024-06-13','07:29:16','Login'),(104,12,'admin','2024-06-13','07:29:36','Login'),(105,26,'employee','2024-06-13','07:31:14','Login'),(106,26,'employee','2024-06-13','07:38:40','Login'),(107,12,'admin','2024-06-13','07:39:41','Login'),(108,26,'employee','2024-06-13','07:40:16','Login'),(109,12,'admin','2024-06-13','07:40:39','Login'),(110,26,'employee','2024-06-13','07:41:06','Login'),(111,12,'admin','2024-06-13','07:41:36','Login'),(112,12,'admin','2024-06-13','07:44:06','Login'),(113,12,'admin','2024-06-13','07:48:14','Login'),(114,26,'employee','2024-06-13','07:49:43','Login'),(115,12,'admin','2024-06-13','07:52:01','Login'),(116,26,'employee','2024-06-13','07:52:58','Login'),(117,26,'employee','2024-06-13','08:03:52','Login'),(118,26,'employee','2024-06-13','08:07:49','Login'),(119,12,'admin','2024-06-13','08:08:02','Login'),(120,26,'employee','2024-06-13','08:08:16','Login'),(121,12,'admin','2024-06-13','08:10:47','Login'),(122,12,'admin','2024-06-13','08:11:45','Login'),(123,12,'admin','2024-06-13','08:15:11','Login'),(124,26,'employee','2024-06-13','08:15:41','Login'),(125,12,'admin','2024-06-13','08:16:50','Login');
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

-- Dump completed on 2024-06-13  8:20:32
