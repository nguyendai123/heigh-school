import PySimpleGUI as sg
from Quanlyhocsinh import mydb
import Quanlylophoc as lh
mycursor4 = mydb.cursor()
study_list = []
attitude_list = []
title = ''
layout = [[sg.Button('Xếp loại học tập',k='-STUDY-',use_ttk_buttons=True),
           sg.Button('Xếp loại hạnh kiểm',k='-ATTITUDE-',use_ttk_buttons=True),
           sg.Button('Khen thưởng,kỷ luật',k='-REWARD-',use_ttk_buttons=True)]]

study_heading = ['Lớp','Sĩ_số','Giỏi','Giỏi_%','Khá','Khá_%','Trung_bình','Trung_bình_%','Yếu','Yếu_%','Chưa_xếp_loại','Ghi chú']
attitude_heading = ['Lớp','Sĩ_số','Tốt','Tốt_%','Khá','Khá_%','Yếu','Yếu_%','Kém','Kém_%','Ghi chú']
report_lo = [[sg.Frame('Các tác vụ',layout)],
             [sg.Text('',font = 'Calibra 20',k='-TITLE-')],
             [sg.Table(study_list,study_heading,
                       
                       background_color='LightBlue4',
                        text_color='white',change_submits=True,visible=False,k='-STUDYTB-')],
             [sg.Exit(k='-EXIT5-',visible=False)]
             ]

def Thống_kê_xếp_loại_học_tập(window):
    study_list.clear()
    Tự_động_tính_xếp_loại_học_lực()
    mycursor4.execute('select * from xeploaihocluc')
    study = mycursor4.fetchall()
    for i in study:
        study_list.append(list(i))
    window['-TITLE-'].update('\tXếp loại học tập')    
    window['-STUDYTB-'].update(study_list,visible=True)    
    
def Thống_kê_xếp_loại_hạnh_kiểm(window):
    attitude_list.clear()
    Tự_động_tính_xếp_loại_hạnh_kiểm() 
    mycursor4.execute('select * from xeploaihanhkiem')
    attitude = mycursor4.fetchall()
    for i in attitude:
        attitude_list.append(list(i))
    window['-TITLE-'].update('\tXếp loại hạnh kiểm')
    window['-STUDYTB-'].update(attitude_list,visible=True)    
    
    
def Tự_động_tính_xếp_loại_học_lực():
    mycursor4.execute("Delete from xeploaihocluc")
    for i in range(len(lh.cls_list)):
        
        mycursor4.execute(("SELECT COUNT(*) FROM hocsinh WHERE Lớp = %s"),(lh.cls_list[i][0],))
        Sĩ_số = mycursor4.fetchone()
        Sĩ_số = list(Sĩ_số)
        
        mycursor4.execute(("SELECT COUNT(*) FROM hocsinh WHERE Học_lực = 'Giỏi' and Lớp = %s"),(lh.cls_list[i][0],))
        Giỏi = mycursor4.fetchone()   
        Giỏi_ptrăm = round(Giỏi[0]/Sĩ_số[0]*100,2)
        
        mycursor4.execute(("SELECT COUNT(*) FROM hocsinh WHERE Học_lực = 'Khá' and Lớp = %s"),(lh.cls_list[i][0],))
        Khá = mycursor4.fetchone()
        Khá_ptrăm = round(Khá[0]/Sĩ_số[0]*100,2)
        
        mycursor4.execute(("SELECT COUNT(*) FROM hocsinh WHERE Học_lực = 'Trung_bình' and Lớp = %s"),(lh.cls_list[i][0],))
        Trung_bình = mycursor4.fetchone()
        Trung_bình_ptrăm = round(Trung_bình[0]/Sĩ_số[0]*100,2)
        
        mycursor4.execute(("SELECT COUNT(*) FROM hocsinh WHERE Học_lực = 'Yếu' and Lớp = %s"),(lh.cls_list[i][0],))
        Yếu = mycursor4.fetchone()
        Yếu_ptrăm = round(Yếu[0]/Sĩ_số[0]*100,2)
        
        mycursor4.execute(("SELECT Học_lực,COUNT(*) FROM hocsinh Where Lớp= %s Group by Học_lực"),(lh.cls_list[i][0],))
        Chưa_xếp_loại = mycursor4.fetchall()

        
        print(Giỏi[0],Khá[0],Trung_bình[0],Yếu[0],Sĩ_số[0],Giỏi_ptrăm,Khá_ptrăm)
        print(type(Giỏi[0]),type(Giỏi_ptrăm))
        query = (lh.cls_list[i][0],Sĩ_số[0],Giỏi[0],Giỏi_ptrăm,Khá[0],Khá_ptrăm,Trung_bình[0],Trung_bình_ptrăm,Yếu[0],Yếu_ptrăm,Chưa_xếp_loại[-1][1])
        
        mycursor4.execute(("INSERT INTO `Xeploaihocluc`  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NULL)"),query)
        mydb.commit()

def Tự_động_tính_xếp_loại_hạnh_kiểm():
    mycursor4.execute("Delete from xeploaihanhkiem")   
    for i in range(len(lh.cls_list)):
        
        mycursor4.execute(("SELECT COUNT(*) FROM hocsinh WHERE Lớp = %s"),(lh.cls_list[i][0],))
        Sĩ_số = mycursor4.fetchone()
        Sĩ_số = list(Sĩ_số)
        
        mycursor4.execute(("SELECT COUNT(*) FROM hocsinh WHERE Hạnh_kiểm = 'Tốt' and Lớp = %s"),(lh.cls_list[i][0],))
        Giỏi = mycursor4.fetchone()   
        Giỏi_ptrăm = round(Giỏi[0]/Sĩ_số[0]*100,2)
        
        mycursor4.execute(("SELECT COUNT(*) FROM hocsinh WHERE Hạnh_kiểm = 'Khá' and Lớp = %s"),(lh.cls_list[i][0],))
        Khá = mycursor4.fetchone()
        Khá_ptrăm = round(Khá[0]/Sĩ_số[0]*100,2)
        
        mycursor4.execute(("SELECT COUNT(*) FROM hocsinh WHERE Hạnh_kiểm = 'Trung_bình' and Lớp = %s"),(lh.cls_list[i][0],))
        Trung_bình = mycursor4.fetchone()
        Trung_bình_ptrăm = round(Trung_bình[0]/Sĩ_số[0]*100,2)
        
        mycursor4.execute(("SELECT COUNT(*) FROM hocsinh WHERE Hạnh_kiểm = 'Yếu' and Lớp = %s"),(lh.cls_list[i][0],))
        Yếu = mycursor4.fetchone()
        Yếu_ptrăm = round(Yếu[0]/Sĩ_số[0]*100,2)
        
        mycursor4.execute(("SELECT Hạnh_kiểm,COUNT(*) FROM hocsinh Where Lớp= %s Group by Hạnh_kiểm"),(lh.cls_list[i][0],))
        Chưa_xếp_loại = mycursor4.fetchall()

        
        print(Giỏi[0],Khá[0],Trung_bình[0],Yếu[0],Sĩ_số[0],Giỏi_ptrăm,Khá_ptrăm)
        print(type(Giỏi[0]),type(Giỏi_ptrăm))
        query = (lh.cls_list[i][0],Sĩ_số[0],Giỏi[0],Giỏi_ptrăm,Khá[0],Khá_ptrăm,Trung_bình[0],Trung_bình_ptrăm,Yếu[0],Yếu_ptrăm,Chưa_xếp_loại[-1][1])
        
        mycursor4.execute(("INSERT INTO `Xeploaihanhkiem`  VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,NULL)"),query)
        mydb.commit()      
   