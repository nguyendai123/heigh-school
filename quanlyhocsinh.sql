-- Active: 1653597599247@@127.0.0.1@3306@quanlyhocsinh
DROP TABLE if EXISTS `hocsinh`;
CREATE TABLE `hocsinh` (
  `Họ và tên` varchar(50) NOT NULL,
  `Ngày sinh` VARCHAR(10) NOT NULL,
  `ID` CHAR(7) NOT NULL,
  `Lớp` VARCHAR(5) NOT NULL,
  `Giới tính` CHAR(4) not null,
  `Nơi sinh` varchar(50) NOT NULL,
  `Dân tộc` char(10) NOT NULL,
  `Mồ côi` char (5) DEFAULT NULL,
  `Địa chỉ` varchar(50) NOT NULL,
  `Ghi chú` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

INSERT INTO `hocsinh` VALUES ('Từ Minh Anh','05/02/2010','2010001','6A','Nữ','Hà Nội','Kinh','Không','Đống Đa,Hà Nội',NULL);
INSERT INTO `hocsinh` VALUES ('Chung Ngọc Gia Bảo','21/09/2010','2010002','6A','Nam','Hà Nội','Kinh','Không','Đống Đa,Hà Nội',NULL);
INSERT INTO `hocsinh` VALUES ('Hứa Thị Mỹ Duyên','01/02/2010','2010003','6A','Nữ','Hà Nội','Kinh','Không','Cầu Giấy,Hà Nội',NULL);
INSERT INTO `hocsinh` VALUES ('Dương Thành Đạt','09/11/2010','2010004','6A','Nam','Hà Nội','Kinh','Không','Đống Đa,Hà Nội',NULL);
INSERT INTO `hocsinh` VALUES ('Nguyễn Quốc Hào','21/08/2010','2010005','6A','Nam','Hà Nội','Kinh','Không','Đống Đa,Hà Nội',NULL);
INSERT INTO `hocsinh` VALUES ('Nguyễn Thanh Hào','07/03/2010','2010006','6A','Nam','Hà Nội','Kinh','Không','Đống Đa,Hà Nội',NULL);
INSERT INTO `hocsinh` VALUES ('Nguyễn Đào Ngọc Hân','07/07/2010','2010007','6A','Nữ','Hà Nội','Kinh','Không','Đống Đa,Hà Nội',NULL);
INSERT INTO `hocsinh` VALUES ('Tô Minh Hoàng','11/05/2010','2010008','6A','Nam','Hà Nội','Kinh','Không','Cầu Giấy,Hà Nội',NULL);
INSERT INTO `hocsinh` VALUES ('Lâm Quốc Hùng','30/07/2010','2010009','6A','Nam','Hà Nội','Kinh','Không','Đống Đa,Hà Nội',NULL);
INSERT INTO `hocsinh` VALUES ('Trần Minh Khánh','18/10/2010','2010010','6A','Nam','Hà Nội','Kinh','Không','Đống Đa,Hà Nội',NULL);
INSERT INTO `hocsinh` VALUES ('Nguyễn Đăng Khoa','18/03/2010','2010011','6A','Nam','Hà Nội','Kinh','Không','Đống Đa,Hà Nội',NULL);
INSERT INTO `hocsinh` VALUES ('Trần Văn Kiệt','28/09/2010','2010012','6A','Nam','Hà Nội','Kinh','Không','Cầu Giấy,Hà Nội',NULL);
INSERT INTO `hocsinh` VALUES ('Đặng Mỹ Kim','13/03/2010','2010013','6A','Nữ','Hà Nội','Kinh','Không','Cầu Giấy,Hà Nội',NULL);
INSERT INTO `hocsinh` VALUES ('Châu Hồng Liên','23/12/2010','2010014','6A','Nữ','Hà Nội','Kinh','Không','Đống Đa,Hà Nội',NULL);
INSERT INTO `hocsinh` VALUES ('Triệu Gia Mẫn','29/10/2010','2010015','6A','Nữ','Hà Nội','Kinh','Không','Đống Đa,Hà Nội',NULL);


SELECT * FROM hocsinh;



SELECT * FROM bangdiemcanhan;

SELECT * FROM bangdiemcanhan;

SELECT * FROM bangdiemcanhan;

SELECT * FROM giaovien;

SELECT * FROM bangdiemcanhan;

SELECT * FROM bangdiemcanhan;

SELECT * FROM giaovien;

SELECT * FROM giaovien;

SELECT * FROM giaovien;

SELECT * FROM giaovien;

SELECT `Tên_lớp`,`Mã_lớp`,`Giáo_viên_chủ_nhiệm`,`Niên_khóa` FROM lophoc;

SELECT * FROM xeploaihocluc;

SELECT * FROM hocsinh;