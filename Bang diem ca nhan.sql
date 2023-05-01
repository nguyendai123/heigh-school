DROP TABLE if EXISTS `bangdiemcanhan` ;

CREATE TABLE `bangdiemcanhan` (
`ID` char(7) NOT NULL,
`Môn học` char(10) NOT NULL,
`Mã môn` varchar(10) NOT NULL,
`Điểm_miệng` float(10) DEFAULT NULL,
`Điểm_15_phút` float(10) DEFAULT NULL,
`Điểm_1_tiết` float(10) DEFAULT NULL,
`Điểm_giữa_kì` float(10) DEFAULT NULL,
`Điểm_cuối_kì` float(10) DEFAULT NULL,
`Điểm_tổng_kết_học_kì_I_hoặc_II` float(10) DEFAULT NULL
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
INSERT INTO `bangdiemcanhan`  VALUES (2010001,'Ngữ văn','NV20221',8,9,7,9,10,NULL);
INSERT INTO `bangdiemcanhan`  VALUES (2010001,'Toán','T20221',8.5,9,7,9.5,10,NULL);
INSERT INTO `bangdiemcanhan`  VALUES (2010002,'Toán','T20221',7,9,8,8,10,NULL);
INSERT INTO `bangdiemcanhan`  VALUES (2010003,'Toán','T20221',9,8,7,8,9,NULL);
INSERT INTO `bangdiemcanhan`  VALUES (2010004,'Toán','T20221',10,9,8,9,9,NULL);
INSERT INTO `bangdiemcanhan`  VALUES (2010005,'Toán','T20221',8,10,9,10,7,NULL);
INSERT INTO `bangdiemcanhan`  VALUES (2010006,'Toán','T20221',9,10,9,9,7.5,NULL);
INSERT INTO `bangdiemcanhan`  VALUES (2010007,'Toán','T20221',9,8,9,8,8,NULL);
INSERT INTO `bangdiemcanhan`  VALUES (2010008,'Toán','T20221',10,8,8,9,8,NULL);
INSERT INTO `bangdiemcanhan`  VALUES (2010009,'Toán','T20221',10,10,9,10,8,NULL);
INSERT INTO `bangdiemcanhan`  VALUES (2010010,'Toán','T20221',9,10,9.5,9,9,NULL);

SELECT ID, Điểm_miệng, Điểm_15_phút, (Điểm_miệng + Điểm_15_phút)/2 as Điểm_tổng_kết_học_kì_I_hoặc_II  FROM bangdiemcanhan;
UPDATE bangdiemcanhan SET Điểm_tổng_kết_học_kì_I_hoặc_II = NULL;
DELETE FROM bangdiemcanhan WHERE ID = 2010002 and Môn_học = 'Ngữ văn';

SELECT hocsinh.Họ_và_tên, Lớp, giaovien.Họ_và_tên as Giáo_viên FROM hocsinh
JOIN giaovien ON Lớp = Chủ_nhiệm_lớp