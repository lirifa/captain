/*
SQLyog Ultimate v11.24 (32 bit)
MySQL - 5.6.33-log : Database - captain
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`captain` /*!40100 DEFAULT CHARACTER SET utf8 */;

USE `captain`;

/*Table structure for table `acct` */

DROP TABLE IF EXISTS `acct`;

CREATE TABLE `acct` (
  `trdacct` varchar(32) NOT NULL,
  `acc_name` varchar(32) NOT NULL,
  `bid` int(11) NOT NULL,
  `pid` int(11) NOT NULL,
  `equity` decimal(17,2) NOT NULL COMMENT '客户权益',
  `margin_locked` decimal(17,2) NOT NULL COMMENT '保证金占用',
  `fund_avaril` decimal(17,2) NOT NULL COMMENT '可用资金',
  `risk_degree` varchar(11) NOT NULL COMMENT '风险度',
  PRIMARY KEY (`trdacct`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `acct` */

insert  into `acct`(`trdacct`,`acc_name`,`bid`,`pid`,`equity`,`margin_locked`,`fund_avaril`,`risk_degree`) values ('16039','恒邦黄金交易账户',5,4,'5617649.03','2581561.53','3026087.50','46.00%');

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group` */

/*Table structure for table `auth_group_permissions` */

DROP TABLE IF EXISTS `auth_group_permissions`;

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group_permissi_permission_id_23962d04_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_58c48ba9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_group_permissions` */

/*Table structure for table `auth_permission` */

DROP TABLE IF EXISTS `auth_permission`;

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permissi_content_type_id_51277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=28 DEFAULT CHARSET=utf8;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add productinfo',7,'add_productinfo'),(20,'Can change productinfo',7,'change_productinfo'),(21,'Can delete productinfo',7,'delete_productinfo'),(22,'Can add serverinfo',8,'add_serverinfo'),(23,'Can change serverinfo',8,'change_serverinfo'),(24,'Can delete serverinfo',8,'delete_serverinfo'),(25,'Can add strategyinfo',9,'add_strategyinfo'),(26,'Can change strategyinfo',9,'change_strategyinfo'),(27,'Can delete strategyinfo',9,'delete_strategyinfo');

/*Table structure for table `auth_user` */

DROP TABLE IF EXISTS `auth_user`;

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `auth_user` */

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values (1,'pbkdf2_sha256$20000$essOsaZ1ibAb$7hk4ymJebLlyQzuu7ugmKIBvPm+VBEukRBeFtF+FpRk=','2017-02-03 03:00:15',1,'fafa','','','199201680@163.com',1,1,'2017-01-20 07:24:21');

/*Table structure for table `auth_user_groups` */

DROP TABLE IF EXISTS `auth_user_groups`;

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_30a071c9_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_30a071c9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_24702650_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_groups` */

/*Table structure for table `auth_user_user_permissions` */

DROP TABLE IF EXISTS `auth_user_user_permissions`;

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_user_perm_permission_id_3d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_7cd7acb6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `auth_user_user_permissions` */

/*Table structure for table `broker` */

DROP TABLE IF EXISTS `broker`;

CREATE TABLE `broker` (
  `bid` int(11) NOT NULL,
  `bname` varchar(32) NOT NULL,
  `blname` varchar(128) NOT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `broker` */

insert  into `broker`(`bid`,`bname`,`blname`) values (1,'南华','南华期货'),(2,'中信','中信期货'),(3,'信达','信达期货'),(4,'永安','永安期货'),(5,'恒邦','恒邦黄金');

/*Table structure for table `django_admin_log` */

DROP TABLE IF EXISTS `django_admin_log`;

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin__content_type_id_5151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_1c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin__content_type_id_5151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_1c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_admin_log` */

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(7,'operation','productinfo'),(8,'operation','serverinfo'),(9,'operation','strategyinfo'),(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=15 DEFAULT CHARSET=utf8;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2017-01-20 07:22:00'),(2,'auth','0001_initial','2017-01-20 07:22:12'),(3,'admin','0001_initial','2017-01-20 07:22:13'),(4,'contenttypes','0002_remove_content_type_name','2017-01-20 07:22:14'),(5,'auth','0002_alter_permission_name_max_length','2017-01-20 07:22:15'),(6,'auth','0003_alter_user_email_max_length','2017-01-20 07:22:15'),(7,'auth','0004_alter_user_username_opts','2017-01-20 07:22:15'),(8,'auth','0005_alter_user_last_login_null','2017-01-20 07:22:16'),(9,'auth','0006_require_contenttypes_0002','2017-01-20 07:22:16'),(10,'operation','0001_initial','2017-01-20 07:22:16'),(11,'sessions','0001_initial','2017-01-20 07:22:17'),(12,'operation','0002_auto_20170120_1524','2017-01-20 07:25:35'),(13,'operation','0003_serverinfo','2017-01-20 11:10:19'),(14,'operation','0004_auto_20170120_1913','2017-01-20 11:13:46');

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `django_session` */

insert  into `django_session`(`session_key`,`session_data`,`expire_date`) values ('piqorpgbun2dsl8l91ikw8hr92h5fxhj','MjZiODZkNzlmY2FiY2Y1ZDg4MDFjNTFkN2RiZWFjYzk1OTM5Y2M2Mjp7Il9hdXRoX3VzZXJfaGFzaCI6IjkyOWFkNTEzMzcyNjE2YjBkZTRiMWU2Njk5OGRlZjRhMzhkZmRiMjMiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=','2017-02-17 03:00:15');

/*Table structure for table `fund_log` */

DROP TABLE IF EXISTS `fund_log`;

CREATE TABLE `fund_log` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '日志id',
  `acct_type` varchar(32) NOT NULL COMMENT '账户类型',
  `acct_id` varchar(32) NOT NULL COMMENT '账户id',
  `fund` decimal(17,2) NOT NULL COMMENT '出入金金额',
  `log_tm` datetime NOT NULL COMMENT '日志时间',
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `fund_log` */

/*Table structure for table `marketinfo` */

DROP TABLE IF EXISTS `marketinfo`;

CREATE TABLE `marketinfo` (
  `stkex` char(1) NOT NULL,
  `exchange_id` varchar(32) NOT NULL,
  `market_name` varchar(32) NOT NULL,
  PRIMARY KEY (`stkex`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `marketinfo` */

insert  into `marketinfo`(`stkex`,`exchange_id`,`market_name`) values ('0','SZ','深交所'),('1','SH','上交所'),('5','CFFEX','中金所'),('6','SHFE','上期所'),('7','DCE','大商所'),('8','CZCE','郑商所'),('9','SGE','金交所');

/*Table structure for table `master_acct` */

DROP TABLE IF EXISTS `master_acct`;

CREATE TABLE `master_acct` (
  `acc_num` varchar(32) NOT NULL COMMENT '账户号',
  `acc_name` varchar(32) NOT NULL COMMENT '账户名',
  `trdacct` varchar(32) NOT NULL COMMENT '关联资金账户',
  `equity` decimal(17,2) NOT NULL COMMENT '客户权益',
  `buy_margin` decimal(17,2) NOT NULL COMMENT '已用买保证金',
  `sell_margin` decimal(17,2) NOT NULL COMMENT '已用卖保证金',
  `margin_locked` decimal(17,2) NOT NULL COMMENT '已用总保证',
  `fund_avaril` decimal(17,2) NOT NULL COMMENT '可用资金',
  PRIMARY KEY (`acc_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `master_acct` */

insert  into `master_acct`(`acc_num`,`acc_name`,`trdacct`,`equity`,`buy_margin`,`sell_margin`,`margin_locked`,`fund_avaril`) values ('666600002','黄金白银期限套利期货账号','10007177','5051487.10','184680.85','2005858.70','2190539.55','2860947.55');

/*Table structure for table `productinfo` */

DROP TABLE IF EXISTS `productinfo`;

CREATE TABLE `productinfo` (
  `pid` int(11) NOT NULL,
  `pname` varchar(32) NOT NULL,
  `admin` varchar(32) NOT NULL,
  `desc` varchar(128) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `productinfo` */

insert  into `productinfo`(`pid`,`pname`,`admin`,`desc`) values (1,'洪荒世纪','世纪盛元','哈哈'),(2,'弘金世纪','丽海宏景','嘿嘿好'),(3,'弘金华银','世纪盛元','测试'),(4,'南华自营','世纪盛元','测试');

/*Table structure for table `serverinfo` */

DROP TABLE IF EXISTS `serverinfo`;

CREATE TABLE `serverinfo` (
  `srvnum` varchar(10) NOT NULL,
  `ip` char(39) NOT NULL,
  `user` varchar(10) NOT NULL,
  `passwd` varchar(50) NOT NULL,
  `port` int(11) NOT NULL,
  `productadmin` varchar(32) NOT NULL,
  `desc` varchar(100) NOT NULL,
  PRIMARY KEY (`srvnum`),
  UNIQUE KEY `ip` (`ip`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `serverinfo` */

insert  into `serverinfo`(`srvnum`,`ip`,`user`,`passwd`,`port`,`productadmin`,`desc`) values ('01','172.24.13.2','ison','abcd1234',22,'世纪盛元','研发二部服务器'),('02','172.24.13.5','ss2ison','lhhj@#$',22,'丽海弘金','研发服务器'),('srvzx001','172.27.13.179','pmops','pmops@#$',22,'世纪盛元','中信服务器');

/*Table structure for table `strategyinfo` */

DROP TABLE IF EXISTS `strategyinfo`;

CREATE TABLE `strategyinfo` (
  `sid` int(8) NOT NULL,
  `sname` varchar(32) NOT NULL,
  `scfg` varchar(32) NOT NULL,
  `port` int(11) NOT NULL,
  `product` int(8) NOT NULL,
  `master_acc` int(30) NOT NULL,
  `sub_acc` int(30) NOT NULL,
  `desc` varchar(32) NOT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `strategyinfo` */

insert  into `strategyinfo`(`sid`,`sname`,`scfg`,`port`,`product`,`master_acc`,`sub_acc`,`desc`) values (1,'多因子策略','hessx',1000,1,4,8,'嘿嘿');

/*Table structure for table `sub_acct` */

DROP TABLE IF EXISTS `sub_acct`;

CREATE TABLE `sub_acct` (
  `acc_num` varchar(32) NOT NULL,
  `acc_name` varchar(32) NOT NULL,
  `master_acct` varchar(32) NOT NULL,
  `equity` decimal(17,2) NOT NULL,
  `fund_avaril` decimal(17,2) NOT NULL,
  `margin_locked` decimal(17,2) NOT NULL,
  `buy_margin` decimal(17,2) NOT NULL,
  `sell_margin` decimal(17,2) NOT NULL,
  PRIMARY KEY (`acc_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `sub_acct` */

insert  into `sub_acct`(`acc_num`,`acc_name`,`master_acct`,`equity`,`fund_avaril`,`margin_locked`,`buy_margin`,`sell_margin`) values ('666600000001','恒邦黄金交易账号','666600002','3304914.06','1464156.66','1840757.40','1840757.40','0.00');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
