 ALTER TABLE `captain`.`strategyinfo` CHANGE `product` `product` VARCHAR(32) NOT NULL; 

ALTER TABLE `captain`.`serviceinfo` ADD COLUMN `ser_stat` VARCHAR(32) NULL COMMENT '服务状态' AFTER `ser_srv`, ADD COLUMN `port_stat` VARCHAR(32) NULL COMMENT '端口状态' AFTER `ser_stat`; 

ALTER TABLE `captain`.`feerate` ADD COLUMN `update_tm` DATETIME NOT NULL COMMENT '更新时间' AFTER `feerate_by_qty`; 

