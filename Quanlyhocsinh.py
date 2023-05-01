from asyncio.windows_events import NULL
import PySimpleGUI as sg
import mysql.connector
import re

mydb = mysql.connector.connect(host='localhost',
                               user='root1',
                               passwd='1232001',
                               database='qlhtthcs')

mycursor = mydb.cursor()
mycursor.execute('select * from hocsinh')
student = mycursor.fetchall()

student_list = []
for i in student:
    student_list.append(list(i))
    # print(list(i))

sg.theme('LightBlue1')
std_headings = ['Họ_và_tên', 'Ngày_sinh', 'ID', 'Lớp',
                'Giới_tính', 'Nơi_sinh', 'Dân_tộc', 'Địa_chỉ', 'Ghi chú']
layout = [[sg.Text('\t\t\t   Danh sách học sinh', justification='center', font='Calibra 20')],
          [sg.Table(student_list,
                    std_headings,
                    num_rows=15,
                    background_color='LightBlue4', justification='center', text_color='white', change_submits=True, enable_click_events=True, key='-STDTABLE-'
                    ), sg.Column([[sg.Button('Nhập', key='-INSERT-', expand_x=True)], [sg.Button('Sửa', expand_x=True, key='-FIX-', disabled=True)], [sg.Button('Tìm kiếm', key='-FIND-')], [sg.Button('Xóa', expand_x=True, disabled=True, key='-DEL-')]])],
          [sg.Input(key='-INFOR-')],
          [sg.Exit(k='-EXIT1-')]]


def Insert_student(window):
    add_student = sg.Window('Nhập thông tin học sinh', layout=[[sg.T('*Họ và tên:', size=(15, 1)), sg.In(key='-FNAME-')],
                                                               [sg.T('Ngày:'), sg.InputCombo([i for i in range(1, 32)], k='-D-'),
                                                                sg.T('Tháng:'), sg.InputCombo(
                                                                   [i for i in range(1, 13)], k='-M-'),
                                                                sg.T('Năm:'), sg.InputCombo(
                                                                   [i for i in range(2000, 2022)], k='-Y-')
                                                                ],
                                                               [sg.T('ID: \t', size=(15, 1)), sg.In(
                                                                   k='-ID-', expand_x=True)],
                                                               [sg.T('Lớp: \t', size=(15, 1)), sg.In(
                                                                   k='-CLASS-', expand_x=True)],
                                                               [sg.T('Giới tính:', size=(15, 1)), sg.Checkbox(
                                                                   'Nam', k='-NAM-'), sg.Checkbox('Nữ', k='-NỮ-', expand_x=True)],
                                                               [sg.T('Nơi sinh:', size=(15, 1)), sg.In(
                                                                   k='-BORN-', expand_x=True)],
                                                               [sg.T('Dân tộc:', size=(15, 1)), sg.In(
                                                                   k='-KIND-', expand_x=True)],
                                                               [sg.T('Địa chỉ:', size=(15, 1)), sg.In(
                                                                   k='-ADDRESS-', expand_x=True)],
                                                               [sg.T('Ghi chú:', size=(15, 1)), sg.In(
                                                                   k='-NOTE-', expand_x=True)],
                                                               [sg.OK('Xác nhận', key='-OK-'), sg.Cancel(key='-CANCEL-')]])
    while True:
        choices, values2 = add_student.read()
        if choices == sg.WIN_CLOSED:
            break
        if choices == '-OK-':
            if values2['-FNAME-'] == '':
                sg.popup('Bạn chưa điền đầy đủ thông tin cần thiết')
            else:
                # Date of birth
                DoB = '{}/{}/{}'.format(values2['-D-'],
                                        values2['-M-'], values2['-Y-'])
                sex = ''
                if values2['-NAM-']:
                    sex = 'Nam'
                elif values2['-NỮ-']:
                    sex = 'Nữ'
                mycursor.execute(('insert into hocsinh values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'), (
                    values2['-FNAME-'], DoB, values2['-ID-'], values2['-CLASS-'], values2['-SEX-'], values2['-BORN-'], values2['-KIND-'], values2['-ADDRESS-'], values2['-NOTE-']))
                sg.popup('Đã thêm thông tin học sinh!')
                student_list.append([values2['-FNAME-'], DoB, values2['-ID-'], values2['-CLASS-'], values2['-SEX-'],
                                    values2['-BORN-'], values2['-KIND-'], values2['-ADDRESS-'], values2['-NOTE-']])
                window['-STDTABLE-'].update(student_list)
                mydb.commit()
                add_student.close()

        elif choices == '-CANCEL-':
            add_student.close()


def Fix_student(window, row, column, values):
    student_list[row-1][column-1] = values['-INFOR-']
    sg.popup('Chỉnh sửa thông tin thành công!')
    window['-STDTABLE-'].update(student_list)
    mycursor.execute(("update hocsinh set {} = %s where ID = %s".format(
        std_headings[column-1])), (values['-INFOR-'], student_list[row-1][2]))
    mydb.commit()
    window['-FIX-'].update(disabled=True)
    # window['-INFOR-'].update(disabled=True)


def Find_student(window, values):
    student_search = []
    if values['-INFOR-'] != '':
        for i in range(9):
            for j in range(len(student_list)):
                values['-INFOR-'] = str(values['-INFOR-'])
                text = str(student_list[j][i])
                if re.findall(values['-INFOR-'], text):
                    student_search.append(student_list[j])
                    window['-STDTABLE-'].update(student_search)

    elif values['-INFOR-'] == '':
        window['-STDTABLE-'].update(student_list)
    student_search.clear()


def Delete_student(window, row):
    # print(hs.student_list[row-1][2])
    try:
        mycursor.execute('delete from hocsinh where ID = %s',
                         (student_list[row-1][2],))
        mydb.commit()
        student_list.remove(student_list[row-1])
    except:
        print('error')
    window['-STDTABLE-'].update(student_list)
    sg.popup('Xóa thông tin thành công!')
    window['-DEL-'].update(disabled=True)
