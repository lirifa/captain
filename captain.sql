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

/*Table structure for table `auth_group` */

DROP TABLE IF EXISTS `auth_group`;

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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

/*Table structure for table `broker` */

DROP TABLE IF EXISTS `broker`;

CREATE TABLE `broker` (
  `bid` int(11) NOT NULL,
  `bname` varchar(32) NOT NULL,
  `blname` varchar(128) NOT NULL,
  PRIMARY KEY (`bid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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

/*Table structure for table `delayfeeinfo` */

DROP TABLE IF EXISTS `delayfeeinfo`;

CREATE TABLE `delayfeeinfo` (
  `bid` int(11) NOT NULL,
  `contract_id` varchar(32) NOT NULL,
  `delayfee_tatio` decimal(15,8) NOT NULL,
  `bs_derect` char(1) NOT NULL,
  PRIMARY KEY (`bid`,`contract_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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

/*Table structure for table `django_content_type` */

DROP TABLE IF EXISTS `django_content_type`;

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_3ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

/*Table structure for table `django_migrations` */

DROP TABLE IF EXISTS `django_migrations`;

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

/*Table structure for table `django_session` */

DROP TABLE IF EXISTS `django_session`;

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `feerate` */

DROP TABLE IF EXISTS `feerate`;

CREATE TABLE `feerate` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `bid` int(11) NOT NULL COMMENT '券商id',
  `exchange_id` varchar(32) NOT NULL COMMENT '交易所',
  `contract_id` varchar(32) NOT NULL COMMENT '合约标识',
  `biz_type` char(1) NOT NULL COMMENT '开平标志',
  `feerate_by_amt` decimal(15,8) NOT NULL COMMENT '按金额（成交金额百分比）',
  `feerate_by_qty` decimal(15,8) NOT NULL COMMENT '按数量（每手收费）',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8;

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

/*Table structure for table `gwinfo` */

DROP TABLE IF EXISTS `gwinfo`;

CREATE TABLE `gwinfo` (
  `gw_id` varchar(4) NOT NULL COMMENT 'gateway_id',
  `gw_name` varchar(32) NOT NULL COMMENT 'gateway_name',
  `stat` char(1) NOT NULL COMMENT '状态',
  `clear_tm` datetime NOT NULL COMMENT '清算时间',
  `oper` varchar(32) NOT NULL COMMENT '执行人',
  PRIMARY KEY (`gw_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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

/*Table structure for table `marketinfo` */

DROP TABLE IF EXISTS `marketinfo`;

CREATE TABLE `marketinfo` (
  `stkex` char(1) NOT NULL,
  `exchange_id` varchar(32) NOT NULL,
  `market_name` varchar(32) NOT NULL,
  PRIMARY KEY (`stkex`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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

/*Table structure for table `productinfo` */

DROP TABLE IF EXISTS `productinfo`;

CREATE TABLE `productinfo` (
  `pid` int(11) NOT NULL,
  `pname` varchar(32) NOT NULL,
  `admin` varchar(32) NOT NULL,
  `desc` varchar(128) NOT NULL,
  PRIMARY KEY (`pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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

/*Table structure for table `serviceinfo` */

DROP TABLE IF EXISTS `serviceinfo`;

CREATE TABLE `serviceinfo` (
  `ser_id` varchar(8) NOT NULL COMMENT '服务id',
  `ser_name` varchar(32) NOT NULL COMMENT '服务名称',
  `ser_att` varchar(32) NOT NULL COMMENT '服务属性',
  `ser_cfg` varchar(32) NOT NULL COMMENT '服务对应配置名',
  `ser_port` int(11) NOT NULL COMMENT '服务端口',
  `ser_srv` varchar(32) NOT NULL COMMENT '所属主机',
  `desc` varchar(32) NOT NULL COMMENT '备注',
  PRIMARY KEY (`ser_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Table structure for table `strategyinfo` */

DROP TABLE IF EXISTS `strategyinfo`;

CREATE TABLE `strategyinfo` (
  `sid` int(8) NOT NULL,
  `sname` varchar(32) NOT NULL,
  `scfg` varchar(32) NOT NULL,
  `ssrv` varchar(32) NOT NULL,
  `port` int(11) NOT NULL,
  `product` int(8) NOT NULL,
  `master_acc` varchar(32) NOT NULL,
  `sub_acc` varchar(32) NOT NULL,
  `desc` varchar(32) NOT NULL,
  PRIMARY KEY (`sid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

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

/*Table structure for table `userinfo` */

DROP TABLE IF EXISTS `userinfo`;

CREATE TABLE `userinfo` (
  `username` varchar(50) NOT NULL,
  `passwd` varchar(50) NOT NULL,
  `phone_num` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
