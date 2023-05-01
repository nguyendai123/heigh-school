from asyncio.windows_events import NULL
import PySimpleGUI as sg
import Quanlyhocsinh as hs
from Quanlyhocsinh import mydb

SỐ_MÔN_ĐIỀU_KIỆN = 3

result_headings = ['Môn_học','Mã_môn_học','Điểm_miệng','Điểm_15_phút','Điểm_1_tiết','Điểm_giữa_kỳ','Điểm_cuối_kỳ','Điểm_tổng_kết_học_kỳ']
result_list = []
mycursor2 = mydb.cursor()
tổng_kết_các_môn = 0
std_list_ID = []
for i in range(len(hs.student_list)):
    std_list_ID.append(hs.student_list[i][2])

result_lo = [ [sg.T('Mã học sinh: '),sg.InputCombo(std_list_ID,k='-ID_CHOSEN-'),sg.Button('Tra cứu',k='-SEARCH-')],
              [sg.Frame('Thông tin học sinh',[[sg.T('Họ và tên: ',k='-HVT-')],
                                              [sg.T('Lớp: ',k='-L-')],
                                              [sg.T('Học lực: ',k='-HL-')],
                                              [sg.T('Hạnh kiểm: ', k = '-ATT-')]
                                              ],
                        visible=True,k='-CV-')],
              [sg.Table(result_list,result_headings,k='-RESTABLE-',
                        background_color='LightBlue4',
                        justification='center',
                        text_color='white',
                        change_submits=True,
                        enable_click_events=True),sg.Column([[sg.Button('Nhập điểm',k='-INPOINT-')],
                                                             [sg.Button('Sửa điểm ',k='-FIXPOINT-',disabled=True)],
                                                             [sg.Button('\t\nTính điểm \ntổng kết\n\t',size=(7,3),pad=(5,5),disabled=True,k='-CALC-',expand_x=True)]])],
              [sg.T('Điểm tổng kết học kỳ của tất cả các môn: ',k='-AVGPOINT-')],
              [sg.Input(k='-INFOR2-')],
              [sg.Exit(visible=False,k='-EXIT4-')]]  
    
show_result_querry = ('Select Môn_học,Mã_môn,Điểm_miệng,Điểm_15_phút,Điểm_1_tiết,Điểm_giữa_kì,Điểm_cuối_kì,Điểm_tổng_kết_học_kỳ from bangdiemcanhan where ID = %s')

def Nhập_điểm(window,values):
    subject_list = ['Ngữ văn','Toán']
    add_point = sg.Window('Nhập điểm',layout=[[sg.InputCombo(std_list_ID,k='-ID_CHOSEN1-'),sg.Button('Kiểm tra',k='-CHECK-')],
                                                  [sg.T('Họ và Tên: ',k='-HVT1-')],
                                                  [sg.T('Lớp: ',k='-L1-')],
                                                  [sg.T('Môn: '),sg.InputCombo(subject_list,k='-SUBJ-')],
                                                  [sg.T('Điểm miệng: '),sg.In(k='-ORAL-')],
                                                  [sg.T('Điểm 15 phút: '),sg.In(k='-15M-')],
                                                  [sg.T('Điểm 1 tiết: '),sg.In(k='-45M-')],
                                                  [sg.T('Điểm giữa kỳ: '),sg.In(k='-MIDTERM-')],
                                                  [sg.T('Điểm cuối kỳ: '),sg.In(k='-FINALTERM-')],
                                                  [sg.OK('Xác nhận',k='-OK2-'),sg.Cancel(k='-CANCEL2-')]])
    while True:
            choices, values2 = add_point.read()
            if choices == sg.WIN_CLOSED:
                break
            if choices == '-OK2-':
                if values2['-ID_CHOSEN1-'] == '': 
                    sg.popup('Bạn chưa chọn học sinh cần nhập điểm')
                else:
                    mycursor2.execute(('insert into bangdiemcanhan values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'),
                                      (values2['-ID_CHOSEN1-'],values2['-SUBJ-'],'NV20221',values2['-ORAL-'],values2['-15M-'],values2['-45M-'],values2['-MIDTERM-'],values2['-FINALTERM-'],NULL)) 
                    mycursor2.execute(show_result_querry,(values['-ID_CHOSEN-'],))
                    result = mycursor2.fetchall()
                    result_list.clear()
                    for i in result:
                        result_list.append(list(i))
                    sg.popup('Đã nhập thêm điểm!')
                    #print(result_list)
                    #result_list.append([values2['-SUBJ-'],'NV20221',values2['-ORAL-'],values2['-15M-'],values2['-45M-'],values2['-MIDTERM-'],values2['-FINALTERM-'],''])
                    window['-RESTABLE-'].update(result_list)
                    mydb.commit()
                    add_point.close()
                    
                    
            elif choices == '-CHECK-':        
                    for j in range(len(hs.student_list)): 
                        if str(values2['-ID_CHOSEN1-']) == hs.student_list[j][2]:
                            print('Corect')
                            add_point['-HVT1-'].update('Họ và tên: {}'.format(hs.student_list[j][0])) 
                            add_point['-L1-'].update('Lớp: {}'.format(hs.student_list[j][3]))
                            add_point['-HL-'].update('Học lực: {}'.format(hs.student_list[j][10]))
                            add_point['-ATT-'].update('Hạnh kiểm: {}'.format(hs.student_list[j][11]))
            elif choices == '-CANCEL2-':
                    add_point.close()             
 

def Tra_điểm(window,values):
    result_list.clear()
    #window['-RESTABLE-'].update()
    ID_chosen = (values['-ID_CHOSEN-'],)
    mycursor2.execute(show_result_querry,ID_chosen)
    result = mycursor2.fetchall()
    for i in result:
            result_list.append(list(i)) 
            
    for j in range(len(hs.student_list)): 
        if str(values['-ID_CHOSEN-']) == hs.student_list[j][2]:
                print('Corect')
                mycursor2.execute('select * from hocsinh')
                student = mycursor2.fetchall()

                hs.student_list.clear()
                for i in student:
                    hs.student_list.append(list(i))
                window['-HVT-'].update('Họ và tên: {}'.format(hs.student_list[j][0])) 
                window['-L-'].update('Lớp: {}'.format(hs.student_list[j][3]))
                window['-HL-'].update('Học lực: {}'.format(hs.student_list[j][10]))
                window['-ATT-'].update('Hạnh kiểm: {}'.format(hs.student_list[j][11]))
                window['-AVGPOINT-'].update('Điểm tổng kết học kỳ của tất cả các môn: {}'.format(hs.student_list[j][11]))
                window['-RESTABLE-'].update(result_list,visible=True) 
    print(len(result_list))
    if len(result_list) < SỐ_MÔN_ĐIỀU_KIỆN: window['-CALC-'].update(disabled = True)
    else:
        window['-CALC-'].update(disabled = False)
        
    
def Sửa_điểm(window,row,column,values):
    result_list[row-1][column-1] = values['-INFOR2-'] 
    sg.popup('Chỉnh sửa thông tin thành công!')
    window['-RESTABLE-'].update(result_list)
    mycursor2.execute(("update bangdiemcanhan set {} = %s where ID = %s and Môn_học = %s".format(result_headings[column-1])),(values['-INFOR2-'],values['-ID_CHOSEN-'],result_list[row-1][0]))   
    mydb.commit()
    window['-FIXPOINT-'].update(disabled=True)      
    
def Tính_TK(window,values):  
        global tổng_kết_các_môn  
        for row in range(len(result_list)):
            tổng_kết = round((result_list[row-1][2]+result_list[row-1][3]+result_list[row-1][4]*2+result_list[row-1][5]*2+result_list[row-1][6]*3)/9,1)
            result_list[row-1][7] = tổng_kết
            tổng_kết_các_môn += tổng_kết
            mycursor2.execute(("update bangdiemcanhan set Điểm_tổng_kết_học_kỳ = %s where ID = %s and Môn_học = %s"),(tổng_kết,values['-ID_CHOSEN-'],result_list[row-1][0]))   
            mydb.commit()
        print(result_list)    
        window['-RESTABLE-'].update(result_list)
        avgpoint = round(tổng_kết_các_môn/SỐ_MÔN_ĐIỀU_KIỆN)
        window['-AVGPOINT-'].update('Điểm tổng kết học kỳ của tất cả các môn: {}'.format(avgpoint))
        if avgpoint >= 8:
            mycursor2.execute(("update hocsinh set Học_lực = %s where ID = %s"),('Giỏi',values['-ID_CHOSEN-']))   
            mycursor2.execute(("update hocsinh set Tổng_kết_các_môn = %s where ID = %s"),(avgpoint,values['-ID_CHOSEN-']))
            mydb.commit()
            window['-HL-'].update('Học lực: Giỏi')
        
        elif avgpoint <= 6.5 and avgpoint < 8:
            mycursor2.execute(("update hocsinh set Học_lực = %s where ID = %s"),('Khá',values['-ID_CHOSEN-']))   
            mycursor2.execute(("update hocsinh set Tổng_kết_các_môn = %s where ID = %s"),(avgpoint,values['-ID_CHOSEN-']))
            mydb.commit()
            window['-HL-'].update('Học lực: Khá')    
        
        elif avgpoint <= 5 and avgpoint < 6.5:
            mycursor2.execute(("update hocsinh set Học_lực = %s where ID = %s"),('Trung_bình',values['-ID_CHOSEN-']))   
            mycursor2.execute(("update hocsinh set Tổng_kết_các_môn = %s where ID = %s"),(avgpoint,values['-ID_CHOSEN-']))
            mydb.commit()
            window['-HL-'].update('Học lực: Trung bình') 
        elif avgpoint < 5:
            mycursor2.execute(("update hocsinh set Học_lực = %s where ID = %s"),('Yếu',values['-ID_CHOSEN-']))   
            mycursor2.execute(("update hocsinh set Tổng_kết_các_môn = %s where ID = %s"),(avgpoint,values['-ID_CHOSEN-']))
            mydb.commit()
            window['-HL-'].update('Học lực: Yếu')     
                
    #window['-CALC-'].update(disabled = True)    


def Exit(window):
        result_list.clear()
        window['-HVT-'].update('Họ và tên: ')
        window['-L-'].update('Lớp: ')
        window['-HL-'].update('Học lực: ')
        window['-HL-'].update('Hạnh kiểm: ')
        window['-AVGPOINT-'].update('Điểm tổng kết học kỳ của tất cả các môn: ')
        window['-ID_CHOSEN-'].update('')                                    