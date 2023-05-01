DROP TABLE if EXISTS `taikhoangiaovien`
CREATE TABLE `taikhoangiaovien` (
`ID` char(8) NOT NULL,
`Họ_và_tên` varchar(50) NOT NULL,
`Tên_đăng_nhập` varchar(50) NOT NULL,
`Mật_khẩu` varchar(50) NOT NULL,
`Chức_vụ` varchar(50) NOT NULL
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `taikhoangiaovien`  VALUES ('23111967','Nguyễn Phú Đồng','23111967','Dong1967','Phó hiệu trưởng');
INSERT INTO `taikhoangiaovien`  VALUES ('12061978','Huỳnh Văn Nhứt','12061978','Nhut1978','Giáo viên');
INSERT INTO `taikhoangiaovien`  VALUES (25101975,'Nguyễn Thị Minh Hằng','25101975','Hang1975','Giáo viên',NULL);
INSERT INTO `taikhoangiaovien`  VALUES (12121966,'Trần Thị Thanh Hảo','12121966','Hao1966','Hiệu trưởng',NULL);
INSERT INTO `taikhoangiaovien`  VALUES (08031985,'Lương Thị Phương','08031985','Phuong1985','Giáo viên',NULL);
INSERT INTO `taikhoangiaovien`  VALUES (25111979,'Hồ Thị Quỳnh Giang','25111979','Giang1979','Giáo viên',NULL);
INSERT INTO `taikhoangiaovien`  VALUES (06011976,'Đỗ Thị Ngọc Lan','06011976','Lan1967','Phó hiệu trưởng',NULL);
INSERT INTO `taikhoangiaovien`  VALUES (11011987,'Đoàn Minh Long','11011987','Long1987','Giáo viên',NULL);

DELETE FROM `taikhoangiaovien` WHERE ID = 12061978;

select Chuyên_môn,Họ_và_tên,Lớp_được_dạy from giaovien 

