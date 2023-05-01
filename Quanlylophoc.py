import PySimpleGUI as sg
from Quanlyhocsinh import mydb
from openpyxl import Workbook
import os

cls_headings = ['Lớp','Mã_lớp','Sĩ số','Giáo_viên_chủ_nhiệm','Niên_khóa']
cls_list = []
stdmini_list = []
tkb_list = [] #Mỗi lần 1 lớp chứ ko phải show ra tất cả các lớp
mycursor0 = mydb.cursor()
mycursor0.execute('select * from lophoc')
classes = mycursor0.fetchall()
for i in classes:
    cls_list.append(list(i))
attitude_box = ['Tốt','Khá','Trung bình','Yếu']
cls_layout = [[sg.Text('          Danh sách lớp học',justification='center',font = 'Calibra 20')],
              [sg.Frame('Tên lớp',[[sg.InputCombo(['','6A','6B'],k='-CLS_CHOSEN-')]]),sg.Frame('Niên khóa',[[sg.InputCombo(['','2018-2022'],k='-YEARS_CHOSEN-')]]),
               sg.Button('Tìm kiếm',key='-FIND0-'),sg.Button('Refresh',k='-RF-')],
              [sg.Table(cls_list,
                        cls_headings,
                        background_color='LightBlue4',justification='center',
                        text_color='white',change_submits=True,
                        enable_click_events=True,
                        right_click_selects = True,
                        right_click_menu = ['menu',['Xuất ra danh sách học sinh','Thời khóa biểu']],
                        k='-CLSTABLE-'),sg.Column([[sg.Button('Nhập thêm lớp',key='-ADDCLS-',expand_x=True)],
                                                   [sg.Button('Sửa',expand_x=True,key='-FIX0-',disabled=True)],
                                                   [sg.Button('Xóa',expand_x=True,disabled=True,key= '-DEL0-')]]),
                sg.VSeparator(),
                sg.Table(values =stdmini_list,
                         headings=['Lớp','    Họ và tên    ','Ngày sinh','Học_lực','Hạnh_kiểm'],
                         background_color='LightBlue4',justification='center',
                         right_click_selects = True,
                         right_click_menu = ['hạnh kiểm',attitude_box],
                         text_color='white',change_submits=True,
                         visible = False,
                         k='-STDTABLEMINI-') ] ,
                
              [sg.Input(key = '-INFOR0-')],
              [sg.Exit(visible=False,k='-EXIT0-')]]

def Refresh(window):
    window['-CLS_CHOSEN-'].update('')
    window['-YEARS_CHOSEN-'].update('')
    cls_list.clear()
    mycursor0.execute('select * from lophoc')
    classes = mycursor0.fetchall()
    for i in classes:
        cls_list.append(list(i))
    window['-CLSTABLE-'].update(cls_list)    
    

def Tìm_kiếm(values,window):
    cls_list.clear()
    if values['-YEARS_CHOSEN-'] == '': mycursor0.execute(("select * from lophoc where Tên_lớp = %s"),(values['-CLS_CHOSEN-'],))
    elif values['-CLS_CHOSEN-'] == '': mycursor0.execute(("select * from lophoc where Niên_khóa = %s"),(values['-YEARS_CHOSEN-'],))
    else: mycursor0.execute(("select * from lophoc where Tên_lớp = %s and Niên_khóa = %s"),(values['-CLS_CHOSEN-'],values['-YEARS_CHOSEN-']))
    cls_searching_for = mycursor0.fetchall()
    print(cls_searching_for)
    for i in cls_searching_for:
        cls_list.append(list(i))
    window['-CLSTABLE-'].update(cls_list)   
     
def Xuất_ra_danh_sách_học_sinh(row,window):
    
    stdmini_list.clear()
    mycursor0.execute(("select Lớp,Họ_và_tên,Ngày_sinh,Học_lực,Hạnh_kiểm from hocsinh where Lớp = %s"),(cls_list[row-1][0],))
    stdmini = mycursor0.fetchall()
    for i in stdmini:
        stdmini_list.append(list(i))
    print(stdmini_list)    
    window['-STDTABLEMINI-'].update(stdmini_list,visible=True)

def Nhập_thêm_lớp(window):
    cls_list.clear()
    add_cls = sg.Window('Nhập thêm lớp',[[sg.T('Tên lớp mới:            '),sg.In(k='-NEWCLSNAME-')],
                                         [sg.T('Mã lớp:                    '),sg.In(k='-NEWCLS-')],
                                         [sg.T('Giáo viên Chủ nhiệm: '),sg.In(k='-NEWCLSTEACHER-')],
                                         [sg.T('Sĩ Số:                      '),sg.In(k='-NUMSTD-')],
                                         [sg.T('Niên khóa:                '),sg.In(k='-NEWCLSYEARS-')],
                                         [sg.OK()]
                                         ])
    while True:
        evt,val = add_cls.read()
        if evt == sg.WIN_CLOSED:
            break
        if evt == 'OK':
           if val['-NEWCLSNAME-'] == '' and val['-NEWCLS-'] == '' and val['-NUMSTD-'] == '' and val['-NEWCLSTEACHER-'] == '' and val['-NEWCLSYEARS-'] == '':
               break 
           mycursor0.execute(('insert into lophoc values(%s,%s,%s,%s,%s)'),(val['-NEWCLSNAME-'],val['-NEWCLS-'],val['-NUMSTD-'],val['-NEWCLSTEACHER-'],val['-NEWCLSYEARS-']))
           mydb.commit()
           sg.popup('Thêm lớp thành công')
           break 
    add_cls.close()
    mycursor0.execute('select * from lophoc')
    classes = mycursor0.fetchall()
    for i in classes:
        cls_list.append(list(i))
    window['-CLSTABLE-'].update(cls_list)
    
def Sửa_thông_tin_lớp(window,row,column,values):
    cls_list[row-1][column-1] = values['-INFOR0-']
    sg.popup('Chỉnh sửa thông tin thành công!')
    window['-CLSTABLE-'].update(cls_list)
    mycursor0.execute(("update lophoc set {} = %s where Mã_lớp = %s".format(cls_headings[column-1])),(values['-INFOR0-'],cls_list[row-1][1]))   
    mydb.commit()
    window['-FIX0-'].update(disabled=True)      
    
def Xóa_lớp(window,row):
    try:
        mycursor0.execute('delete from lophoc where Mã_lớp = %s',(cls_list[row-1][1],))
        mydb.commit()
        cls_list.remove(cls_list[row-1])
    except:
        print('error')    
    window['-STDTABLE-'].update(cls_list)
    sg.popup('Xóa thông tin thành công!') 
    window['-DEL0-'].update(disabled = True)    
    
    
def Nhập_hạnh_kiểm(row,window,event):
    stdmini_list[row-1][3] = event 
    window['-STDTABLEMINI-'].update(stdmini_list)
    mycursor0.execute(('update hocsinh set Hạnh_kiểm = %s where Họ_và_tên = %s'),(event,stdmini_list[row-1][1]))
    mydb.commit() 

#Click chuột phải để ra thời khóa biểu     
def Thời_khóa_biểu(row,window):
    tkb_list.clear()
    tkb_headings = ['Tiết','Thứ_2','Thứ_3','Thứ_4','Thứ_5','Thứ_6','Thứ_7']
    
    mycursor0.execute(('select * from thoikhoabieu where Lớp=%s'),(cls_list[row-1][0],))
    tkb = mycursor0.fetchall()
    for i in tkb:
        tkb_list.append(list(i[1:]))
    print(len(tkb_list))    
    if len(tkb_list) < 5:
        for i in range(len(tkb_list),5):
            t = i+1
            mycursor0.execute("insert into thoikhoabieu values (NULL,%s,'Hello','','','','','',%s)",(t,cls_list[row-1][0])) 
            
    mydb.commit()
    mycursor0.execute(('select * from thoikhoabieu where Lớp=%s'),(cls_list[row-1][0],))
    tkb1 = mycursor0.fetchall()
    
    for i in tkb1:
        tkb_list.append(list(i[1:]))     
    print(len(tkb_list)) 
    
    TKB_fixlayout = [[sg.T('Tiết'),sg.T('Thứ 2',s=(10,1)),sg.T('Thứ 3',s = (10,1)),sg.T('Thứ 4',s = (4,1)),sg.T('   Thứ 5',s = (9,1)),sg.T('Thứ 6',s = (7,1)),sg.T('Thứ 7',s = (7,1))],
                     [sg.T(' 1'),sg.In(tkb_list[0][1],s = (10,1),k='2-1'),sg.In(tkb_list[0][2],s = (10,1),k='3-1'),sg.In(tkb_list[0][3],s = (10,1),k='4-1'),sg.In(tkb_list[0][4],s = (10,1),k='5-1'),sg.In(tkb_list[0][5],s = (10,1),k='6-1'),sg.In(tkb_list[0][6],s = (10,1),k='7-1')],
                     [sg.T(' 2'),sg.In(tkb_list[1][1],s = (10,1),k='2-2'),sg.In(tkb_list[1][2],s = (10,1),k='3-2'),sg.In(tkb_list[1][3],s = (10,1),k='4-2'),sg.In(tkb_list[1][4],s = (10,1),k='5-2'),sg.In(tkb_list[1][5],s = (10,1),k='6-2'),sg.In(tkb_list[1][6],s = (10,1),k='7-2')],
                     [sg.T(' 3'),sg.In(tkb_list[2][1],s = (10,1),k='2-3'),sg.In(tkb_list[2][2],s = (10,1),k='3-3'),sg.In(tkb_list[2][3],s = (10,1),k='4-3'),sg.In(tkb_list[2][4],s = (10,1),k='5-3'),sg.In(tkb_list[2][5],s = (10,1),k='6-3'),sg.In(tkb_list[2][6],s = (10,1),k='7-3')],
                     [sg.T(' 4'),sg.In(tkb_list[3][1],s = (10,1),k='2-4'),sg.In(tkb_list[3][2],s = (10,1),k='3-4'),sg.In(tkb_list[3][3],s = (10,1),k='4-4'),sg.In(tkb_list[3][4],s = (10,1),k='5-4'),sg.In(tkb_list[3][5],s = (10,1),k='6-4'),sg.In(tkb_list[3][6],s = (10,1),k='7-4')],
                     [sg.T(' 5'),sg.In(tkb_list[4][1],s = (10,1),k='2-5'),sg.In(tkb_list[4][2],s = (10,1),k='3-5'),sg.In(tkb_list[4][3],s = (10,1),k='4-5'),sg.In(tkb_list[4][4],s = (10,1),k='5-5'),sg.In(tkb_list[4][5],s = (10,1),k='6-5'),sg.In(tkb_list[4][6],s = (10,1),k='7-5')]
                     ]
    tkb_window = sg.Window('Thời khóa biểu',[[TKB_fixlayout],
                                             [sg.Button('Chỉnh sửa\nTKB',k='-TKB-'),sg.Button('Xuất TKB ra Excel', k='-EXCEL-')]])
    evt,val = tkb_window.read()
    if evt == '-TKB-':
        # while True:
        #     event2,values2 = TKB_window.read()
        #     if event2 == sg.WIN_CLOSED: break 
            #if event2 == 'OK':
                for i in range(5):
                    tiết = i+1
                    for j in range(1,6):
                        thứ = j+1
                        tkb_list[i][j] = val['{}-{}'.format(thứ,j)]
                        mycursor0.execute('Update thoikhoabieu set Thứ_%s = %s where Tiết=%s and Lớp=%s',(thứ,val['{}-{}'.format(thứ,tiết)],tiết,tkb_list[0][7]))
                mydb.commit()
                #window['-CLSTABLEMINI-'].update(tkb_list)
                sg.popup('Thay đổi thông tin thành công')
                         
                tkb_window.close()
    elif evt == '-EXCEL-':
        Xuất_thời_khóa_biểu_ra_flie_Excel()     

def Xuất_thời_khóa_biểu_ra_flie_Excel():
    wb = Workbook()
    ws = wb.active              
    ws.title = "Thời khóa biểu"
    ws.append(['Tiết','Thứ 2','Thứ 3','Thứ 4','Thứ 5','Thứ 6','Thứ 7'])
    ws.append(['1',tkb_list[0][1],tkb_list[0][2],tkb_list[0][3],tkb_list[0][4],tkb_list[0][5],tkb_list[0][6]])
    ws.append(['2',tkb_list[1][1],tkb_list[1][2],tkb_list[1][3],tkb_list[1][4],tkb_list[1][5],tkb_list[1][6]])
    ws.append(['3',tkb_list[2][1],tkb_list[2][2],tkb_list[2][3],tkb_list[2][4],tkb_list[2][5],tkb_list[2][6]])
    ws.append(['4',tkb_list[3][1],tkb_list[3][2],tkb_list[3][3],tkb_list[3][4],tkb_list[3][5],tkb_list[3][6]])
    ws.append(['5',tkb_list[4][1],tkb_list[4][2],tkb_list[4][3],tkb_list[4][4],tkb_list[4][5],tkb_list[4][6]])
    wb.save('Thời khóa biểu lớp {}.xlsx'.format(tkb_list[0][7]))
    os.startfile('Thời khóa biểu lớp {}.xlsx'.format(tkb_list[0][7]))