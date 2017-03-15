/*
SQLyog Ultimate v11.24 (32 bit)
MySQL - 5.7.17-log : Database - captain
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

/*Table structure for table `serviceinfo` */

DROP TABLE IF EXISTS `serviceinfo`;

CREATE TABLE `serviceinfo` (
  `ser_id` varchar(8) NOT NULL COMMENT '服务id',
  `ser_name` varchar(32) NOT NULL COMMENT '服务名称',
  `ser_att` varchar(32) NOT NULL COMMENT '服务属性',
  `ser_cfg` varchar(32) NOT NULL COMMENT '服务对应配置名',
  `ser_port` int(11) NOT NULL COMMENT '服务端口',
  `ser_srv` varchar(32) NOT NULL COMMENT '所属主机',
  `ser_stat` varchar(32) DEFAULT NULL COMMENT '服务状态',
  `port_stat` varchar(32) DEFAULT NULL COMMENT '端口状态',
  `desc` varchar(32) NOT NULL COMMENT '备注',
  PRIMARY KEY (`ser_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

/*Data for the table `serviceinfo` */

insert  into `serviceinfo`(`ser_id`,`ser_name`,`ser_att`,`ser_cfg`,`ser_port`,`ser_srv`,`ser_stat`,`port_stat`,`desc`) values ('1','黄金期现套利策略','SS','ss-PropAuArb',9019,'srvnh001','UP','DOWN','黄金期现套利策略'),('10','信达行情','PS','ps-All',10000,'srvxd001',NULL,NULL,'信达行情'),('11','信达期货GW','GW','gw-PropXDFut',9901,'srvxd001','UP','UP','信达期货GW'),('12','南华期货-黄金现货GW','GW','gw-PropNHFS',9006,'srvnh001',NULL,NULL,'南华期货-黄金现货GW'),('13','弘金华银-行情','PS','ps-All',10000,'srvzx001',NULL,NULL,'南华CTP行情'),('14','弘金华银-期货GW','GW','gw-HjhyZXFut',9910,'srvzx001',NULL,NULL,'中信期货'),('15','弘金华银-ManualTrader','SS','ss-HjhyMT',10304,'srvzx001',NULL,NULL,'MT'),('16','弘金华银-股票多因子','SS','ss-HjhyStkMulti',10305,'srvzx001',NULL,NULL,'股票多因子策略'),('17','弘金华银-统计多因子300投机','SS','ss-HjhyStat300Spec',10306,'srvzx001',NULL,NULL,'统计多因子300投机'),('18','弘金华银-跨期调仓','SS','ss-HjhyRollover500',10307,'srvzx001',NULL,NULL,'跨期调仓'),('19','弘金华银-商品多因子','SS','ss-HjhyComMulti',10308,'srvzx001',NULL,NULL,'商品多因子'),('2','商品多因子策略','SS','ss-PropComMulti',9069,'srvnh001',NULL,NULL,'商品多因子策略'),('20','弘金华银-商品CTA','SS','ss-HjhyComCta',10309,'srvzx001',NULL,NULL,'商品CTA'),('21','弘金华银-ICS平台组合','SS','ss-HjhyIcs500Port',10311,'srvzx001',NULL,NULL,'ICS平台组合'),('22','信达自营-股票GW','SS2ISON','ss2ison',9906,'srvxd001',NULL,NULL,'股票GW'),('23','弘金华银-股票GW','SS2ISON','ss2ison',9906,'srvzx001',NULL,NULL,'股票GW'),('24','弘金世纪&洪荒世纪1-行情','PS','pp-All',10000,'prod001',NULL,NULL,'行情'),('25','弘金世纪1-期货GW','GW','gw-Hjsj1YAFut',9911,'prod001',NULL,NULL,'弘金世纪1-期货GW'),('26','弘金世纪1-商品多因子','SS','ss-Hjsj1ComMulti',10300,'prod001',NULL,NULL,'商品多因子'),('27','洪荒世纪1-期货GW','GW','gw-Hhsj1NHFut',9910,'prod001',NULL,NULL,'期货GW'),('28','洪荒世纪1-ManualTrader','SS','ss-Hhsj1MT',10307,'prod001',NULL,NULL,'MT'),('29','洪荒世纪1-商品多因子','SS','ss-Hhsj1ComMulti',10303,'prod001',NULL,NULL,'商品多因子'),('3','商品CTA策略','SS','ss-PropComCta',9063,'srvnh001',NULL,NULL,'商品CTA策略'),('30','洪荒世纪1-商品CTA','SS','ss-Hhsj1ComCta',10304,'prod001',NULL,NULL,'商品CTA'),('31','洪荒世纪1-股票多因子','SS','ss-Hhsj1StkMulti',10301,'prod001',NULL,NULL,'股票多因子'),('32','洪荒世纪1-统计多因子300投机','SS','ss-Hhsj1Stat300Spec',10305,'prod001',NULL,NULL,'统计多因子300投机'),('33','洪荒世纪1-统计多因子300套保','SS','ss-Hhsj1Stat300Hedge',10306,'prod001',NULL,NULL,'统计多因子300套保'),('34','博益安盈1&横华自营-行情','PS','ps-All',10000,'pord002',NULL,NULL,'行情'),('35','博益安盈1-期货GW','GW','gw-Byay1NHFu',9910,'pord002',NULL,NULL,'期货GW'),('36','博益安盈1-中证500多因子','SS','ss-Byay1StkMulti',10300,'pord002',NULL,NULL,'中证500多因子'),('37','横华自营-期货GW','GW','gw',9911,'pord002',NULL,NULL,'期货GW'),('38','横华自营-ManualTrader','SS','ss',10301,'pord002',NULL,NULL,'MT'),('4','黄金跨期套利策略','SS','ss-PropAuCal',9033,'srvnh001',NULL,NULL,'黄金跨期套利策略'),('5','白银期现套利策略','SS','ss-PropAgArb',9020,'srvnh001',NULL,NULL,'白银期现套利策略'),('6','南华行情','PS','ps-Sgit',9000,'srvnh001',NULL,NULL,'南华行情'),('7','南华自营 - 期货GW','GW','gw-PropNHFutSpec',9004,'srvnh001',NULL,NULL,'南华自营 - 期货GW'),('8','ManualTrader','SS','ss-PropXDMT',10300,'srvxd001',NULL,NULL,'ManualTrader'),('9','股票多因子','SS','ss-PropXDStkMulti',10301,'srvxd001',NULL,NULL,'股票多因子');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
