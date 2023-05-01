DROP TABLE if EXISTS `thoikhoabieu`;
CREATE TABLE `thoikhoabieu`(
    `STT` int(20) NOt NULL PRIMARY KEY Auto_increment,
    `Tiết`  INT(8) NOt NULL , 
    `Thứ_2` VARCHAR(10) DEFAULT NULL,
    `Thứ_3` VARCHAR(10) DEFAULT NULL,
    `Thứ_4` VARCHAR(10) DEFAULT NULL,
    `Thứ_5` VARCHAR(10) DEFAULT NULL,
    `Thứ_6` VARCHAR(10) DEFAULT NULL,
    `Thứ_7` VARCHAR(10) DEFAULT NULL,
    `Lớp` CHAR(5) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

ALTER Table `thoikhoabieu` AUTO_INCREMENT=;
update thoikhoabieu set `Lớp` ='6A' WHERE Thứ_3 = (NULL) ;
INSERT into `thoikhoabieu` VALUES(NULL,1,'Hello','','','','','','');