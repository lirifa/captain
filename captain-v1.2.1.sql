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

insert  into `acct`(`trdacct`,`acc_name`,`bid`,`pid`,`equity`,`margin_locked`,`fund_avaril`,`risk_degree`) values ('10007177','南华期货-期货账户',1,1,'0.00','0.00','0.00','0'),('120301232','中信期货-期货账户',2,4,'0.00','0.00','0.00','0'),('12105045','南华期货-期货账户',1,3,'0.00','0.00','0.00','0'),('12105047','南华期货-期货账户',1,2,'0.00','0.00','0.00','0'),('16039','南华期货-黄金现货账户',5,1,'0.00','0.00','0.00','0'),('275508085','永安期货-期货账户',4,6,'0.00','0.00','0.00','0'),('69300002','信达期货-期货账户',3,5,'0.00','0.00','0.00','0');

/*Table structure for table `acct_hold` */

DROP TABLE IF EXISTS `acct_hold`;

CREATE TABLE `acct_hold` (
  `trd_date` char(8) NOT NULL COMMENT '交易日期',
  `trdacct` varchar(32) NOT NULL COMMENT '资金账户号',
  `instrument` varchar(32) NOT NULL COMMENT '合约名',
  `variety` varchar(32) NOT NULL COMMENT '品种名',
  `long_pos` int(11) NOT NULL COMMENT '买持仓',
  `avg_buy_price` decimal(17,3) NOT NULL COMMENT '买均价',
  `short_pos` int(11) NOT NULL COMMENT '卖持仓',
  `avg_sell_price` decimal(17,3) NOT NULL COMMENT '卖均价',
  `pos_pl` decimal(17,2) NOT NULL COMMENT '持仓盯市盈亏',
  `margin_occupied` decimal(17,2) NOT NULL COMMENT '保证金占用',
  `sh_mark` char(1) NOT NULL COMMENT '投保标识',
  PRIMARY KEY (`trd_date`,`instrument`,`trdacct`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `acct_hold` */

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
) ENGINE=InnoDB AUTO_INCREMENT=49 DEFAULT CHARSET=utf8;

/*Data for the table `auth_permission` */

insert  into `auth_permission`(`id`,`name`,`content_type_id`,`codename`) values (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add productinfo',7,'add_productinfo'),(20,'Can change productinfo',7,'change_productinfo'),(21,'Can delete productinfo',7,'delete_productinfo'),(22,'Can add serverinfo',8,'add_serverinfo'),(23,'Can change serverinfo',8,'change_serverinfo'),(24,'Can delete serverinfo',8,'delete_serverinfo'),(25,'Can add strategyinfo',9,'add_strategyinfo'),(26,'Can change strategyinfo',9,'change_strategyinfo'),(27,'Can delete strategyinfo',9,'delete_strategyinfo'),(28,'Can add user',10,'add_user'),(29,'Can change user',10,'change_user'),(30,'Can delete user',10,'delete_user'),(31,'Can add acct',11,'add_acct'),(32,'Can change acct',11,'change_acct'),(33,'Can delete acct',11,'delete_acct'),(34,'Can add master_acct',12,'add_master_acct'),(35,'Can change master_acct',12,'change_master_acct'),(36,'Can delete master_acct',12,'delete_master_acct'),(37,'Can add sub_acct',13,'add_sub_acct'),(38,'Can change sub_acct',13,'change_sub_acct'),(39,'Can delete sub_acct',13,'delete_sub_acct'),(40,'Can add broker',14,'add_broker'),(41,'Can change broker',14,'change_broker'),(42,'Can delete broker',14,'delete_broker'),(43,'Can add fund_change_log',15,'add_fund_change_log'),(44,'Can change fund_change_log',15,'change_fund_change_log'),(45,'Can delete fund_change_log',15,'delete_fund_change_log'),(46,'Can add acct_hold',16,'add_acct_hold'),(47,'Can change acct_hold',16,'change_acct_hold'),(48,'Can delete acct_hold',16,'delete_acct_hold');

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

insert  into `auth_user`(`id`,`password`,`last_login`,`is_superuser`,`username`,`first_name`,`last_name`,`email`,`is_staff`,`is_active`,`date_joined`) values (1,'pbkdf2_sha256$20000$essOsaZ1ibAb$7hk4ymJebLlyQzuu7ugmKIBvPm+VBEukRBeFtF+FpRk=','2017-02-21 08:36:00',1,'fafa','','','199201680@163.com',1,1,'2017-01-20 07:24:21');

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

/*Table structure for table `cusfund` */

DROP TABLE IF EXISTS `cusfund`;

CREATE TABLE `cusfund` (
  `trd_date` date NOT NULL,
  `account_id` bigint(20) NOT NULL,
  `fund_balance_total` decimal(20,6) NOT NULL,
  `available_fund` decimal(20,6) NOT NULL,
  `margin_call` decimal(20,6) NOT NULL,
  `risk_degree` decimal(5,4) NOT NULL,
  `pre_balance_zr` decimal(20,6) NOT NULL,
  `pre_balance_zb` decimal(20,6) NOT NULL,
  `balance_zr` decimal(20,6) NOT NULL,
  `balance_zb` decimal(20,6) NOT NULL,
  `total_profit_zr` decimal(20,6) NOT NULL,
  `total_profit_zb` decimal(20,6) NOT NULL,
  `float_profit_zb` decimal(20,6) NOT NULL,
  `spec_charge_against` decimal(20,6) NOT NULL,
  `is_trading_menber` char(1) NOT NULL,
  `currency` char(3) NOT NULL,
  `currency_fund` decimal(20,6) NOT NULL,
  `currency_charge_against` decimal(20,6) NOT NULL,
  `other_currency_mortgage_out` decimal(20,6) NOT NULL,
  `currency_mortgage_margin` decimal(20,6) NOT NULL,
  `total_fund` decimal(20,6) NOT NULL,
  PRIMARY KEY (`trd_date`,`account_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `cusfund` */

/*Table structure for table `data_send` */

DROP TABLE IF EXISTS `data_send`;

CREATE TABLE `data_send` (
  `id` int(11) NOT NULL,
  `d_name` varchar(32) NOT NULL,
  `o_srv` varchar(32) NOT NULL,
  `o_dir` varchar(32) NOT NULL,
  `p_srv` varchar(32) NOT NULL,
  `p_dir` varchar(32) NOT NULL,
  `update_tm` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `data_send` */

/*Table structure for table `delayfeeinfo` */

DROP TABLE IF EXISTS `delayfeeinfo`;

CREATE TABLE `delayfeeinfo` (
  `bid` int(11) NOT NULL,
  `contract_id` varchar(32) NOT NULL,
  `delayfee_tatio` decimal(15,8) NOT NULL,
  `bs_derect` char(1) NOT NULL,
  PRIMARY KEY (`bid`,`contract_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `delayfeeinfo` */

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
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

/*Data for the table `django_content_type` */

insert  into `django_content_type`(`id`,`app_label`,`model`) values (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(11,'operation','acct'),(16,'operation','acct_hold'),(14,'operation','broker'),(15,'operation','fund_change_log'),(12,'operation','master_acct'),(7,'operation','productinfo'),(8,'operation','serverinfo'),(9,'operation','strategyinfo'),(13,'operation','sub_acct'),(10,'operation','user'),(6,'sessions','session');

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

/*Data for the table `django_migrations` */

insert  into `django_migrations`(`id`,`app`,`name`,`applied`) values (1,'contenttypes','0001_initial','2017-01-20 07:22:00'),(2,'auth','0001_initial','2017-01-20 07:22:12'),(3,'admin','0001_initial','2017-01-20 07:22:13'),(4,'contenttypes','0002_remove_content_type_name','2017-01-20 07:22:14'),(5,'auth','0002_alter_permission_name_max_length','2017-01-20 07:22:15'),(6,'auth','0003_alter_user_email_max_length','2017-01-20 07:22:15'),(7,'auth','0004_alter_user_username_opts','2017-01-20 07:22:15'),(8,'auth','0005_alter_user_last_login_null','2017-01-20 07:22:16'),(9,'auth','0006_require_contenttypes_0002','2017-01-20 07:22:16'),(10,'operation','0001_initial','2017-01-20 07:22:16'),(11,'sessions','0001_initial','2017-01-20 07:22:17'),(12,'operation','0002_auto_20170120_1524','2017-01-20 07:25:35'),(13,'operation','0003_serverinfo','2017-01-20 11:10:19'),(14,'operation','0004_auto_20170120_1913','2017-01-20 11:13:46'),(15,'operation','0002_auto_20170207_1528','2017-02-22 08:36:43'),(16,'operation','0003_auto_20170207_1543','2017-02-22 08:36:43');

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

/*Table structure for table `feerate` */

DROP TABLE IF EXISTS `feerate`;

CREATE TABLE `feerate` (
  `id` int(11) NOT NULL AUTO_INCREMENT COMMENT '主键id',
  `bid` int(11) NOT NULL COMMENT '券商id',
  `exchange_id` varchar(32) NOT NULL COMMENT '交易所',
  `contract_id` varchar(32) NOT NULL COMMENT '合约标识',
  `biz_type` char(1) NOT NULL COMMENT '开平标志',
  `feerate_by_amt` decimal(15,8) NOT NULL COMMENT '按金额（成交金额百分比）',
  `feerate_by_qty` decimal(15,8) NOT NULL COMMENT '按数量（每手收费）',
  `update_tm` datetime NOT NULL COMMENT '更新时间',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

/*Data for the table `feerate` */

insert  into `feerate`(`id`,`bid`,`exchange_id`,`contract_id`,`biz_type`,`feerate_by_amt`,`feerate_by_qty`,`update_tm`) values (1,1,'CFFEX','AU','0','0.00020000','1.20000000','0000-00-00 00:00:00');

/*Table structure for table `fts_order` */

DROP TABLE IF EXISTS `fts_order`;

CREATE TABLE `fts_order` (
  `trd_date` char(8) NOT NULL,
  `order_date` char(8) NOT NULL,
  `order_time` timestamp(2) NOT NULL DEFAULT CURRENT_TIMESTAMP(2) ON UPDATE CURRENT_TIMESTAMP(2),
  `order_sn` int(11) NOT NULL,
  `order_id` varchar(10) NOT NULL,
  `order_type` char(1) NOT NULL,
  `mp_ordertype` varchar(1) NOT NULL,
  `cust_code` bigint(20) NOT NULL,
  `cuacct_code` bigint(20) NOT NULL,
  `int_org` smallint(6) NOT NULL,
  `currency` char(1) NOT NULL,
  `trdacct` varchar(10) NOT NULL,
  `trdacct_exid` varchar(10) NOT NULL,
  `stkex` char(1) NOT NULL,
  `stkbd` char(2) NOT NULL,
  `stk_name` varchar(16) NOT NULL,
  `stk_code` varchar(32) NOT NULL,
  `stk_biz` smallint(6) NOT NULL,
  `bs_side` char(1) NOT NULL,
  `order_price` decimal(17,3) NOT NULL,
  `order_qty` int(11) NOT NULL,
  `order_amt` decimal(17,3) NOT NULL,
  `withdrawn_qty` int(11) NOT NULL,
  `matched_qty` int(11) NOT NULL,
  `matched_amt` decimal(17,3) NOT NULL,
  `commision` decimal(17,3) NOT NULL,
  `order_status` char(1) NOT NULL,
  PRIMARY KEY (`trd_date`,`order_sn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `fts_order` */

/*Table structure for table `fts_order_his` */

DROP TABLE IF EXISTS `fts_order_his`;

CREATE TABLE `fts_order_his` (
  `trd_date` char(8) NOT NULL,
  `order_date` char(8) NOT NULL,
  `order_time` timestamp(2) NOT NULL DEFAULT CURRENT_TIMESTAMP(2) ON UPDATE CURRENT_TIMESTAMP(2),
  `order_sn` int(11) NOT NULL,
  `order_id` varchar(10) NOT NULL,
  `order_type` char(1) NOT NULL,
  `mp_ordertype` varchar(1) NOT NULL,
  `cust_code` bigint(20) NOT NULL,
  `cuacct_code` bigint(20) NOT NULL,
  `int_org` smallint(6) NOT NULL,
  `currency` char(1) NOT NULL,
  `trdacct` varchar(10) NOT NULL,
  `trdacct_exid` varchar(10) NOT NULL,
  `stkex` char(1) NOT NULL,
  `stkbd` char(2) NOT NULL,
  `stk_name` varchar(16) NOT NULL,
  `stk_code` varchar(32) NOT NULL,
  `stk_biz` smallint(6) NOT NULL,
  `bs_side` char(1) NOT NULL,
  `order_price` decimal(17,3) NOT NULL,
  `order_qty` int(11) NOT NULL,
  `order_amt` decimal(17,3) NOT NULL,
  `withdrawn_qty` int(11) NOT NULL,
  `matched_qty` int(11) NOT NULL,
  `matched_amt` decimal(17,3) NOT NULL,
  `commision` decimal(17,3) NOT NULL,
  `order_status` char(1) NOT NULL,
  PRIMARY KEY (`trd_date`,`order_sn`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `fts_order_his` */

/*Table structure for table `fund_change_log` */

DROP TABLE IF EXISTS `fund_change_log`;

CREATE TABLE `fund_change_log` (
  `log_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '日志id',
  `acct_type` varchar(32) NOT NULL COMMENT '账户类型',
  `acct_id` varchar(32) NOT NULL COMMENT '账户id',
  `change_fund` decimal(17,2) NOT NULL COMMENT '出入金',
  `desc` varchar(64) NOT NULL COMMENT '备注',
  `log_tm` datetime NOT NULL COMMENT '日志时间',
  PRIMARY KEY (`log_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

/*Data for the table `fund_change_log` */

insert  into `fund_change_log`(`log_id`,`acct_type`,`acct_id`,`change_fund`,`desc`,`log_tm`) values (1,'acct','10007177','1.00','哈哈哈哈','2017-02-20 07:54:57'),(2,'master_acct','66660000201','1.00','test','2017-02-20 08:25:55'),(3,'master_acct','66660000201','1.00','test2','2017-02-20 08:26:57'),(4,'sub_acct','66660000000701','1.00','1','2017-02-20 08:50:40');

/*Table structure for table `gatewayinfo` */

DROP TABLE IF EXISTS `gatewayinfo`;

CREATE TABLE `gatewayinfo` (
  `gw_id` varchar(32) NOT NULL COMMENT 'gateway_id',
  `gw_name` varchar(32) NOT NULL COMMENT 'gateway_name',
  `gw_cfg` varchar(32) NOT NULL COMMENT '对应配置名',
  `port` int(11) NOT NULL COMMENT '端口',
  `gw_srv` varchar(32) NOT NULL COMMENT '所属主机',
  `product` varchar(32) NOT NULL COMMENT '所属产品',
  `desc` varchar(32) NOT NULL COMMENT '备注',
  PRIMARY KEY (`gw_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `gatewayinfo` */

insert  into `gatewayinfo`(`gw_id`,`gw_name`,`gw_cfg`,`port`,`gw_srv`,`product`,`desc`) values ('1','信达期货GW','gw-PropXDFut',9901,'srvxd001','信达自营','信达期货GW'),('2','南华期货-黄金现货GW','gw-PropNHFS',9006,'srvnh001','南华自营','南华期货-黄金现货GW11'),('3','弘金华银-期货GW','gw-HjhyZXFut',9910,'srvzx001','弘金华银','中信期货GW'),('4','弘金世纪1-期货GW','gw-Hjsj1YAFut',9911,'prod001','弘金世纪1号','弘金世纪1-期货GW'),('5','洪荒世纪1-期货GW','gw-Hhsj1NHFut',9910,'prod001','洪荒世纪1号','洪荒世纪1-期货GW'),('6','博益安盈1-期货GW','gw-Byay1NHFu',9910,'pord002','博益安盈1号','博益安盈1-期货GW'),('7','信达股票GW','ss2ison',9906,'srvxd001','信达自营','股票GW'),('8','弘金华银股票GW','ss2ison',9906,'srvzx001','弘金华银','股票GW');

/*Table structure for table `marginrateinfo` */

DROP TABLE IF EXISTS `marginrateinfo`;

CREATE TABLE `marginrateinfo` (
  `bid` int(11) NOT NULL,
  `contract` varchar(32) NOT NULL,
  `exchange_id` varchar(32) NOT NULL,
  `volume_multiple` int(11) NOT NULL,
  `long_marginratio` decimal(12,10) NOT NULL,
  `short_marginratio` decimal(12,10) NOT NULL,
  PRIMARY KEY (`bid`,`contract`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `marginrateinfo` */

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

insert  into `master_acct`(`acc_num`,`acc_name`,`trdacct`,`equity`,`buy_margin`,`sell_margin`,`margin_locked`,`fund_avaril`) values ('666600002','南华自营-期货总账户','10007177','0.00','0.00','0.00','0.00','0.00'),('66660000201','南华自营-黄金现货总账户','16039','0.00','0.00','0.00','0.00','0.00'),('666600004','博益安盈1号 - 期货总账户','12105045','0.00','0.00','0.00','0.00','0.00'),('666600006','洪荒世纪1号 - 期货总账户','12105047','0.00','0.00','0.00','0.00','0.00'),('666600008','信达自营 - 期货总账户','69300002','0.00','0.00','0.00','0.00','0.00'),('666600009','洪荒世纪1号 - 期货总账户','12105047','0.00','0.00','0.00','0.00','0.00'),('666600011','弘金华银 - 期货总账户','120301232','0.00','0.00','0.00','0.00','0.00'),('666600012','弘金华银 - 期货总账户','120301232','0.00','0.00','0.00','0.00','0.00'),('666600014','弘金世纪1号 - 期货总账户','275508085','0.00','0.00','0.00','0.00','0.00'),('666600015','弘金世纪1号 - 期货总账户','275508085','0.00','0.00','0.00','0.00','0.00');

/*Table structure for table `master_acct_hold` */

DROP TABLE IF EXISTS `master_acct_hold`;

CREATE TABLE `master_acct_hold` (
  `trd_date` char(8) NOT NULL COMMENT '交易日期',
  `acc_num` varchar(32) NOT NULL COMMENT '总账号',
  `instrument` varchar(32) NOT NULL COMMENT '合约名',
  `variety` varchar(32) NOT NULL COMMENT '品种名',
  `long_pos` int(11) NOT NULL COMMENT '买持仓',
  `avg_buy_price` decimal(17,3) NOT NULL COMMENT '买均价',
  `short_pos` int(11) NOT NULL COMMENT '卖持仓',
  `avg_sell_price` decimal(17,3) NOT NULL COMMENT '卖均价',
  `pos_pl` decimal(17,2) NOT NULL COMMENT '持仓订市盈亏',
  `margin_occupied` decimal(17,2) NOT NULL COMMENT '保证金占用',
  `sh_mark` char(1) NOT NULL COMMENT '投保标识',
  PRIMARY KEY (`trd_date`,`acc_num`,`instrument`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `master_acct_hold` */

/*Table structure for table `priceserverinfo` */

DROP TABLE IF EXISTS `priceserverinfo`;

CREATE TABLE `priceserverinfo` (
  `ps_id` varchar(4) NOT NULL COMMENT 'PS id',
  `ps_name` varchar(32) NOT NULL COMMENT 'PS name',
  `ps_cfg` varchar(32) NOT NULL COMMENT '对应配置名',
  `ps_srv` varchar(32) NOT NULL COMMENT '所属主机',
  `port` int(11) NOT NULL COMMENT '端口',
  `desc` varchar(32) NOT NULL COMMENT '备注',
  PRIMARY KEY (`ps_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `priceserverinfo` */

insert  into `priceserverinfo`(`ps_id`,`ps_name`,`ps_cfg`,`ps_srv`,`port`,`desc`) values ('1','信达行情','ps-All','srvxd001',10000,'desc'),('2','弘金华银-行情','ps-All','srvzx001',10000,'南华ctp行情'),('3','弘金世纪&洪荒世纪1-行情','pp-All','prod001',10000,'desc'),('4','博益安盈1&横华&博益安盈4-行情','ps-All','pord002',10000,'三产品共用行情'),('5','南华行情','ps-Sgit','srvnh001',9000,'南华行情');

/*Table structure for table `productinfo` */

DROP TABLE IF EXISTS `productinfo`;

CREATE TABLE `productinfo` (
  `pid` int(11) NOT NULL,
  `pname` varchar(32) NOT NULL,
  `admin` varchar(32) NOT NULL,
  `desc` varchar(128) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `productinfo` */

insert  into `productinfo`(`pid`,`pname`,`admin`,`desc`) values (1,'南华自营','世纪盛元','黄金现货、期货'),(2,'洪荒世纪1号','丽海弘金','期货、股票'),(3,'博益安盈1号','丽海弘金','期货、股票'),(4,'弘金华银','世纪盛元','期货、股票'),(5,'信达自营','丽海弘金','期货、股票'),(6,'弘金世纪1号','丽海弘金','期货');

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

insert  into `serverinfo`(`srvnum`,`ip`,`user`,`passwd`,`port`,`productadmin`,`desc`) values ('pord002','172.24.10.34','pmops','pmops@#$',22,'丽海弘金','量化服务器'),('prod001','172.24.58.1','pmops','pmops@#$',22,'丽海弘金','量化服务器'),('srvnh001','172.24.54.1','pmops','pmops@#$',22018,'世纪盛元','量化服务端'),('srvxd001','172.18.12.128','pmops','pmops@#$',22,'世纪盛元','量化服务器'),('srvzx001','172.27.13.179','pmops','pmops@#$',22,'世纪盛元','量化服务端'),('trd004','172.24.53.4','pmops','pmops@#$',22,'世纪盛元','交易服务器'),('trd010','172.24.53.10','pmops','pmops@#$',22,'世纪盛元','交易服务器');

/*Table structure for table `serviceinfo` */

DROP TABLE IF EXISTS `serviceinfo`;

CREATE TABLE `serviceinfo` (
  `ser_id` int(6) NOT NULL AUTO_INCREMENT COMMENT '服务id',
  `ser_name` varchar(32) NOT NULL COMMENT '服务名称',
  `ser_att` varchar(32) NOT NULL COMMENT '服务属性',
  `ser_cfg` varchar(32) NOT NULL COMMENT '服务对应配置名',
  `ser_port` int(11) NOT NULL COMMENT '服务端口',
  `ser_srv` varchar(32) NOT NULL COMMENT '所属主机',
  `ser_stat` varchar(32) DEFAULT NULL COMMENT '服务状态',
  `port_stat` varchar(32) DEFAULT NULL COMMENT '端口状态',
  `desc` varchar(32) NOT NULL COMMENT '备注',
  PRIMARY KEY (`ser_id`)
) ENGINE=InnoDB AUTO_INCREMENT=39 DEFAULT CHARSET=utf8;

/*Data for the table `serviceinfo` */

insert  into `serviceinfo`(`ser_id`,`ser_name`,`ser_att`,`ser_cfg`,`ser_port`,`ser_srv`,`ser_stat`,`port_stat`,`desc`) values (1,'黄金期现套利策略','SS','ss-PropAuArb',9019,'srvnh001','UP','DOWN','黄金期现套利策略'),(2,'商品多因子策略','SS','ss-PropComMulti',9069,'srvnh001',NULL,NULL,'商品多因子策略'),(3,'商品CTA策略','SS','ss-PropComCta',9063,'srvnh001',NULL,NULL,'商品CTA策略'),(4,'黄金跨期套利策略','SS','ss-PropAuCal',9033,'srvnh001',NULL,NULL,'黄金跨期套利策略'),(5,'白银期现套利策略','SS','ss-PropAgArb',9020,'srvnh001',NULL,NULL,'白银期现套利策略'),(6,'南华行情','PS','ps-Sgit',9000,'srvnh001',NULL,NULL,'南华行情'),(7,'南华自营 - 期货GW','GW','gw-PropNHFutSpec',9004,'srvnh001',NULL,NULL,'南华自营 - 期货GW'),(8,'ManualTrader','SS','ss-PropXDMT',10300,'srvxd001',NULL,NULL,'ManualTrader'),(9,'股票多因子','SS','ss-PropXDStkMulti',10301,'srvxd001',NULL,NULL,'股票多因子'),(10,'信达行情','PS','ps-All',10000,'srvxd001',NULL,NULL,'信达行情'),(11,'信达期货GW','GW','gw-PropXDFut',9901,'srvxd001','UP','UP','信达期货GW'),(12,'南华期货-黄金现货GW','GW','gw-PropNHFS',9006,'srvnh001',NULL,NULL,'南华期货-黄金现货GW'),(13,'弘金华银-行情','PS','ps-All',10000,'srvzx001',NULL,NULL,'南华CTP行情'),(14,'弘金华银-期货GW','GW','gw-HjhyZXFut',9910,'srvzx001',NULL,NULL,'中信期货'),(15,'弘金华银-ManualTrader','SS','ss-HjhyMT',10304,'srvzx001',NULL,NULL,'MT'),(16,'弘金华银-股票多因子','SS','ss-HjhyStkMulti',10305,'srvzx001',NULL,NULL,'股票多因子策略'),(17,'弘金华银-统计多因子300投机','SS','ss-HjhyStat300Spec',10306,'srvzx001',NULL,NULL,'统计多因子300投机'),(18,'弘金华银-跨期调仓','SS','ss-HjhyRollover500',10307,'srvzx001',NULL,NULL,'跨期调仓'),(19,'弘金华银-商品多因子','SS','ss-HjhyComMulti',10308,'srvzx001',NULL,NULL,'商品多因子'),(20,'弘金华银-商品CTA','SS','ss-HjhyComCta',10309,'srvzx001',NULL,NULL,'商品CTA'),(21,'弘金华银-ICS平台组合','SS','ss-HjhyIcs500Port',10311,'srvzx001',NULL,NULL,'ICS平台组合'),(22,'信达自营-股票GW','SS2ISON','ss2ison',9906,'srvxd001',NULL,NULL,'股票GW'),(23,'弘金华银-股票GW','SS2ISON','ss2ison',9906,'srvzx001',NULL,NULL,'股票GW'),(24,'弘金世纪&洪荒世纪1-行情','PS','pp-All',10000,'prod001',NULL,NULL,'行情'),(25,'弘金世纪1-期货GW','GW','gw-Hjsj1YAFut',9911,'prod001',NULL,NULL,'弘金世纪1-期货GW'),(26,'弘金世纪1-商品多因子','SS','ss-Hjsj1ComMulti',10300,'prod001',NULL,NULL,'商品多因子'),(27,'洪荒世纪1-期货GW','GW','gw-Hhsj1NHFut',9910,'prod001',NULL,NULL,'期货GW'),(28,'洪荒世纪1-ManualTrader','SS','ss-Hhsj1MT',10307,'prod001',NULL,NULL,'MT'),(29,'洪荒世纪1-商品多因子','SS','ss-Hhsj1ComMulti',10303,'prod001',NULL,NULL,'商品多因子'),(30,'洪荒世纪1-商品CTA','SS','ss-Hhsj1ComCta',10304,'prod001',NULL,NULL,'商品CTA'),(31,'洪荒世纪1-股票多因子','SS','ss-Hhsj1StkMulti',10301,'prod001',NULL,NULL,'股票多因子'),(32,'洪荒世纪1-统计多因子300投机','SS','ss-Hhsj1Stat300Spec',10305,'prod001',NULL,NULL,'统计多因子300投机'),(33,'洪荒世纪1-统计多因子300套保','SS','ss-Hhsj1Stat300Hedge',10306,'prod001',NULL,NULL,'统计多因子300套保'),(34,'博益安盈1&横华自营-行情','PS','ps-All',10000,'pord002',NULL,NULL,'行情'),(35,'博益安盈1-期货GW','GW','gw-Byay1NHFu',9910,'pord002',NULL,NULL,'期货GW'),(36,'博益安盈1-中证500多因子','SS','ss-Byay1StkMulti',10300,'pord002',NULL,NULL,'中证500多因子'),(37,'横华自营-期货GW','GW','gw',9911,'pord002',NULL,NULL,'期货GW'),(38,'横华自营-ManualTrader','SS','ss',10301,'pord002',NULL,NULL,'MT');

/*Table structure for table `strategyinfo` */

DROP TABLE IF EXISTS `strategyinfo`;

CREATE TABLE `strategyinfo` (
  `ss_id` int(8) NOT NULL,
  `ss_name` varchar(32) NOT NULL,
  `ss_cfg` varchar(32) NOT NULL,
  `ss_srv` varchar(32) NOT NULL,
  `port` int(11) NOT NULL,
  `product` varchar(32) NOT NULL,
  `master_acc` varchar(32) NOT NULL,
  `sub_acc` varchar(32) NOT NULL,
  `desc` varchar(32) NOT NULL,
  PRIMARY KEY (`ss_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `strategyinfo` */

insert  into `strategyinfo`(`ss_id`,`ss_name`,`ss_cfg`,`ss_srv`,`port`,`product`,`master_acc`,`sub_acc`,`desc`) values (101,'黄金期现套利策略','ss-PropAuArb','srvnh001',9019,'1','66660000201','66660000000101','黄金期现套利策略'),(103,'中证500多因子策略','ss-Byay1StkMulti','pord002',10300,'3','666600004','666600000003','中证500多因子策略'),(104,'商品多因子策略','ss-PropComMulti','srvnh001',9069,'1','666600002','666600000004','商品多因子策略'),(105,'商品CTA策略','ss-PropComCta','srvnh001',9063,'1','666600002','666600000005','商品CTA策略'),(106,'黄金跨期套利策略','ss-PropAuCal','srvnh001',9033,'1','666600002','666600000006','黄金跨期套利策略'),(107,'白银期现套利策略','ss-PropAgArb','srvnh001',9020,'1','666600002','666600000007','白银期现套利策略'),(108,'商品多因子策略','ss-Hhsj1ComMulti','prod001',10303,'2','666600006','666600000008','商品多因子策略'),(109,'商品CTA策略','ss-Hhsj1ComCta','prod001',10304,'2','666600006','666600000009','商品CTA策略'),(110,'股票多因子策略','ss-Hhsj1StkMulti','prod001',10301,'2','666600006','666600000010','股票多因子策略'),(111,'ManualTrader','ss-PropXDMT','srvxd001',10300,'5','666600008','666600000011','ManualTrader'),(112,'统计多因子300投机','ss-Hhsj1Stat300Spec','prod001',10305,'2','666600006','666600000012','统计多因子300投机'),(113,'统计多因子300套保','ss-Hhsj1Stat300Hedge','prod001',10306,'2','666600009','666600000013','统计多因子300套保'),(114,'ManualTrader','ss-Hhsj1MT','prod001',10307,'2','666600006','666600000014','ManualTrader'),(116,'股票多因子','ss-PropXDStkMulti','srvxd001',10301,'5','666600008','666600000016','股票多因子'),(117,'PortfolioTrader策略','ss-Hhsj1StkMultiPT','prod001',10302,'2','666600006','666600000010','PortfolioTrader策略'),(118,'ManualTrader','ss-HjhyMT','srvzx001',10304,'4','666600011','666600000018','ManualTrader'),(119,'股票多因子','ss-HjhyStkMulti','srvzx001',10305,'4','666600011','666600000020','股票多因子'),(120,'统计多因子300投机','ss-HjhyStat300Spec','srvzx001',10306,'4','666600011','666600000020','统计多因子300投机'),(121,'ManualTrader','ss-Hjsj1MT','prod001',10311,'6','666600014','666600000021','ManualTrader'),(122,'商品多因子','ss-Hjsj1ComMulti','prod001',10300,'6','666600014','666600000022','商品多因子'),(123,'跨期调仓','ss-HjhyRollover500','srvzx001',10307,'4','666600011','666600000023','跨期调仓'),(124,'商品多因子','ss-HjhyComMulti','srvzx001',10308,'4','666600011','666600000024','商品多因子'),(125,'商品CTA','ss-HjhyComCta','srvzx001',10309,'4','666600011','666600000025','商品CTA'),(126,'ICS平台组合','ss-HjhyIcs500Port','srvzx001',10311,'4','666600011','666600000026','ICS平台组合');

/*Table structure for table `sub_acct` */

DROP TABLE IF EXISTS `sub_acct`;

CREATE TABLE `sub_acct` (
  `acc_num` varchar(32) NOT NULL,
  `acc_name` varchar(32) NOT NULL,
  `master_acct` varchar(32) NOT NULL,
  `equity` decimal(17,2) NOT NULL,
  `margin_locked` decimal(17,2) NOT NULL,
  `buy_margin` decimal(17,2) NOT NULL,
  `sell_margin` decimal(17,2) NOT NULL,
  `fund_avaril` decimal(17,2) NOT NULL,
  PRIMARY KEY (`acc_num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `sub_acct` */

insert  into `sub_acct`(`acc_num`,`acc_name`,`master_acct`,`equity`,`margin_locked`,`buy_margin`,`sell_margin`,`fund_avaril`) values ('66660000000101','南华自营-黄金期现套利策略子账户','66660000201','0.00','0.00','0.00','0.00','0.00'),('666600000003','博益安盈1号-中证500多因子策略子账户','666600004','0.00','0.00','0.00','0.00','0.00'),('666600000004','南华自营-商品多因子策略子账户','666600002','0.00','0.00','0.00','0.00','0.00'),('666600000005','南华自营-商品CTA策略子账户','666600002','0.00','0.00','0.00','0.00','0.00'),('666600000006','南华自营-黄金跨期套利策略子账户','666600002','0.00','0.00','0.00','0.00','0.00'),('666600000007','南华自营-白银期现套利策略子账户','66660000201','0.00','0.00','0.00','0.00','0.00'),('666600000008','洪荒世纪1号-商品多因子策略子账户','666600006','0.00','0.00','0.00','0.00','0.00'),('666600000009','洪荒世纪1号-商品CTA策略子账户','666600006','0.00','0.00','0.00','0.00','0.00'),('666600000010','洪荒世纪1号-股票多因子策略子账户','666600006','0.00','0.00','0.00','0.00','0.00'),('666600000011','信达自营-ManualTrader策略子账户','666600008','0.00','0.00','0.00','0.00','0.00'),('666600000012','洪荒世纪1号-统计多因子300投机策略子账户','666600006','0.00','0.00','0.00','0.00','0.00'),('666600000013','洪荒世纪1号-统计多因子300套保策略子账户','666600009','0.00','0.00','0.00','0.00','0.00'),('666600000014','洪荒世纪1号-ManualTrader策略子账户','666600006','0.00','0.00','0.00','0.00','0.00'),('666600000015','洪荒世纪1号-现金管理子账户','666600006','0.00','0.00','0.00','0.00','0.00'),('666600000016','信达自营-股票多因子策略子账户','666600008','0.00','0.00','0.00','0.00','0.00'),('666600000018','弘金华银-ManualTrader策略子账户','666600011','0.00','0.00','0.00','0.00','0.00'),('666600000019','弘金华银-股票多因子策略子账户','666600011','0.00','0.00','0.00','0.00','0.00'),('666600000020','弘金华银-统计多因子300投机策略子账户','666600011','0.00','0.00','0.00','0.00','0.00'),('666600000021','弘金世纪1号-ManualTrader策略子账户','666600014','0.00','0.00','0.00','0.00','0.00'),('666600000022','弘金世纪1号-商品多因子策略子账户','666600014','0.00','0.00','0.00','0.00','0.00'),('666600000023','弘金华银-跨期调仓策略子账户','666600011','0.00','0.00','0.00','0.00','0.00'),('666600000024','弘金华银-商品多因子策略子账户','666600011','0.00','0.00','0.00','0.00','0.00'),('666600000025','弘金华银-商品CTA策略子账户','666600011','0.00','0.00','0.00','0.00','0.00'),('666600000026','弘金华银-ICS平台组合策略子账户','666600011','0.00','0.00','0.00','0.00','0.00');

/*Table structure for table `sub_acct_hold` */

DROP TABLE IF EXISTS `sub_acct_hold`;

CREATE TABLE `sub_acct_hold` (
  `trd_date` char(8) NOT NULL COMMENT '交易日期',
  `acc_num` varchar(32) NOT NULL COMMENT '总账号',
  `instrument` varchar(32) NOT NULL COMMENT '合约名',
  `variety` varchar(32) NOT NULL COMMENT '品种名',
  `long_pos` int(11) NOT NULL COMMENT '买持仓',
  `avg_buy_price` decimal(17,3) NOT NULL COMMENT '买均价',
  `short_pos` int(11) NOT NULL COMMENT '卖持仓',
  `avg_sell_price` decimal(17,3) NOT NULL COMMENT '卖均价',
  `pos_pl` decimal(17,2) NOT NULL COMMENT '持仓订市盈亏',
  `margin_occupied` decimal(17,2) NOT NULL COMMENT '保证金占用',
  `sh_mark` char(1) NOT NULL COMMENT '投保标识',
  PRIMARY KEY (`trd_date`,`acc_num`,`instrument`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `sub_acct_hold` */

/*Table structure for table `userinfo` */

DROP TABLE IF EXISTS `userinfo`;

CREATE TABLE `userinfo` (
  `username` varchar(50) NOT NULL,
  `passwd` varchar(50) NOT NULL,
  `tel` varchar(50) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `permission` char(1) NOT NULL,
  `desc` varchar(32) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `userinfo` */

insert  into `userinfo`(`username`,`passwd`,`tel`,`email`,`permission`,`desc`) values ('pmops','pmops@#$','1900','pmops@hongkingsystem.com','0','系统管理员');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
