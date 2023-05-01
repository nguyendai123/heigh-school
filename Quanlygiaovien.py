import PySimpleGUI as sg
from Quanlyhocsinh import mydb
import re
mycursor1 = mydb.cursor()

mycursor1.execute('select * from Giaovien')
teachers = mycursor1.fetchall()


teacher_list = []
for i in teachers:
    teacher_list.append(list(i))

teacher_headings = ['ID','Họ và tên','Ngày sinh','Số_điện_thoại','Chủ nhiệm','Giới tính','Chuyên môn','Trình độ','Chức vụ','Ghi chú']


teacher_lo = [[sg.Text('\t\t\t   Danh sách giáo viên',justification='center',font = 'Calibra 20')],
              [sg.Table(teacher_list,
                        teacher_headings,
                        background_color='LightBlue4',justification='center',
                        text_color='white',change_submits=True,
                        enable_click_events=True,
                        k='-TCTABLE-'),sg.Column([[sg.Button('Nhập',key='-INSERT1-',expand_x=True)],[sg.Button('Sửa',expand_x=True,key='-FIX1-',disabled=True)],[sg.Button('Tìm kiếm',key='-FIND1-')],[sg.Button('Xóa',expand_x=True,disabled=True,key= '-DEL1-')]])],
              [sg.Input(key = '-INFOR1-')],
              [sg.Exit(visible=False,k='-EXIT2-')]]




def Insert_teacher(window):
    add_teacher = sg.Window('Nhập thông tin giáo viên',layout=[[sg.T('*Họ và tên:', size =(15, 1)),sg.In(key='-FNAME1-')],
                                                                   [sg.T('Ngày:'),sg.InputCombo([i for i in range(1,32)],k='-D1-'),
                                                                    sg.T('Tháng:'),sg.InputCombo([i for i in range(1,13)],k='-M1-'),
                                                                    sg.T('Năm:'),sg.InputCombo([i for i in range(2000,2022)],k='-Y1-')
                                                                    ],
                                                                   [sg.T('ID:', size =(15, 1)),sg.In(k='-ID1-',expand_x=True)],
                                                                   [sg.T('Lớp:' , size =(15, 1)),sg.In(k='-CLASS-',expand_x=True)],
                                                                   [sg.T('Giới tính:', size =(15, 1)),sg.Checkbox('Nam',k='-NAM1-'),sg.Checkbox('Nữ',k='-NỮ1-',expand_x=True)],
                                                                   [sg.T('Chuyên môn:', size =(15, 1)),sg.In(k='-MAJOR-',expand_x=True)],
                                                                   [sg.T('Trình độ:', size =(15, 1)),sg.In(k='-LEVEL-',expand_x=True)],
                                                                   [sg.T('Số điện thoại:', size =(15, 1)),sg.In(k='-PHONE-',expand_x=True)],
                                                                   [sg.T('Chức vụ:', size =(15, 1)),sg.In(k='-JOB-',expand_x=True)],
                                                                   [sg.T('Ghi chú:', size =(15, 1)),sg.In(k='-NOTE1-',expand_x=True)],
                                                                   [sg.OK('Xác nhận',key='-OK1-'),sg.Cancel(key='-CANCEL1-')]])
    while True:
            choices, values2 = add_teacher.read()
            if choices == sg.WIN_CLOSED:
                break
            if choices == '-OK1-':
                if values2['-FNAME1-'] == '':
                    sg.popup('Bạn chưa điền đầy đủ thông tin cần thiết')
                else:
                    DoB = '{}/{}/{}'.format(values2['-D1-'],values2['-M1-'],values2['-Y1-']) #Date of birth
                    sex = ''
                    if values2['-NAM1-']: sex = 'Nam'
                    elif values2['-NỮ1-']:sex = 'Nữ'
                    
                    
                    mycursor1.execute(('insert into Giaovien values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'),
                                      (values2['-ID1-'],values2['-FNAME1-'],DoB,values2['-PHONE-'],values2['-CLASS-'],sex,values2['-MAJOR-'],values2['-LEVEL-'],values2['-JOB-'],values2['-NOTE-'])) 
                    sg.popup('Đã thêm thông tin giáo viên!')
                    teacher_list.append([values2['-ID1-'],values2['-FNAME1-'],DoB,values2['-PHONE-'],values2['-CLASS-'],sex,values2['-MAJOR-'],values2['-LEVEL-'],values2['-JOB-'],values2['-NOTE-']])
                    window['-TCTABLE-'].update(teacher_list)
                    mydb.commit()
                    add_teacher.close()
                    
                    
            elif choices == '-CANCEL1-':
                    add_teacher.close()     
    
def Fix_teacher(window,row,column,values):
    teacher_list[row-1][column-1] = values['-INFOR1-']
    sg.popup('Chỉnh sửa thông tin thành công!')
    window['-TCTABLE-'].update(teacher_list)
    mycursor1.execute(("update Giaovien set {} = %s where ID = %s".format(teacher_headings[column-1])),(values['-INFOR-'],teacher_list[row-1][0]))   
    mydb.commit()
    window['-FIX1-'].update(disabled=True)
    #window['-INFOR-'].update(disabled=True)

def Find_teacher(window,values):
    teacher_search = []
    if values['-INFOR1-'] != '':
        for i in range(9):
            for j in range(len(teacher_list)):
                text = str(teacher_list[j][i])
                if re.findall(values['-INFOR1-'],text):
                    teacher_search.append(teacher_list[j])
                    window['-TCTABLE-'].update(teacher_search)
    elif values['-INFOR1-'] == '': window['-TCTABLE-'].update(teacher_list)            
    
def Delete_teacher(window,row):
    #print(hs.result_list[row-1][2])
        try:
            mycursor1.execute('delete from Giaovien where ID = %s',(teacher_list[row-1][0],))
            mydb.commit()
            teacher_list.remove(teacher_list[row-1])
        except:
            print('error')    
        window['-TCTABLE-'].update(teacher_list)
        sg.popup('Xóa thông tin thành công!') 
        window['-DEL1-'].update(disabled = True)  


    
            