from time import sleep, time
import PySimpleGUI as sg
import Quanlylophoc as lh
import Quanlyhocsinh as hs
import Quanlygiaovien as gv
import Quanlyketquahoctap as kq
import Baocaothongke as rp
import Phanconggiangday as pc 
import Quanlytaikhoangiaovien as tk
menu_board = sg.Column([[sg.Button('\t\n  Quản lý Lớp học  \n\t',use_ttk_buttons=True,pad=(10,10),k='-CLASS-',expand_x = True)],
                        [sg.Button('\t\n  Quản lý Học sinh  \n\t',use_ttk_buttons=True,pad=(10,10),k='-STUDENT-',expand_x = True)],
                        [sg.Button('\t\n  Quản lý Giáo viên  \n\t',use_ttk_buttons=True,pad=(10,10),k='-TEACHER-',expand_x = True)],
                        [sg.Button('\t\n  Quản lý kết quả\nhọc tập  \n\t',use_ttk_buttons=True,pad=(10,10),expand_x=True,k='-RESULT-')],
                        [sg.Button('\t\n  Báo cáo thống kê  \n\t',use_ttk_buttons=True,pad=(10,10),k='-REPORT-',expand_x = True)],
                        [sg.Button('\t\n Phân công giảng dạy \n\t',use_ttk_buttons=True,pad=(10,10),k='-STRAT-')]],background_color='purple')


tab = sg.TabGroup([[sg.T('\t\t            Nhấn vào tab để hiện bảng'),
                    sg.Tab('New Tab',[[]],k='-NEWTAB-'),sg.Tab('Tab 0',lh.cls_layout,key='-TAB0-',visible=False),
                    sg.Tab('Tab 1',hs.layout,title_color='yellow',key='-TAB1-',visible=False),
                    sg.Tab('Tab 2', gv.teacher_lo,key='-TAB2-',visible=False),
                    sg.Tab('Tab 3', kq.result_lo,key='-TAB3-',visible=False),
                    sg.Tab('Tab 4', rp.report_lo,key = '-TAB4-',visible=False),
                    sg.Tab('Tab 5', pc.strat_lo,key = '-TAB5-',visible=False)]],
                    expand_y=True,enable_events=True,key='-TABGR-',visible=False,focus_color='lightblue')
menu_left = [
    ['Tài khoản',['Đổi mật khẩu','Đăng xuất']]
]

layout1 = [[sg.Menu(menu_left)], 
           [sg.Column([[]],key='-GREETING-')],
            [menu_board,tab]
           ]



login_layout = [[sg.T('Tên đăng nhập:      '),sg.In(k='-ACCOUNT-')],
                [sg.T('Mật khẩu: \t'),sg.In(password_char='*',k='-PASSWORD-')],
                [sg.Text('',k='-MSG-',text_color='red')],
                [sg.Button('Đăng nhập',k='-LOGIN-',bind_return_key=True),sg.Button('Quên mật khẩu',k='-FORGETPASS-')]]
Log_in = sg.Window('Quản lý học sinh',login_layout)
window = sg.Window('Quản lý học sinh', layout1,location=(5,70),finalize=True)
window.hide()
login_status = False
no_tab = True
tab0 = False
tab1 = False
tab2 = False
tab3 = False
tab4 = False
tab5 = False

table0 = window['-CLSTABLE-']
table0.bind('<Button-1>', "Click")
table0.bind('<Button-3>', "Click")

table = window['-STDTABLE-']
table.bind('<Button-1>', "Click")

table1 = window['-TCTABLE-']
table1.bind('<Button-1>', "Click")

table2 = window['-RESTABLE-']
table2.bind('<Button-1>', "Click")

table3 = window['-STDTABLEMINI-']
table3.bind('<Button-3>', "Click")

table5 = window['-STRATTABLE-']
table5.bind('<Button-1>', "Click")

print(tk.Account_Password_list)
while True:
    while login_status == False:
        event0, values0 = Log_in.read()
        if event0 == sg.WIN_CLOSED:
            break
        if event0 == '-LOGIN-':
            for i in range(len(tk.Account_Password_list)):
                if (values0['-ACCOUNT-'] == tk.Account_Password_list[i][0]):
                    if values0['-PASSWORD-'] != tk.Account_Password_list[i][1]:    
                        Log_in['-MSG-'].update('Tài khoản hoặc mật khẩu của bạn chưa đúng,vui lòng thử lại')
                
                    else:
                        login_status = True
                        Log_in['-MSG-'].update('')
                        Log_in.hide()
                        window.un_hide()
                        window.extend_layout(window['-GREETING-'],[[sg.Text('Xin chào {}!'.format(tk.Name_list[i]),font='Calibra 15',relief='solid',border_width=1)]])
                
                elif values0['-PASSWORD-'] == tk.Account_Password_list[i][1]:
                    if (values0['-ACCOUNT-'] != tk.Account_Password_list[i][0]):
                        Log_in['-MSG-'].update('Tài khoản hoặc mật khẩu của bạn chưa đúng,vui lòng thử lại')
    
    event, values = window.read()
    
    if no_tab == True:    
        window['-TAB1-'].update(visible=False)
        window['-TAB2-'].update(visible=False)
        window['-TAB3-'].update(visible=False)
        #window['-TCTABLE-'].update(visible=True)
        
    if event == sg.WIN_CLOSED:
        break
    if event == 'Đăng xuất':
        login_status = False
        window.hide()
        sleep(2)
        Log_in.un_hide()
        
        

#Quản lý lớp học
    if event == '-CLASS-':
        no_tab = False
        tab0 = True
        window['-NEWTAB-'].update(visible=False)
        window['-TAB0-'].update(title='Quản lý lớp học',visible=True)
        window['-EXIT0-'].update(visible=True)
        window['-CLSTABLE-'].update(visible=True)
    
    if event == '-CLSTABLE-':
        pass
    elif event == '-CLSTABLE-Click' :
        window['-INFOR0-'].update(disabled= False)
        e0 = table0.user_bind_event
        region = table0.Widget.identify('region', e0.x, e0.y)
        window['-FIX0-'].update(disabled = False)
        window['-DEL0-'].update(disabled = False)
        if region == 'heading':
            continue
        elif region == 'cell':
            row0 = int(table0.Widget.identify_row(e0.y))
        elif region == 'separator':
            continue
        else:
            continue
        column0 = int(table0.Widget.identify_column(e0.x)[1:])
        #print(f"Table clicked at ({row}, {column})")
        print(lh.cls_list[row0-1][column0-1])
        window['-INFOR0-'].update(lh.cls_list[row0-1][column0-1])
    
    

    if event == 'Xuất ra danh sách học sinh':
        lh.Xuất_ra_danh_sách_học_sinh(row0,window)
    
    if event == 'Thời khóa biểu':
        lh.Thời_khóa_biểu(row0,window)
    
    if event == '-STDTABLEMINI-':
        pass
    elif event == '-STDTABLEMINI-Click' :
        e3 = table3.user_bind_event
        region3 = table3.Widget.identify('region', e3.x, e3.y)
        if region3 == 'heading':
            continue
        elif region3 == 'cell':
            row3 = int(table3.Widget.identify_row(e3.y))
        elif region3 == 'separator':
            continue
        else:
            continue
        column3 = int(table3.Widget.identify_column(e3.x)[1:])
        #print(f"Table clicked at ({row}, {column})")
        print(lh.stdmini_list[row3-1][column3-1])
    
    elif event in lh.attitude_box:
        lh.Nhập_hạnh_kiểm(row3,window,event)  
    
    elif event == '-RF-':
        lh.Refresh(window)
    
    elif event == '-ADDCLS-':
        lh.Nhập_thêm_lớp(window)
    
    elif event == '-FIND0-':
       lh.Tìm_kiếm(values,window)
    
    elif event == '-FIX0-':
       lh.Sửa_thông_tin_lớp(window,row0,column0,values)
       
    elif event == '-DEL0-':
        lh.Xóa_lớp(window,row0)

    print(type(values['-INFOR-']))
#Quản lý học sinh    
    if event == '-STUDENT-':
        no_tab = False
        tab1 = True
        window['-NEWTAB-'].update(visible=False)
        window['-TAB1-'].update(title='Quản lý học sinh',visible=True)
        window['-EXIT1-'].update(visible=True)
        window['-STDTABLE-'].update(visible=True)
    
    if event == '-STDTABLE-':
        pass
    elif event == '-STDTABLE-Click':
        window['-INFOR-'].update(disabled= False)
        e = table.user_bind_event
        region = table.Widget.identify('region', e.x, e.y)
        window['-FIX-'].update(disabled = False)
        window['-DEL-'].update(disabled = False)
        if region == 'heading':
            continue
        elif region == 'cell':
            row = int(table.Widget.identify_row(e.y))
        elif region == 'separator':
            continue
        else:
            continue
        column = int(table.Widget.identify_column(e.x)[1:])
        #print(f"Table clicked at ({row}, {column})")
        print(hs.student_list[row-1][column-1])
        window['-INFOR-'].update(hs.student_list[row-1][column-1])
    
    elif event == '-INSERT-':
        hs.Insert_student(window)    
            
    elif event == '-FIX-':
       hs.Fix_student(window,row,column,values)
    
    elif event == '-FIND-':
        hs.Find_student(window,values)
       
    elif event == '-DEL-':
        hs.Delete_student(window,row)     

#Quản lý giáo viên        
    elif event == '-TEACHER-':
        no_tab = False
        tab2 = True
        window['-NEWTAB-'].update(visible=False)
        window['-TAB2-'].update(title='Quản lý giáo viên',visible=True)
        window['-EXIT2-'].update(visible=True)
        window['-TCTABLE-'].update(visible=True)
    if event == '-TCTABLE-':
        pass
    elif event == '-TCTABLE-Click':
        window['-INFOR1-'].update(disabled= False)
        e1 = table1.user_bind_event
        region1 = table1.Widget.identify('region', e1.x, e1.y)
        window['-FIX1-'].update(disabled = False)
        window['-DEL1-'].update(disabled = False)
        if region1 == 'heading':
            continue
        elif region1 == 'cell':
            row1 = int(table1.Widget.identify_row(e1.y))
        elif region1 == 'separator':
            continue
        else:
            continue
        column1 = int(table1.Widget.identify_column(e1.x)[1:])
        #print(f"Table clicked at ({row}, {column})")
        print(gv.teacher_list[row1-1][column1-1])
        window['-INFOR1-'].update(gv.teacher_list[row1-1][column1-1])
    elif event == '-INSERT1-':
        gv.Insert_teacher(window)    
            
    elif event == '-FIX1-':
       gv.Fix_teacher(window,row1,column1,values)
    
    elif event == '-FIND1-':
        gv.Find_teacher(window,values)
       
    elif event == '-DEL1-':
        gv.Delete_teacher(window,row1)     
        
#Quản lý kết quả học tập    
    elif event == '-RESULT-':
        no_tab = False
        tab3 = True
        window['-NEWTAB-'].update(visible=False)
        window['-TAB3-'].update(title='Kết quả học tập',visible=True)
        window['-EXIT4-'].update(visible=True)
        window['-RESTABLE-'].update(kq.result_list,visible=True)
    if event == '-RESTABLE-':
        pass
    elif event == '-RESTABLE-Click':
        window['-INFOR2-'].update(disabled= False)
        e2 = table2.user_bind_event
        region2 = table2.Widget.identify('region', e2.x, e2.y)
        window['-FIXPOINT-'].update(disabled = False)
        #window['-DEL1-'].update(disabled = False)
        if region2 == 'heading':
            continue
        elif region2 == 'cell':
            row2 = int(table2.Widget.identify_row(e2.y))
        elif region2 == 'separator':
            continue
        else:
            continue
        column2 = int(table2.Widget.identify_column(e2.x)[1:])
        #print(f"Table clicked at ({row2}, {column2})")
        #print(kq.result_list)
        window['-INFOR2-'].update(kq.result_list[row2-1][column2-1])    
    elif event == '-SEARCH-':
        kq.Tra_điểm(window,values)
    elif event == '-INPOINT-':
        kq.Nhập_điểm(window,values)
    elif event == '-FIXPOINT-':
        kq.Sửa_điểm(window,row2,column2,values)
    elif event == '-CALC-':
        kq.Tính_TK(window,values)    

#Báo cáo thống kê
    elif event == '-REPORT-':
        no_tab = False
        tab4 = True
        window['-NEWTAB-'].update(visible=False)
        window['-TAB4-'].update(title='Báo cáo thống kê',visible=True)
        
        #window['-RESTABLE-'].update(kq.result_list,visible=True)
    elif event == '-STUDY-':
        window['-EXIT5-'].update(visible=True)
        rp.Thống_kê_xếp_loại_học_tập(window)
    elif event == '-ATTITUDE-':
        window['-EXIT5-'].update(visible=True)
        rp.Thống_kê_xếp_loại_hạnh_kiểm(window)    


#Phân công giảng dạy     
    elif event == '-STRAT-':
        no_tab = False   
        window['-NEWTAB-'].update(visible=False)
        window['-TAB5-'].update(title='Phân công giảng dạy',visible=True)
    
    if event == '-STRATTABLE-':
        pass
    elif event == '-STRATTABLE-Click' :
        window['-INFOR5-'].update(disabled= False)
        e5 = table5.user_bind_event
        region5 = table5.Widget.identify('region', e5.x, e5.y)
        window['-FIX5-'].update(disabled = False)
        window['-DEL5-'].update(disabled = False)
        if region5 == 'heading':
            continue
        elif region5 == 'cell':
            row5 = int(table5.Widget.identify_row(e5.y))
        elif region5 == 'separator':
            continue
        else:
            continue
        column5 = int(table5.Widget.identify_column(e5.x)[1:])
        #print(f"Table clicked at ({row}, {column})")
        print(pc.strat_list[row5-1][column5-1])
        if pc.strat_list[row5-1][column5-1] == None:
            window['-INFOR5-'].update('')
        else: window['-INFOR5-'].update(pc.strat_list[row5-1][column5-1])
    
    elif event == '-INSERT5-':
        pc.Nhập(window)
    
    elif event == '-FIX5-':
        pc.Sửa(window,values,row5,column5)    
    
    elif event == '-FIX5-':
        pc.Tìm_kiếm(window,values)
    
    elif event == '-FIX5-':
        pc.Xóa(window,row5)    


#Thoát
    elif event == '-EXIT0-':
        tab0 = False
        lh.stdmini_list.clear()
        window['-STDTABLEMINI-'].update(visible=False)
        if tab1 == True or tab2 == True or tab3 == True: window['-TAB0-'].update(visible=False)
        else: 
            window['-TAB0-'].update(visible=False)
            window['-TAB1-'].update(visible=False)
            window['-TAB2-'].update(visible=False)
            window['-TAB3-'].update(visible=False)
            window['-TAB4-'].update(visible=False)
            window['-TAB5-'].update(visible=False)
            window['-NEWTAB-'].update(visible=True)
            #no_tab = True    
        
    elif event == '-EXIT1-':
        tab1 = False
        if tab0 == True or tab2 == True or tab3 == True: window['-TAB1-'].update(visible=False)
        else: 
            window['-TAB0-'].update(visible=False)
            window['-TAB1-'].update(visible=False)
            window['-TAB2-'].update(visible=False)
            window['-TAB3-'].update(visible=False)
            window['-TAB4-'].update(visible=False)
            window['-TAB5-'].update(visible=False)
            window['-NEWTAB-'].update(visible=True)
            #no_tab = True    
    elif event == '-EXIT2-':
        tab2 = False  
        if tab0 == True or tab1 == True or tab3 == True: window['-TAB2-'].update(visible=False)
        else:
            window['-TAB0-'].update(visible=False)
            window['-TAB1-'].update(visible=False)
            window['-TAB2-'].update(visible=False)
            window['-TAB3-'].update(visible=False)
            window['-TAB4-'].update(visible=False)
            window['-TAB5-'].update(visible=False)
            window['-NEWTAB-'].update(visible=True)
            #no_tab = True
    elif event == '-EXIT4-':
        kq.Exit(window)
        tab3 = False
        if tab0 == True or tab1 == True or tab2 == True: window['-TAB3-'].update(visible=False)
        else:
            window['-TAB0-'].update(visible=False) 
            window['-TAB1-'].update(visible=False)
            window['-TAB2-'].update(visible=False)
            window['-TAB3-'].update(visible=False)
            window['-TAB4-'].update(visible=False)
            window['-TAB5-'].update(visible=False)
            window['-NEWTAB-'].update(visible=True) 
    elif event == '-EXIT5-':
        tab4 = False
        if tab0 == True or tab1 == True or tab2 == True or tab3 == True or tab5 == True: window['-TAB4-'].update(visible=False)
        else:
            window['-TAB0-'].update(visible=False) 
            window['-TAB1-'].update(visible=False)
            window['-TAB2-'].update(visible=False)
            window['-TAB3-'].update(visible=False)
            window['-TAB4-'].update(visible=False)
            window['-TAB5-'].update(visible=False)
            window['-NEWTAB-'].update(visible=True) 
    elif event == '-EXIT6-':      
        tab5 = False      
        if tab0 == True or tab1 == True or tab2 == True or tab3 == True or tab4 == True: window['-TAB4-'].update(visible=False)
        else:
            window['-TAB0-'].update(visible=False) 
            window['-TAB1-'].update(visible=False)
            window['-TAB2-'].update(visible=False)
            window['-TAB3-'].update(visible=False)
            window['-TAB4-'].update(visible=False)
            window['-TAB5-'].update(visible=False)
            window['-NEWTAB-'].update(visible=True)           
window.close()    