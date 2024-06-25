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
) ENGINE=InnoDB AUTO_INCREMENT=355 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_logs`
--

LOCK TABLES `user_logs` WRITE;
/*!40000 ALTER TABLE `user_logs` DISABLE KEYS */;
INSERT INTO `user_logs` VALUES (1,1,2,'2024-06-16','15:19:18','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in \"\"'),(2,1,2,'2024-06-16','15:20:50','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in \"\"'),(3,1,2,'2024-06-16','15:25:08','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in \"None\"'),(4,1,2,'2024-06-16','15:27:10','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(5,1,2,'2024-06-16','15:53:03','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(6,1,2,'2024-06-16','15:59:16','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(7,1,2,'2024-06-16','16:21:23','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(8,1,2,'2024-06-16','16:22:42','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(9,1,2,'2024-06-16','16:24:12','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(10,1,2,'2024-06-16','16:25:37','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(11,1,2,'2024-06-16','16:29:34','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(12,1,2,'2024-06-16','16:33:04','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(13,1,2,'2024-06-16','16:37:09','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(14,1,2,'2024-06-16','16:37:39','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(15,1,2,'2024-06-16','16:39:08','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(16,1,2,'2024-06-16','16:40:51','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(17,1,2,'2024-06-16','16:42:48','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(18,1,2,'2024-06-16','16:43:58','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(19,1,2,'2024-06-16','16:45:55','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(20,1,2,'2024-06-16','16:46:41','User:\"lv0101\" using DESKTOP-P0I91HL: successfully logged in'),(21,1,2,'2024-06-16','16:47:36','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(22,1,2,'2024-06-16','16:49:30','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(23,1,2,'2024-06-16','16:51:50','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(24,1,2,'2024-06-16','16:52:49','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(25,1,2,'2024-06-16','16:55:18','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(26,1,2,'2024-06-16','16:56:50','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(27,1,2,'2024-06-16','17:00:12','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(28,1,2,'2024-06-16','17:39:23','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(29,1,2,'2024-06-16','17:40:49','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(30,1,2,'2024-06-16','17:42:13','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(31,1,2,'2024-06-16','17:50:04','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(32,1,2,'2024-06-16','17:53:41','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(33,1,2,'2024-06-16','17:57:02','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(34,1,2,'2024-06-16','17:58:37','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(35,1,2,'2024-06-16','18:00:09','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(36,1,1,'2024-06-16','18:16:45','User:\"LV0101\" using DESKTOP-P0I91HL: attempted to login'),(37,1,1,'2024-06-16','18:40:33','User:\"LV0101\" using DESKTOP-P0I91HL: attempted to login'),(38,1,2,'2024-06-16','18:41:17','User:\"None\" using DESKTOP-P0I91HL: successfully logged in \"LV0101\"'),(39,1,2,'2024-06-16','18:42:16','User:\"None\" using DESKTOP-P0I91HL: successfully logged in \"LV0101\"'),(40,1,2,'2024-06-16','18:43:40','User:\"None\" using DESKTOP-P0I91HL: successfully logged in \"LV0101\"'),(41,1,2,'2024-06-16','18:46:22','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(42,1,2,'2024-06-16','18:51:25','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(43,1,2,'2024-06-16','18:54:34','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(44,1,10,'2024-06-16','18:55:00','User:\"LV0101\" using DESKTOP-P0I91HL: added new user \"JL0106\"'),(45,1,2,'2024-06-16','18:56:48','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(46,1,2,'2024-06-16','18:57:55','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(47,1,11,'2024-06-16','18:58:04','User:\"LV0101\" using DESKTOP-P0I91HL: update LoA \"for user jownjown@gmaa.com to Staff and Cashier\"'),(48,1,2,'2024-06-16','19:03:57','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(49,1,13,'2024-06-16','19:04:03','User:\"LV0101\" using DESKTOP-P0I91HL: deactivated a user \"for user jownjown@gmaa.com to Disabled\"'),(50,1,2,'2024-06-17','14:41:03','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(51,1,2,'2024-06-17','15:10:59','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(52,1,2,'2024-06-17','15:12:43','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(53,1,2,'2024-06-17','15:28:00','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(54,1,2,'2024-06-17','15:50:17','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(55,1,2,'2024-06-17','15:54:33','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(56,1,1,'2024-06-17','15:55:57','User:\"LV0101\" using DESKTOP-P0I91HL: attempted to login'),(57,1,2,'2024-06-17','15:56:04','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(58,1,2,'2024-06-17','16:00:11','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(59,1,2,'2024-06-17','16:02:27','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(60,1,2,'2024-06-17','16:04:49','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(61,1,2,'2024-06-17','16:07:48','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(62,1,2,'2024-06-17','16:09:49','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(63,1,2,'2024-06-17','16:10:40','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(64,1,2,'2024-06-17','16:11:40','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(65,1,2,'2024-06-17','16:15:26','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(66,1,2,'2024-06-17','16:20:32','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(67,1,2,'2024-06-17','16:21:07','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(68,1,2,'2024-06-17','16:23:55','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(69,1,2,'2024-06-17','16:26:23','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(70,1,2,'2024-06-17','16:29:21','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(71,1,2,'2024-06-17','16:52:28','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(72,1,2,'2024-06-17','16:54:37','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(73,1,2,'2024-06-17','16:57:08','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(74,1,2,'2024-06-17','17:30:42','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(75,1,2,'2024-06-17','17:35:40','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(76,1,2,'2024-06-17','19:45:18','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(77,1,2,'2024-06-17','19:47:19','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(78,1,2,'2024-06-17','19:48:15','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(79,1,2,'2024-06-17','19:49:05','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(80,1,2,'2024-06-17','19:55:51','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(81,1,2,'2024-06-17','19:57:33','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(82,1,2,'2024-06-17','19:57:49','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(83,1,2,'2024-06-17','19:59:44','User:\"LV0101\" using DESKTOP-P0I91HL: successfully logged in'),(84,1,2,'2024-06-18','15:03:18','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(85,1,2,'2024-06-18','15:07:35','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(86,1,2,'2024-06-18','15:10:58','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(87,1,2,'2024-06-18','15:12:53','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(88,1,2,'2024-06-18','15:26:34','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(89,1,2,'2024-06-18','15:27:28','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(90,1,2,'2024-06-18','15:30:07','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(91,1,2,'2024-06-18','15:33:14','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(92,1,2,'2024-06-18','15:47:07','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(93,1,2,'2024-06-18','15:47:28','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(94,1,1,'2024-06-18','16:01:41','User:\"LV0101\" using LAPTOP-A220H6MF: attempted to login'),(95,1,2,'2024-06-18','16:01:44','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(96,1,2,'2024-06-18','16:02:38','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(97,1,2,'2024-06-18','16:03:47','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(98,1,2,'2024-06-18','16:09:51','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(99,1,2,'2024-06-18','16:11:34','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(100,1,2,'2024-06-18','16:12:06','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(101,1,2,'2024-06-18','16:14:29','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(102,1,2,'2024-06-18','16:15:47','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(103,1,2,'2024-06-18','16:19:56','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(104,1,2,'2024-06-18','16:21:04','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(105,1,2,'2024-06-18','16:21:32','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(106,1,2,'2024-06-18','16:22:16','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(107,1,2,'2024-06-18','16:23:05','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(108,1,2,'2024-06-18','16:25:36','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(109,1,2,'2024-06-18','16:26:24','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(110,1,2,'2024-06-18','16:26:50','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(111,1,2,'2024-06-18','16:27:10','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(112,1,2,'2024-06-18','16:28:07','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(113,1,1,'2024-06-18','16:29:29','User:\"LV0101\" using LAPTOP-A220H6MF: attempted to login'),(114,1,2,'2024-06-18','16:29:33','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(115,1,2,'2024-06-18','16:56:49','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(116,1,2,'2024-06-18','17:05:28','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(117,1,2,'2024-06-18','17:07:48','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(118,1,2,'2024-06-18','17:11:58','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(119,1,2,'2024-06-18','17:13:51','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(120,1,2,'2024-06-18','17:14:58','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(121,1,2,'2024-06-18','17:15:27','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(122,1,2,'2024-06-18','17:25:26','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(123,1,2,'2024-06-18','17:27:54','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(124,1,2,'2024-06-18','17:28:38','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(125,1,2,'2024-06-18','17:45:30','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(126,1,2,'2024-06-18','17:45:56','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(127,1,2,'2024-06-18','17:46:31','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(128,1,2,'2024-06-18','17:48:58','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(129,1,2,'2024-06-18','17:54:27','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(130,1,2,'2024-06-18','18:26:03','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(131,1,2,'2024-06-18','18:26:08','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(132,1,2,'2024-06-18','18:27:04','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(133,1,1,'2024-06-18','18:28:10','User:\"LV0101\" using LAPTOP-A220H6MF: attempted to login'),(134,1,2,'2024-06-18','18:28:15','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(135,1,2,'2024-06-18','18:46:26','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(136,1,2,'2024-06-18','18:46:53','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(137,3,1,'2024-06-18','18:52:41','User:\"BT0103\" using LAPTOP-A220H6MF: attempted to login'),(138,3,1,'2024-06-18','18:53:56','User:\"BT0103\" using LAPTOP-A220H6MF: attempted to login'),(139,3,1,'2024-06-18','18:53:58','User:\"BT0103\" using LAPTOP-A220H6MF: attempted to login'),(140,3,1,'2024-06-18','18:53:58','User:\"BT0103\" using LAPTOP-A220H6MF: attempted to login'),(141,3,1,'2024-06-18','18:53:58','User:\"BT0103\" using LAPTOP-A220H6MF: attempted to login'),(142,3,1,'2024-06-18','18:53:58','User:\"BT0103\" using LAPTOP-A220H6MF: attempted to login'),(143,3,2,'2024-06-18','18:59:28','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(144,3,1,'2024-06-18','19:00:56','User:\"BT0103\" using LAPTOP-A220H6MF: attempted to login'),(145,3,1,'2024-06-18','19:00:59','User:\"BT0103\" using LAPTOP-A220H6MF: attempted to login'),(146,3,1,'2024-06-18','19:01:06','User:\"BT0103\" using LAPTOP-A220H6MF: attempted to login'),(147,3,1,'2024-06-18','19:01:08','User:\"BT0103\" using LAPTOP-A220H6MF: attempted to login'),(148,3,1,'2024-06-18','19:01:08','User:\"BT0103\" using LAPTOP-A220H6MF: attempted to login'),(149,3,2,'2024-06-18','19:01:39','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(150,3,2,'2024-06-18','19:02:31','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(151,1,2,'2024-06-18','19:06:37','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(152,3,2,'2024-06-18','19:06:49','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(153,3,2,'2024-06-18','19:12:10','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(154,1,2,'2024-06-18','19:14:45','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(155,1,2,'2024-06-18','19:15:40','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(156,1,2,'2024-06-18','19:16:10','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(157,1,2,'2024-06-18','19:16:54','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(158,3,1,'2024-06-18','19:17:19','User:\"BT0103\" using LAPTOP-A220H6MF: attempted to login'),(159,3,2,'2024-06-18','19:17:22','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(160,3,2,'2024-06-18','19:18:46','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(161,3,2,'2024-06-18','19:20:01','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(162,3,2,'2024-06-18','19:20:49','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(163,1,2,'2024-06-18','19:22:13','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(164,3,2,'2024-06-18','19:22:28','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(165,2,2,'2024-06-18','19:25:00','User:\"YF0102\" using LAPTOP-A220H6MF: successfully logged in'),(166,2,2,'2024-06-18','19:25:19','User:\"YF0102\" using LAPTOP-A220H6MF: successfully logged in'),(167,3,2,'2024-06-18','19:50:56','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(168,3,2,'2024-06-18','19:51:36','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(169,2,1,'2024-06-18','19:51:52','User:\"YF0102\" using LAPTOP-A220H6MF: attempted to login'),(170,2,2,'2024-06-18','19:51:55','User:\"YF0102\" using LAPTOP-A220H6MF: successfully logged in'),(171,3,2,'2024-06-18','19:52:12','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(172,3,2,'2024-06-18','19:53:48','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(173,1,2,'2024-06-18','19:57:01','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(174,1,2,'2024-06-18','20:34:02','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(175,1,2,'2024-06-18','20:37:08','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(176,1,2,'2024-06-18','20:41:04','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(177,1,2,'2024-06-18','20:44:24','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(178,1,2,'2024-06-18','20:48:07','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(179,1,2,'2024-06-18','22:57:53','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(180,3,2,'2024-06-19','13:43:52','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(181,2,2,'2024-06-19','13:46:51','User:\"YF0102\" using LAPTOP-A220H6MF: successfully logged in'),(182,1,2,'2024-06-19','13:47:47','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(183,3,2,'2024-06-19','13:48:23','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(184,1,2,'2024-06-19','13:49:27','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(185,1,2,'2024-06-19','13:53:57','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(186,3,2,'2024-06-19','13:59:48','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(187,3,2,'2024-06-19','13:59:49','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(188,1,2,'2024-06-19','14:37:31','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(189,1,2,'2024-06-19','14:39:39','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(190,3,2,'2024-06-19','14:41:32','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(191,1,2,'2024-06-19','14:46:06','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(192,3,2,'2024-06-19','14:46:20','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(193,3,2,'2024-06-19','14:53:52','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(194,3,2,'2024-06-19','15:03:49','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(195,3,2,'2024-06-19','15:07:21','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(196,1,2,'2024-06-19','15:08:26','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(197,2,2,'2024-06-19','15:08:50','User:\"YF0102\" using LAPTOP-A220H6MF: successfully logged in'),(198,3,2,'2024-06-19','16:59:46','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(199,1,2,'2024-06-19','17:11:15','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(200,1,2,'2024-06-22','14:35:14','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(201,1,2,'2024-06-22','14:35:42','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(202,1,2,'2024-06-22','14:37:50','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(203,1,2,'2024-06-22','14:39:02','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(204,1,9,'2024-06-22','14:39:03','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(205,1,2,'2024-06-22','14:39:33','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(206,1,9,'2024-06-22','14:39:35','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(207,1,2,'2024-06-22','14:46:16','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(208,1,2,'2024-06-22','14:47:28','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(209,1,2,'2024-06-22','14:50:16','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(210,1,9,'2024-06-22','14:50:16','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(211,1,2,'2024-06-22','14:50:59','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(212,1,9,'2024-06-22','14:51:01','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(213,1,2,'2024-06-22','15:00:32','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(214,1,2,'2024-06-22','15:01:55','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(215,1,14,'2024-06-22','15:01:59','User:\"LV0101\" using LAPTOP-A220H6MF: user-initiated backup'),(216,1,9,'2024-06-22','15:02:22','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(217,1,1,'2024-06-22','15:06:29','User:\"LV0101\" using LAPTOP-A220H6MF: attempted to login'),(218,0,1,'2024-06-22','15:07:02','User:\"System\" using LAPTOP-A220H6MF: attempted to login'),(219,1,2,'2024-06-22','15:07:36','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(220,1,2,'2024-06-22','15:07:41','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(221,1,2,'2024-06-22','15:08:24','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(222,1,9,'2024-06-22','15:09:25','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(223,1,2,'2024-06-22','15:14:09','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(224,1,11,'2024-06-22','15:14:23','User:\"LV0101\" using LAPTOP-A220H6MF: update LoA \"of user ld.kirbble@gmail.com to Staff and Cashier\"'),(225,1,11,'2024-06-22','15:14:28','User:\"LV0101\" using LAPTOP-A220H6MF: update LoA \"of user ld.kirbble@gmail.com to Admin\"'),(226,1,2,'2024-06-22','15:16:19','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(227,1,9,'2024-06-22','15:16:23','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(228,1,2,'2024-06-22','15:16:45','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(229,1,9,'2024-06-22','15:16:45','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(230,1,2,'2024-06-22','15:16:47','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(231,1,2,'2024-06-22','15:22:12','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(232,1,2,'2024-06-22','15:24:21','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(233,1,2,'2024-06-22','15:30:45','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(234,1,2,'2024-06-22','15:34:46','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(235,1,2,'2024-06-22','15:44:42','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(236,1,9,'2024-06-22','15:45:09','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(237,1,2,'2024-06-22','15:51:00','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(238,1,9,'2024-06-22','15:51:01','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(239,1,2,'2024-06-22','15:51:03','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(240,1,9,'2024-06-22','15:51:04','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(241,1,2,'2024-06-22','15:51:13','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(242,1,9,'2024-06-22','15:51:14','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(243,1,2,'2024-06-22','16:24:16','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(244,1,9,'2024-06-22','16:24:21','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(245,1,3,'2024-06-22','16:25:03','User:\"LV0101\" using LAPTOP-A220H6MF: initiated OTP authentication '),(246,1,3,'2024-06-22','16:25:52','User:\"LV0101\" using LAPTOP-A220H6MF: initiated OTP authentication '),(247,1,3,'2024-06-22','16:31:58','User:\"LV0101\" using LAPTOP-A220H6MF: initiated OTP authentication '),(248,1,5,'2024-06-22','16:32:04','User:\"LV0101\" using LAPTOP-A220H6MF: cancelled OTP authentication'),(249,1,3,'2024-06-22','16:32:15','User:\"LV0101\" using LAPTOP-A220H6MF: initiated OTP authentication '),(250,1,6,'2024-06-22','16:32:25','User:\"LV0101\" using LAPTOP-A220H6MF: initiated password reset '),(251,1,8,'2024-06-22','16:32:51','User:\"LV0101\" using LAPTOP-A220H6MF: successfully reseted password '),(252,1,3,'2024-06-22','16:43:52','User:\"LV0101\" using LAPTOP-A220H6MF: initiated OTP authentication '),(253,1,6,'2024-06-22','16:43:59','User:\"LV0101\" using LAPTOP-A220H6MF: initiated password reset '),(254,1,8,'2024-06-22','16:44:16','User:\"LV0101\" using LAPTOP-A220H6MF: successfully reseted password '),(255,1,2,'2024-06-22','16:51:16','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(256,1,9,'2024-06-22','16:51:22','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(257,1,2,'2024-06-22','16:57:25','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(258,1,2,'2024-06-22','16:57:56','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(259,1,2,'2024-06-22','17:00:31','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(260,1,2,'2024-06-22','17:02:16','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(261,1,2,'2024-06-22','17:08:40','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(262,1,2,'2024-06-22','17:09:08','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(263,1,2,'2024-06-22','17:09:58','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(264,1,10,'2024-06-22','17:10:06','User:\"LV0101\" using LAPTOP-A220H6MF: added new user \"000204\"'),(265,1,2,'2024-06-22','17:11:49','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(266,1,2,'2024-06-22','17:13:51','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(267,1,2,'2024-06-22','17:14:34','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(268,1,2,'2024-06-22','17:14:51','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(269,1,2,'2024-06-22','17:20:06','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(270,1,3,'2024-06-22','18:00:50','User:\"LV0101\" using LAPTOP-A220H6MF: initiated OTP authentication '),(271,1,6,'2024-06-22','18:01:21','User:\"LV0101\" using LAPTOP-A220H6MF: initiated password reset '),(272,1,3,'2024-06-22','18:05:33','User:\"LV0101\" using LAPTOP-A220H6MF: initiated OTP authentication '),(273,1,6,'2024-06-22','18:05:55','User:\"LV0101\" using LAPTOP-A220H6MF: initiated password reset '),(274,1,3,'2024-06-22','18:10:18','User:\"LV0101\" using LAPTOP-A220H6MF: initiated OTP authentication '),(275,1,6,'2024-06-22','18:10:26','User:\"LV0101\" using LAPTOP-A220H6MF: initiated password reset '),(276,1,3,'2024-06-22','18:11:15','User:\"LV0101\" using LAPTOP-A220H6MF: initiated OTP authentication '),(277,1,6,'2024-06-22','18:11:27','User:\"LV0101\" using LAPTOP-A220H6MF: initiated password reset '),(278,1,3,'2024-06-22','18:14:18','User:\"LV0101\" using LAPTOP-A220H6MF: initiated OTP authentication '),(279,1,6,'2024-06-22','18:15:04','User:\"LV0101\" using LAPTOP-A220H6MF: initiated password reset '),(280,1,7,'2024-06-22','18:15:07','User:\"LV0101\" using LAPTOP-A220H6MF: cancelled password reset '),(281,1,2,'2024-06-22','18:19:09','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(282,1,2,'2024-06-22','18:27:52','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(283,1,2,'2024-06-22','18:28:38','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(284,1,1,'2024-06-22','18:31:09','User:\"LV0101\" using LAPTOP-A220H6MF: attempted to login'),(285,1,2,'2024-06-22','18:31:13','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(286,1,2,'2024-06-22','18:34:06','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(287,0,1,'2024-06-22','18:38:44','User:\"System\" using LAPTOP-A220H6MF: attempted to login'),(288,1,2,'2024-06-22','18:38:50','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(289,1,2,'2024-06-22','18:41:23','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(290,1,1,'2024-06-22','18:44:55','User:\"LV0101\" using LAPTOP-A220H6MF: attempted to login'),(291,1,2,'2024-06-22','18:44:57','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(292,1,2,'2024-06-22','18:46:00','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(293,1,9,'2024-06-22','18:47:45','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(294,1,2,'2024-06-22','18:47:55','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(295,1,2,'2024-06-22','18:54:48','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(296,1,9,'2024-06-22','18:55:36','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(297,1,2,'2024-06-22','18:55:56','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(298,1,9,'2024-06-22','18:56:11','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(299,1,2,'2024-06-22','18:56:20','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(300,1,2,'2024-06-22','18:58:08','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(301,1,2,'2024-06-22','19:00:25','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(302,1,9,'2024-06-22','19:00:36','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(303,1,2,'2024-06-22','19:09:49','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(304,1,2,'2024-06-22','19:10:46','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(305,1,12,'2024-06-22','19:11:00','User:\"LV0101\" using LAPTOP-A220H6MF: changed password'),(306,0,1,'2024-06-22','19:13:05','User:\"System\" using LAPTOP-A220H6MF: attempted to login'),(307,1,2,'2024-06-22','19:13:10','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(308,1,12,'2024-06-22','19:13:36','User:\"LV0101\" using LAPTOP-A220H6MF: changed password'),(309,1,12,'2024-06-22','19:13:59','User:\"LV0101\" using LAPTOP-A220H6MF: changed password'),(310,1,9,'2024-06-22','19:14:02','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(311,1,2,'2024-06-22','19:17:36','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(312,1,2,'2024-06-22','19:50:14','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(313,1,2,'2024-06-22','20:19:33','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(314,1,14,'2024-06-22','20:19:37','User:\"LV0101\" using LAPTOP-A220H6MF: user-initiated backup'),(315,1,9,'2024-06-22','20:19:42','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(316,3,2,'2024-06-22','20:44:05','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(317,3,9,'2024-06-22','20:44:08','User:\"BT0103\" using LAPTOP-A220H6MF: logged out'),(318,2,2,'2024-06-22','20:44:12','User:\"YF0102\" using LAPTOP-A220H6MF: successfully logged in'),(319,2,9,'2024-06-22','21:55:46','User:\"YF0102\" using LAPTOP-A220H6MF: logged out'),(320,1,2,'2024-06-22','23:43:59','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(321,1,3,'2024-06-23','00:26:57','User:\"LV0101\" using LAPTOP-A220H6MF: initiated OTP authentication '),(322,1,6,'2024-06-23','00:27:16','User:\"LV0101\" using LAPTOP-A220H6MF: initiated password reset '),(323,1,7,'2024-06-23','00:27:31','User:\"LV0101\" using LAPTOP-A220H6MF: cancelled password reset '),(324,1,3,'2024-06-23','00:30:02','User:\"LV0101\" using LAPTOP-A220H6MF: initiated OTP authentication '),(325,1,3,'2024-06-23','00:30:19','User:\"LV0101\" using LAPTOP-A220H6MF: initiated OTP authentication '),(326,1,6,'2024-06-23','00:30:35','User:\"LV0101\" using LAPTOP-A220H6MF: initiated password reset '),(327,1,7,'2024-06-23','00:30:41','User:\"LV0101\" using LAPTOP-A220H6MF: cancelled password reset '),(328,1,3,'2024-06-23','00:30:55','User:\"LV0101\" using LAPTOP-A220H6MF: initiated OTP authentication '),(329,1,5,'2024-06-23','00:31:31','User:\"LV0101\" using LAPTOP-A220H6MF: cancelled OTP authentication'),(330,1,2,'2024-06-23','00:31:37','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(331,1,9,'2024-06-23','00:33:28','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(332,2,2,'2024-06-23','00:33:50','User:\"YF0102\" using LAPTOP-A220H6MF: successfully logged in'),(333,2,9,'2024-06-23','00:34:30','User:\"YF0102\" using LAPTOP-A220H6MF: logged out'),(334,3,2,'2024-06-23','00:34:38','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(335,3,9,'2024-06-23','00:34:40','User:\"BT0103\" using LAPTOP-A220H6MF: logged out'),(336,3,2,'2024-06-23','00:34:46','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(337,3,9,'2024-06-23','00:35:36','User:\"BT0103\" using LAPTOP-A220H6MF: logged out'),(338,1,2,'2024-06-23','00:35:53','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(339,1,9,'2024-06-23','00:36:22','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(340,1,2,'2024-06-23','00:37:24','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(341,1,14,'2024-06-23','00:37:32','User:\"LV0101\" using LAPTOP-A220H6MF: user-initiated backup'),(342,1,9,'2024-06-23','01:32:30','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(343,3,2,'2024-06-23','01:32:40','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(344,1,2,'2024-06-23','13:55:27','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(345,3,2,'2024-06-23','13:56:12','User:\"BT0103\" using LAPTOP-A220H6MF: successfully logged in'),(346,1,2,'2024-06-23','14:23:51','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(347,2,2,'2024-06-23','14:24:41','User:\"YF0102\" using LAPTOP-A220H6MF: successfully logged in'),(348,2,9,'2024-06-23','17:24:38','User:\"YF0102\" using LAPTOP-A220H6MF: logged out'),(349,1,2,'2024-06-25','19:39:31','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(350,1,9,'2024-06-25','19:39:47','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(351,1,2,'2024-06-25','19:40:01','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(352,1,9,'2024-06-25','19:40:05','User:\"LV0101\" using LAPTOP-A220H6MF: logged out'),(353,1,2,'2024-06-25','19:42:14','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in'),(354,1,2,'2024-06-25','20:00:13','User:\"LV0101\" using LAPTOP-A220H6MF: successfully logged in');
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

-- Dump completed on 2024-06-25 20:01:51
