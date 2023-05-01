DROP TABLE if EXISTS `giaovien`;

CREATE TABLE `giaovien` (
    `ID` char(8) NOT NULL,
    `Họ_và_tên` varchar(50) NOT NULL,
    `Ngày sinh` varchar(10) NOT NULL,
    `Số_điện_thoại` VARCHAR(10) DEFAULT NULL,
    `Chủ_nhiệm_lớp` varchar(5) DEFAULT NULL,
    `Giới_tính` char(4) NOT NULL,
    `Chuyên_môn` char(10) NOT NULL,
    `Trình_độ` char(10) NOT NULL,
    `Ghi chú` varchar(7) DEFAULT NULL,
    PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `giaovien`  VALUES (23111967,'Nguyễn Phú Đồng','23/11/1967','0914302430','6A','Nam','Toán','Thạc sĩ',NULL);
INSERT INTO `giaovien`  VALUES (12061978,'Huỳnh Văn Nhứt','12/06/1978','0914113578','6B','Nam','Ngữ văn','Thạc sĩ',NULL);
INSERT INTO `giaovien`  VALUES (25101975,'Nguyễn Thị Minh Hằng','25/10/1975','0914909000','7A','Nữ','Toán','Thạc sĩ',NULL);
INSERT INTO `giaovien`  VALUES (12121966,'Trần Thị Thanh Hảo','12/12/1966','0914560298','7B','Nữ','Vật lý','Thạc sĩ',NULL);
INSERT INTO `giaovien`  VALUES (08031985,'Lương Thị Phương','08/03/1985','0395656357','8A','Nữ','Lịch sử','Thạc sĩ',NULL);
INSERT INTO `giaovien`  VALUES (25111979,'Hồ Thị Quỳnh Giang','25/11/1979','0935062406','8B','Nữ','Tin học','Thạc sĩ',NULL);
INSERT INTO `giaovien`  VALUES (06011976,'Đỗ Thị Ngọc Lan','06/01/1976','0972874104','9A','Nữ','Ngữ văn','Thạc sĩ',NULL);
INSERT INTO `giaovien`  VALUES (11011987,'Đoàn Minh Long','11/01/1987','0976193671','9B','Nam','GDCD','Thạc sĩ',NULL);

INSERT INTO `giaovien`  VALUES (11011989,'Trịnh Xuân Tiến Bry','11/01/1989','0935193671',NULL,'Nam','GDCD','Thạc sĩ',NULL);
