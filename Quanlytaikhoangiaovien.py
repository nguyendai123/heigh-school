from Quanlyhocsinh import mydb

mysubcur1 = mydb.cursor()
mysubcur1.execute('select Tên_đăng_nhập,Mật_khẩu,Họ_và_tên from taikhoangiaovien')
Account_Password = mysubcur1.fetchall()
Account_Password_list = []
Name_list = []
for i in Account_Password:
    Account_Password_list.append((i[0],i[1]))
    
    Name_list.append(i[2])

# mycursor = mydb.cursor()
# mycursor.execute(("SELECT Học_lực,COUNT(*) FROM hocsinh Where Lớp='6A' Group by Học_lực"))
# Chưa_xếp_loại = mycursor.fetchall()
# print((Chưa_xếp_loại[0]))
# Chưa_xếp_loại[0] = list(Chưa_xếp_loại[0])
# print((Chưa_xếp_loại[0]))

# mycursor.execute(("SELECT COUNT(*) FROM hocsinh WHERE Học_lực = 'Giỏi' and Lớp = %s"),('6A',))
# Giỏi = mycursor.fetchone()
# Giỏi = list(Giỏi) 
# print(Giỏi[0])  
#Giỏi_ptrăm = round(Giỏi[0]/Sĩ_số[0]*100,2)