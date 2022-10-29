import mysql.connector
from mysql.connector import Error
import datetime
import time

#*FUNCTIONS
# To display any command list as a a table
def f_display(l, sec=0):
    print()
    length0 = -1
    length1 = -1
    for x in range(len(l)):
        if len(str(l[x][0])) > length0:
            length0 = len(str(l[x][0]))
        if len(str(l[x][1])) > length1:
            length1 = len(str(l[x][1]))

    for x in range(len(l)):
        print('+{}++{}+'.format('-'*(length0+2), '-'*(length1+2)))
        print('| {:^{}} '.format(l[x][0], length0), end='|')
        print('| {:<{}} '.format(l[x][1], length1), end='|')
        print()
        time.sleep(sec)
    print('+{}++{}+'.format('-'*(length0+2), '-'*(length1+2)))


# to display the about window
def f_about():
    print('\n+-------+')
    print('| ABOUT |')
    print('+-------+\n')
    print('JC Registral is a tool created for managing data for the admission process of Junior College(JC) students.')
    print('\nDeveloped by:-\n')
    print('\tVarun Baisane    Roll No: 20')
    print('\tAnant Jaiswara   Roll No: 05')
    print('\tSarthak Dale     Roll No: 15')
    print('\n© Copyright 2022 | JC Registralᵀᴹ | All Rights Reserved.')
    time.sleep(1)
    f_panel()

# panel to control admission operations
def f_adm(acad_yr):
    f_display(xi_adm)
    cmd = input('\nEnter command:=> ')

    if not cmd.isnumeric():
        print('\nEnter valid command\n')
        f_adm(acad_yr)
    elif int(cmd) == 1:
        f_data_entry_adm(acad_yr)
    elif int(cmd) == 2:
        f_display_adm(acad_yr)
    elif int(cmd) == 3:
        f_update_adm(acad_yr)
    elif int(cmd) == 4:
        f_del_adm(acad_yr)
    elif int(cmd) == 5:
        f_dummy_data(acad_yr)
    elif int(cmd) == 6:
        f_panel()
    else:
        print('\nEnter valid command\n')
        f_adm(acad_yr)

# To create table
def f_create_table_adm():
    tb_name = "admregister"

    try:
        cur.execute(f'CREATE TABLE {tb_name} (AdmNo int(5) PRIMARY KEY,JoiningYear int(5), StudentName varchar(30), Mail varchar(30) UNIQUE, DoB date, BirthPlace varchar(100), MotherTongue varchar(20), MotherName varchar(30), FatherName varchar(30), Nationality varchar(30), Caste varchar(10), Address varchar(100), ParentOccupation varchar(30),  ParentOccupationCategory varchar(25), ParentPay int(11), ParentMobile varchar(20), ParentOfficeAddress varchar(100), ParentOfficeTelephone int(10), XLastAttended date, XMedium varchar(20), XBoard varchar(20), XPassYear YEAR, XRollNo int(15) UNIQUE, XEng int(3) DEFAULT 0, XMaths int(3) DEFAULT 0, XScience int(3) DEFAULT 0, XSocial int(3) DEFAULT 0, XIILang int(3) DEFAULT 0, XTotalMarks int(3) DEFAULT 0, XPercentage decimal(5,2) DEFAULT 0, Status varchar(5) DEFAULT "XI", Sub varchar(4))')
    except Error:
        # Table already existed
        pass

# To enter all required data
def f_data_entry_adm(acad_yr):
    print('\n+------------------+')
    print('| Personal Details |')
    print('+------------------+')

    stu_name = input("Enter Student's Full Name: ")
    stu_mail = input("Enter Student's Email ID: ")
    stu_dob = input("Enter Date of Birth(FORMAT: YYYY-MM-DD): ")
    stu_bplace = input("Enter Place of Birth: ")
    stu_motong =  input("Enter Mother Tongue: ")
    stu_moname =  input("Enter Mother's Name: ")
    stu_faname=  input("Enter Father's Name: ")
    stu_nat = input("Enter Nationality: ")
    stu_caste = input("Enter Student's Caste(SC/ST/OBC/Gen): ")
    stu_add = input("Enter Student's Address: ")

    print('\n+-----------------+')
    print('| Parents Details |')
    print('+-----------------+')

    pa_occ = input("Enter Parents' Occupation: ")
    pa_occcat = input("Enter Parents' Occupation Category(DAE/NON-DAE): ")
    pa_pay = int(input("Enter Parents' Annual Income: "))
    pa_mob = input("Enter Parents' Mobile Number: ")
    pa_oadd = input("Enter Parents' Office Address: ")
    pa_otel = int(input("Enter Parents' Office Telephone Number: "))

    print('\n+-----------------+')
    print('| Class X Details |')
    print('+-----------------+')

    x_lastatt = input("Enter School Last Attended Date(FORMAT: YYYY-MM-DD): ")
    x_med = input("Enter Medium Of Instruction: ")
    x_board = input("Enter Examination Board: ")
    x_passyr = int(input("Enter Passing Year(FORMAT: YYYY): "))
    x_rollno = int(input("Enter Board Roll Number: "))
    x_eng = int(input("Enter marks obtained in English: "))
    x_maths = int(input("Enter marks obtained in Maths: "))
    x_sci = int(input("Enter marks obtained in Science: "))
    x_ss = int(input("Enter marks obtained in Social Science: "))
    x_2lang = int(input("Enter marks obtained in Second Language: "))
    x_totmrks = int(input("Enter Total marks obtained: "))
    x_per = int(input("Enter 10th percentage: "))

    f_display(sub_c)
    sub_choice = input("Enter Sub Choice(1/2): ")
    if sub_choice == "2":
        sub_choice = "BIO"
    else:
        sub_choice = "CS"
    adm_no = 580

    adm_data = {
        'AdmNo' : adm_no,
        'JoiningYear': acad_yr[:4],
        'StudentName': stu_name,
        'Mail': stu_mail,
        'DoB': stu_dob,
        'BirthPlace': stu_bplace,
        'MotherTongue': stu_motong,
        'MotherName': stu_moname,
        'FatherName': stu_faname,
        'Nationality': stu_nat,
        'Caste': stu_caste,
        'Address': stu_add,
        'ParentOccupation': pa_occ,
        'ParentOccupationCategory': pa_occcat,
        'ParentPay': pa_pay,
        'ParentMobile': pa_mob,
        'ParentOfficeAddress': pa_oadd,
        'ParentOfficeTelephone': pa_otel,
        'XLastAttended': x_lastatt,
        'XMedium': x_med,
        'XBoard': x_board,
        'XPassYear': x_passyr,
        'XRollNo': x_rollno,
        'XEng': x_eng,
        'XMaths': x_maths,
        'XScience': x_sci,
        'XSocial': x_ss,
        'XIILang': x_2lang,
        'XTotalMarks': x_totmrks,
        'XPercentage': x_per,
        'Sub': sub_choice
    }

    adm_datal = []
    adm_datal.append(adm_data)
    f_data_upload_adm(adm_datal)

# To insert data to the table
def f_data_upload_adm(adm_datal):
    tb_name = "admregister"

    for adm_data in adm_datal:
        cur.execute(f'SELECT MAX(AdmNo) FROM {tb_name}')
        res = cur.fetchone()
        if res[0] == None:
            adm_data['AdmNo'] = 580
        else:
            adm_data['AdmNo'] = res[0]+1

        try:
            qry = 'INSERT INTO {} (AdmNo, JoiningYear, StudentName, Mail, DoB, BirthPlace, MotherTongue, MotherName, FatherName, Nationality, Caste, Address, ParentOccupation, ParentOccupationCategory, ParentPay, ParentMobile, ParentOfficeAddress, ParentOfficeTelephone, XLastAttended, XMedium, XBoard, XPassYear, XRollNo, XEng, XMaths, XScience, XSocial, XIILang, XTotalMarks, XPercentage, Sub) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s ,%s, %s, %s ,%s, %s, %s, %s, %s, %s, %s ,%s, %s, %s, %s, %s, %s, %s)'.format(tb_name)

            val = (
                adm_data['AdmNo'],
                adm_data['JoiningYear'],
                adm_data['StudentName'],
                adm_data['Mail'],
                adm_data['DoB'],
                adm_data['BirthPlace'],
                adm_data['MotherTongue'],
                adm_data['MotherName'],
                adm_data['FatherName'],
                adm_data['Nationality'],
                adm_data['Caste'],
                adm_data['Address'],
                adm_data['ParentOccupation'],
                adm_data['ParentOccupationCategory'],
                adm_data['ParentPay'],
                adm_data['ParentMobile'],
                adm_data['ParentOfficeAddress'],
                adm_data['ParentOfficeTelephone'],
                adm_data['XLastAttended'],
                adm_data['XMedium'],
                adm_data['XBoard'],
                adm_data['XPassYear'],
                adm_data['XRollNo'],
                adm_data['XEng'],
                adm_data['XMaths'],
                adm_data['XScience'],
                adm_data['XSocial'],
                adm_data['XIILang'],
                adm_data['XTotalMarks'],
                adm_data['XPercentage'],
                adm_data['Sub'])

            cur.execute(qry, val)
            mydb.commit()
            print('\n...{}, Welcome to AECS-3, Tarapur\n'.format(adm_data['StudentName']))

            cur.execute('SELECT MAX(AdmNo) FROM {}'.format(tb_name))
            res = cur.fetchone()
            print(f'\nYour Admission Number is: {res[0]}\n')
        except Error as e:
            print('\nPlease enter valid information.')
            print(e)
            print()
            f_data_entry_adm(adm_data['JoiningYear'])

    flag = True
    while flag:
        choice = input('Want to enter data for one more student? (Yes/No): ')
        if choice.lower() == "yes":
            f_data_entry_adm(adm_data['JoiningYear'])
            flag = False
        elif choice.lower() == "no":
            f_adm(adm_data['JoiningYear'])
            flag = False
        else:
            print('Enter valid command')
            flag = True

# To display sections of admission details
def f_display_section(l):
    print()
    for col in l:
        length = -1
        for x in range(2):
            if len(str(col[x])) > length:
                length = len(str(col[x]))
        print('+{}+'.format('-'*(length+2)), end='')
    print()
    for col in l:
        length = -1
        for x in range(2):
            if len(str(col[x])) > length:
                length = len(str(col[x]))
        print('| {:<{}}'.format(col[0], length), end=' |')
    print()
    for col in l:
        length = -1
        for x in range(2):
            if len(str(col[x])) > length:
                length = len(str(col[x]))
        print('+{}+'.format('-'*(length+2)), end='')
    print()
    for col in l:
        length = -1
        for x in range(2):
            if len(str(col[x])) > length:
                length = len(str(col[x]))
        print('| {:<{}}'.format(col[1], length), end=' |')
    print()
    for col in l:
        length = -1
        for x in range(2):
            if len(str(col[x])) > length:
                length = len(str(col[x]))
        print('+{}+'.format('-'*(length+2)), end='')
    print()

# To create admission data readable for f_display_section()
def f_display_adm(acad_yr):
    tb_name = "admregister"

    #display table of admno and name
    qry = f'SELECT AdmNo, StudentName FROM {tb_name} WHERE JoiningYear={acad_yr[:4]}'
    cur.execute(qry)
    res = cur.fetchall()

    if len(res) == 0:
        print(f'\nNo students found.')
        f_adm(acad_yr)
    else:
        res.insert(0, ['Admission Number', 'Name of the Student'])
        f_display(res, 0.025)
        print()

        #ask for admno and give full details
        admno = int(input('Enter Admission Number of the Student to Display Data: '))
        for x in range(1,len(res)):
            if admno == res[x][0]:
                qry = f'SELECT * FROM {tb_name} WHERE AdmNo = {admno}'
                cur.execute(qry)
                data = cur.fetchone()

                # create lol for display
                data_header = ['Admission Number','Joining Year', 'Student Name', 'Mail', 'Date of Birth', 'Birth Place', 'Mother Tongue', 'Mother Name', 'Father Name', 'Nationality', 'Caste', 'Address', 'Parent Occupation', 'Parent Occupation Category', 'Parent Pay', 'Parent Mobile', 'Parent Office Address', 'Parent Office Telephone', 'Last Attended', 'Medium', 'Board', 'Passing Year', 'RollNo', 'Eng', 'Maths', 'Science', 'Social', 'II Lang', 'Total', 'Percentage', 'Class', 'Sub']

                bigdata = []
                for i in range(len(data)):
                    l=[]
                    l.append(data_header[i])
                    l.append(data[i])
                    bigdata.append(l)

                # create date to display
                for i in range(len(bigdata)):
                    if type(bigdata[i][1]) == type(datetime.date(2005, 7, 2)):
                        bigdata[i][1] = str(bigdata[i][1])

                print('\n+------------------+')
                print('| Personal Details |')
                print('+------------------+')
                pers_data = bigdata[:12]
                f_display_section(pers_data)

                print('\n+-----------------+')
                print('| Parents Details |')
                print('+-----------------+')
                par_data = bigdata[:1] + bigdata[2:3] + bigdata[11:18]
                f_display_section(par_data)
                
                print('\n+-----------------+')
                print('| Class X Details |')
                print('+-----------------+')
                X_data = bigdata[:1] + bigdata[2:3] + bigdata[18:]
                f_display_section(X_data)

        admno_list = []
        for i in res:
            admno_list.append(i[0])
        if admno in admno_list:
            flag = True
        else:
            print("\nEnter valid Admission Number.")
            flag = False
            f_adm(acad_yr)

        while flag:
            choice = input('Want to Display data for one more student? (Yes/No): ')
            if choice.lower() == "yes":
                f_display_adm(acad_yr)
                flag = False
            elif choice.lower() == "no":
                f_adm(acad_yr)
                flag = False
            else:
                print('Enter valid command')
                flag = True

# SQL update statement 
def f_update_stm(col_name, col_val, adm_no):
    qry = 'UPDATE admregister SET {}=%s WHERE AdmNo=%s'.format(col_name)
    val = (col_val, adm_no)
    cur.execute(qry, val)
    mydb.commit()

# To update particular data 
def f_update_adm(acad_yr):
    qry = f'SELECT AdmNo, StudentName FROM admregister WHERE JoiningYear={acad_yr[:4]}'
    cur.execute(qry)
    res = cur.fetchall()

    if len(res) == 0:
        print(f'\nNo students found.')
        f_adm(acad_yr)
    else:
        res.insert(0, ['Admission Number', 'Name of the Student'])
        f_display(res)
        print()

        adm_no = input('\nEnter Admission Number to Update Data of the Student:=> ')

        f_display(adm_up, 0.025)

        cmd = input('\nEnter command to change Data:=> ')

        if not cmd.isnumeric():
            print('\nEnter valid command\n')
            f_update_adm()
        elif int(cmd) == 1:
            col_val = input('Enter new Joining Year:=> ')
            f_update_stm('JoiningYear', col_val, adm_no)
        elif int(cmd) == 2:
            col_val = input('Enter new Student Name:=> ')
            f_update_stm('StudentName', col_val, adm_no)
        elif int(cmd) == 3:
            col_val = input('Enter new Mail:=> ')
            f_update_stm('Mail', col_val, adm_no)
        elif int(cmd) == 4:
            col_val = input('Enter new Date of Birth(FORMAT: YYYY-MM-DD):=> ')
            f_update_stm('DoB', col_val, adm_no)
        elif int(cmd) == 5:
            col_val = input('Enter new Birth Place:=> ')
            f_update_stm('BirthPlace', col_val, adm_no)
        elif int(cmd) == 6:
            col_val = input('Enter new Mother Tongue:=> ')
            f_update_stm('MotherTongue', col_val, adm_no)
        elif int(cmd) == 7:
            col_val = input('Enter new Mother Name:=> ')
            f_update_stm('MotherName', col_val, adm_no)
        elif int(cmd) == 8:
            col_val = input('Enter new Father Name:=> ')
            f_update_stm('FatherName', col_val, adm_no)
        elif int(cmd) == 9:
            col_val = input('Enter new Nationality:=> ')
            f_update_stm('Nationality', col_val, adm_no)
        elif int(cmd) == 10:
            col_val = input('Enter new Caste(SC/ST/OBC/GEN):=> ')
            f_update_stm('Caste', col_val, adm_no)
        elif int(cmd) == 11:
            col_val = input('Enter new Address:=> ')
            f_update_stm('Address', col_val, adm_no)
        elif int(cmd) == 12:
            col_val = input('Enter new Parent Occupation:=> ')
            f_update_stm('ParentOccupation', col_val, adm_no)
        elif int(cmd) == 13:
            col_val = input('Enter new Parent Occupation Category(DAE/NON-DAE):=> ')
            f_update_stm('ParentOccupationCategory', col_val, adm_no)
        elif int(cmd) == 14:
            col_val = input('Enter new Parent Pay:=> ')
            f_update_stm('ParentPay', col_val, adm_no)
        elif int(cmd) == 15:
            col_val = input('Enter new Parent Mobile:=> ')
            f_update_stm('ParentMobile', col_val, adm_no)
        elif int(cmd) == 16:
            col_val = input('Enter new Parent Office Address:=> ')
            f_update_stm('ParentOfficeAddress', col_val, adm_no)
        elif int(cmd) == 17:
            col_val = input('Enter new Parent Office Telephone:=> ')
            f_update_stm('ParentOfficeTelephone', col_val, adm_no)
        elif int(cmd) == 18:
            col_val = input('Enter new X Last Attended Date(FORMAT: YYYY-MM-DD):=> ')
            f_update_stm('XLastAttended', col_val, adm_no)
        elif int(cmd) == 19:
            col_val = input('Enter new X Medium:=> ')
            f_update_stm('XMedium', col_val, adm_no)
        elif int(cmd) == 20:
            col_val = input('Enter new X Board:=> ')
            f_update_stm('XBoard', col_val, adm_no)
        elif int(cmd) == 21:
            col_val = input('Enter new X Passing Year(FORMAT: YYYY):=> ')
            f_update_stm('XPassYear', col_val, adm_no)
        elif int(cmd) == 22:
            col_val = input('Enter new X Roll No:=> ')
            f_update_stm('XRollNo', col_val, adm_no)
        elif int(cmd) == 23:
            col_val = input('Enter new X English Marks:=> ')
            f_update_stm('XEng', col_val, adm_no)
        elif int(cmd) == 24:
            col_val = input('Enter new X Maths Marks:=> ')
            f_update_stm('XMaths', col_val, adm_no)
        elif int(cmd) == 25:
            col_val = input('Enter new X Science Marks:=> ')
            f_update_stm('XScience', col_val, adm_no)
        elif int(cmd) == 26:
            col_val = input('Enter new X Social Marks:=> ')
            f_update_stm('XSocial', col_val, adm_no)
        elif int(cmd) == 27:
            col_val = input('Enter new X 2nd Language Marks:=> ')
            f_update_stm('XIILang', col_val, adm_no)
        elif int(cmd) == 28:
            col_val = input('Enter new X Total Marks:=> ')
            f_update_stm('XTotalMarks', col_val, adm_no)
        elif int(cmd) == 29:
            col_val = input('Enter new X Percentage:=> ')
            f_update_stm('XPercentage', col_val, adm_no)
        elif int(cmd) == 30:
            col_val = input('Enter new Subject Choice(CS/BIO):=> ')
            f_update_stm('Sub', col_val.upper(), adm_no)

    print('\nUpdated Succesfully')
    f_adm(acad_yr)

# To delete particular student data
def f_del_adm(acad_yr):
    qry = f'SELECT AdmNo, StudentName FROM admregister WHERE JoiningYear={acad_yr[:4]}'
    cur.execute(qry)
    res = cur.fetchall()

    if len(res) == 0:
        print(f'\nNo students found.')
        f_adm(acad_yr)
    else:
        res.insert(0, ['Admission Number', 'Name of the Student'])
        f_display(res)
        print()

        adm_no = input('\nEnter Admission Number to Delete Data of the Student:=> ')

        sql = "DELETE FROM admregister WHERE AdmNo = %s"
        val = (adm_no, )
        cur.execute(sql, val)
        mydb.commit()

        print('\nDeleted Succesfully')

        f_adm(acad_yr)

# To enter dummy data to check all functions
def f_dummy_data(acad_yr):

    adm_datal = []
    val = [(580, acad_yr[:4], 'Tanvi Kamble', f'tanvi{acad_yr[-2:]}@gmail.com', '2005-07-18', 'Mumbai', 'Marathi', 'Sadhana' ,'Prashil', 'Indian', 'SC', 'TAPS', 'Govt Service', 'DAE', 800000, '6539803893', 'Pasthal', '123456', f'{acad_yr[:4]}-02-19', 'English', 'CBSE', acad_yr[:4], f'923456{acad_yr[-2:]}', 95, 95, 95, 95, 95, 475, 95, 'CS'),(580, acad_yr[:4], 'Sarthak Dale',f'itsarthakhere{acad_yr[-2:]}@gmail.com', '2005-06-16', 'TAPS Hospital, Tarapur', 'Marathi', 'Bhavana' ,'Dilip', 'Indian', 'GEN', 'BARC', 'Govt Service', 'DAE', 800000, '6539803893', 'Pasthal', '123456', f'{acad_yr[:4]}-02-19', 'English', 'CBSE', acad_yr[:4], f'127456{acad_yr[-2:]}', 96, 85, 75, 98, 95, 465, 95, 'CS'),(580, acad_yr[:4], 'Aaditya Shirke', f'aadi{acad_yr[-2:]}@gmail.com', '2005-06-16', 'TAPS Hospital, Tarapur', 'Marathi', 'Seema' ,'Vindo', 'Indian', 'GEN', 'TAPS', 'Govt Service', 'DAE', 800000, '6539803893', 'Pasthal', '123456', f'{acad_yr[:4]}-02-19', 'English', 'CBSE', acad_yr[:4], f'193156{acad_yr[-2:]}', 95, 65, 75, 85, 15, 375, 85, 'BIO'),(580, acad_yr[:4], 'Suyash Kodge', f'sush{acad_yr[-2:]}@gmail.com', '2005-07-28', 'TAPS Hospital, Tarapur', 'Marathi', 'Abha' ,'Dhannaya', 'Indian', 'GEN', '3 and 4', 'Govt Service', 'DAE', 800000, '6539803893', 'Pasthal', '123456', f'{acad_yr[:4]}-02-19', 'English', 'CBSE', acad_yr[:4], f'567498{acad_yr[-2:]}', 85, 99, 93, 96, 85, 495, 98, 'CS'),(580, acad_yr[:4], 'Dhruv Patil', f'dhu{acad_yr[-2:]}@gmail.com', '2005-03-28', 'TAPS Hospital, Tarapur', 'Marathi', 'Arushi' ,'Hemant', 'Indian', 'OBC', 'TAPS', 'Govt Service', 'DAE', 800000, '6539803893', 'Pasthal', '123456', f'{acad_yr[:4]}-02-19', 'English', 'CBSE', acad_yr[:4], f'569408{acad_yr[-2:]}', 15, 35, 45, 15, 75, 205, 65, 'BIO'),(580, acad_yr[:4], 'Kuldeep', f'kulu{acad_yr[-2:]}@gmail.com', '2005-01-28', 'TAPS Hospital, Tarapur', 'Hindi', 'Sahana' ,'Harshal', 'Indian', 'SC', '3 and 4', 'Govt Service', 'DAE', 800000, '6539803893', 'Uttrakhand', '123456', f'{acad_yr[:4]}-02-19', 'English', 'CBSE', acad_yr[:4], f'610098{acad_yr[-2:]}', 95, 75, 95, 95, 15,135, 75, 'BIO'),(580, acad_yr[:4], 'Chetas Mohite', f'chets{acad_yr[-2:]}@gmail.com', '2005-07-28', 'TAPS Hospital, Tarapur', 'Marathi', 'Pushpa' ,'Narayan', 'Indian', 'GEN', 'Boisar', 'Govt Service', 'DAE', 800000, '6539803893', 'Pasthal', '123456', f'{acad_yr[:4]}-02-19', 'English', 'CBSE', acad_yr[:4], f'854498{acad_yr[-2:]}', 85, 99, 99, 25, 55, 479, 95, 'BIO'),(580, acad_yr[:4], 'Anirudhha Temak', f'ani{acad_yr[-2:]}@gmail.com', '2005-07-28', 'TAPS Hospital, Tarapur', 'Marathi', 'Rishi' ,'Vishwas', 'Indian', 'SC', 'BARC', 'Govt Service', 'DAE', 800000, '6539803893', 'Pasthal', '123456', f'{acad_yr[:4]}-02-19', 'English', 'CBSE', acad_yr[:4], f'567434{acad_yr[-2:]}', 15, 25, 55, 15, 75, 275, 99, 'CS'),(580, acad_yr[:4], 'Bhumit Humbhire', f'bhumi{acad_yr[-2:]}@gmail.com', '2005-07-28', 'TAPS Hospital, Tarapur', 'Marathi', 'Jhora' ,'Abdul', 'Indian', 'GEN', '3 and 4', 'Govt Service', 'DAE', 800000, '6539803893', 'Pasthal', '123456', f'{acad_yr[:4]}-02-19', 'English', 'CBSE', acad_yr[:4], f'067498{acad_yr[-2:]}', 95, 95, 95, 95, 65, 165, 95, 'CS'),(580, acad_yr[:4], 'Aarya Patil', f'aarya{acad_yr[-2:]}@gmail.com', '2005-03-24', 'TAPS Hospital, Tarapur', 'Marathi', 'Rupali' ,'Nilesh', 'Indian', 'OBC', 'BARC', 'Govt Service', 'DAE', 800000, '6539803893', 'Pasthal', '123456', f'{acad_yr[:4]}-02-19', 'English', 'CBSE', acad_yr[:4], f'570498{acad_yr[-2:]}', 85, 95, 99, 99, 99, 490, 97, 'BIO'),(580, acad_yr[:4], 'Athulya Anilkumar', f'ak{acad_yr[-2:]}@gmail.com', '2005-07-28', 'TAPS Hospital, Tarapur', 'Malayalam', 'Shini' ,'Anilkumar KC', 'Indian', 'GEN', 'BARC', 'Govt Service', 'DAE', 800000, '6539803893', 'Pasthal', '123456', f'{acad_yr[:4]}-02-19', 'English', 'CBSE', acad_yr[:4], f'967468{acad_yr[-2:]}', 99, 75, 15, 85, 95, 468, 95, 'CS'),(580, acad_yr[:4], 'Anant Jaiswara', f'anantjaiswara05{acad_yr[-2:]}@gmail.com', '2005-07-21', 'TAPS Hospital, Tarapur', 'Hindi', 'Shakuntala' ,'Durgesh', 'Indian', 'SC', 'TAPS', 'Govt Service', 'DAE', 800000, '6539803893', 'Pasthal', '123456', f'{acad_yr[:4]}-02-19', 'English', 'CBSE', acad_yr[:4], f'132465{acad_yr[-2:]}', 90, 90, 90, 90, 90, 450, 92, 'CS'),(580, acad_yr[:4], 'Amit Mastud', f'amitmastud07{acad_yr[-2:]}@gmail.com', '2005-07-17', 'TAPS Hospital, Tarapur', 'Marathi', 'Pinky' ,'Dattarya', 'Indian', 'SC', 'TAPS', 'Govt Service', 'DAE', 800000, '6539803893', 'Pasthal', '123456', f'{acad_yr[:4]}-02-19', 'English', 'CBSE', '2021', f'143265{acad_yr[-2:]}', 91, 91, 91, 91, 91, 455, 93, 'BIO'),(580, acad_yr[:4], 'Krish Dhodi', f'krishdhodi12{acad_yr[-2:]}@gmail.com', '2005-05-12', 'TAPS Hospital, Tarapur', 'Gujrati', 'Sita' ,'Sunil', 'Indian', 'St', 'BARC', 'Govt Service', 'DAE', 800000, '6539803893', 'Pasthal', '123456', f'{acad_yr[:4]}-02-19', 'English', 'CBSE', acad_yr[:4], f'123745{acad_yr[-2:]}', 92, 92, 92, 92, 92, 460, 94, 'BIO'),(580, acad_yr[:4], 'Kedar Lokhande', f'kdlokhande{acad_yr[-2:]}@gmail.com', '2005-11-18', 'TAPS Hospital, Tarapur', 'Marathi', 'Anita' ,'Damodar', 'Indian', 'OBC', 'BARC', 'Govt Service', 'DAE', 800000, '6539803893', 'Pasthal', '123456', f'{acad_yr[:4]}-02-19', 'English', 'CBSE', acad_yr[:4], f'152367{acad_yr[-2:]}', 93, 93, 93, 93, 93, 465, 94, 'BIO'),(580, acad_yr[:4], 'Harshal Gunjal', f'harshalop{acad_yr[-2:]}@gmail.com', '2005-08-30', 'TAPS Hospital, Tarapur', 'Marathi', 'Sunita' ,'Shashikant', 'Indian', 'GEN', 'TAPS', 'Govt Service', 'DAE', 800000, '6539803893', 'Pasthal', '123456', f'{acad_yr[:4]}-02-19', 'English', 'CBSE', acad_yr[:4], f'127643{acad_yr[-2:]}', 96, 96, 96, 96, 96, 480, 97, 'CS'),(580, acad_yr[:4], 'Mayank Sharma', f'mayanks{acad_yr[-2:]}@gmail.com', '2005-11-05', 'TAPS Hospital, Tarapur', 'Hindi', 'Soniya' ,'Mausam', 'Indian', 'GEN', 'TAPS', 'Govt Service', 'DAE', 800000, '6539803893', 'Pasthal', '123456', f'{acad_yr[:4]}-02-19', 'English', 'CBSE', acad_yr[:4], f'143765{acad_yr[-2:]}', 90, 90, 90, 90, 90, 450, 92, 'CS'),(580, acad_yr[:4], 'Shashank Mishra', f'smishra{acad_yr[-2:]}@gmail.com', '2005-05-25', 'TAPS Hospital, Tarapur', 'Hindi', 'Swati' ,'Rajesh', 'Indian', 'St', 'TAPS', 'Govt Service', 'DAE', 800000, '6539803893', 'Pasthal', '123456', f'{acad_yr[:4]}-02-19', 'English', 'CBSE', acad_yr[:4], f'134658{acad_yr[-2:]}', 91, 91, 91, 91, 91, 455, 93, 'CS'),(580, acad_yr[:4], 'Ruchita Waghmare', f'ruchi{acad_yr[-2:]}@gmail.com', '2005-12-25', 'TAPS Hospital, Tarapur', 'Marathi', 'Amita' ,'Nishant', 'Indian', 'OBC', '3&4', 'Govt Service', 'DAE', 800000, '6539803893', 'Pasthal', '123456', f'{acad_yr[:4]}-02-19', 'English', 'CBSE', acad_yr[:4], f'132645{acad_yr[-2:]}', 93, 95, 96, 95, 96, 475, 95, 'CS'),(580, acad_yr[:4], 'Avdhi Gujrati', f'avg{acad_yr[-2:]}@gmail.com', '2005-09-23', 'TAPS Hospital, Tarapur', 'Gujrati', 'Jagruti' ,'Akhilesh', 'Indian', 'GEN', '3&4', 'Govt Service', 'DAE', 800000, '6539803893', 'Pasthal', '123456', f'{acad_yr[:4]}-02-19', 'English', 'CBSE', acad_yr[:4], f'152438{acad_yr[-2:]}', 94, 95, 96, 95, 95, 475, 95, 'BIO')]

    for i in val:
        adm_data = {
            'AdmNo' : i[0],
            'JoiningYear': i[1],
            'StudentName': i[2],
            'Mail': i[3],
            'DoB': i[4],
            'BirthPlace': i[5],
            'MotherTongue': i[6],
            'MotherName': i[7],
            'FatherName': i[8],
            'Nationality': i[9],
            'Caste': i[10],
            'Address': i[11],
            'ParentOccupation': i[12],
            'ParentOccupationCategory': i[13],
            'ParentPay': i[14],
            'ParentMobile': i[15],
            'ParentOfficeAddress': i[16],
            'ParentOfficeTelephone': i[17],
            'XLastAttended': i[18],
            'XMedium': i[19],
            'XBoard': i[20],
            'XPassYear': i[21],
            'XRollNo': i[22],
            'XEng': i[23],
            'XMaths': i[24],
            'XScience': i[25],
            'XSocial': i[26],
            'XIILang': i[27],
            'XTotalMarks': i[28],
            'XPercentage': i[29],
            'Sub': i[30]
        }

        adm_datal.append(adm_data)
    f_data_upload_adm(adm_datal)

# Main home function to control all operations
def f_panel():
    f_display(home)
    cmd = input('\nEnter command:=> ')

    if not cmd.isnumeric():
        print('\nEnter valid command\n')
        f_panel()
    elif int(cmd) == 1:
        flag = True
        while flag:
            ayr = input('\nEnter academic year (FORMAT:20XX-XX):=> ')
            if len(str(ayr)) == 7:
                flag = False
                acad_yr = ayr[:4] + ayr[5:]
            else:
                print('\nEnter valid academic year.')
        f_create_table_adm()
        f_adm(acad_yr)
    elif int(cmd) == 2:
        f_about()
    elif int(cmd) == 3:
        print('\nThank You.')
        print('Visit Again.:)\n')
    else:
        print('\nEnter valid command\n')
        f_panel()

#* CODE BEGINS

db = 'csproj3'

#connecting mysql database
try:
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'mysqlpw',
        database = db
    )
except Error:
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'mysqlpw'
    )
    cur = mydb.cursor()
    cur.execute(f'CREATE DATABASE {db}')
    cur.execute(f'USE {db}')

cur = mydb.cursor()

# Starting Interface
print('\n+--------------+')
print('| JC REGISTRAL |')
print('+--------------+\n')
print('==========================================================================================')
print('\nWelcome to JC REGISTRAL\nA tool created for managing data for the admission process of Junior College(JC) students.\n')
print('==========================================================================================')

# command lists
home = [['Command', 'Function'],
    ['1','Check/Enter Admission Details for XI'],
    ['2','About'],
    ['3','Exit']]

xi_adm = [['Command', 'Function'],
    ['1','Enter Admission Details'],
    ['2','Display Admission Details'],
    ['3','Update Admission Details'],
    ['4','Delete Particular Student\'s Admission Details'],
    ['5','Enter Dummy Data'],
    ['6','Back to Home']]

sub_c = [['Command', 'Subjects'],
    ['1', 'Physics, Chemistry, Maths, English, Computer Science'],
    ['2', 'Physics, Chemistry, Maths, English, Biology']]

adm_up = [['Command', 'To Change'],
['1', 'Joining Year'],
['2', 'Student Name'],
['3', 'Mail'],
['4', 'Date of Birth'],
['5', 'Birth Place'],
['6', 'Mother Tongue'],
['7', 'Mother Name'],
['8', 'Father Name'],
['9', 'Nationality'],
['10', 'Caste'],
['11', 'Address'],
['12', 'Parent Occupation'],
['13', 'Parent Occupation Category'],
['14', 'Parent Pay'],
['15', 'Parent Mobile'],
['16', 'Parent Office Address'],
['17', 'Parent Office Telephone'],
['18', 'X Last Attended'],
['19', 'X Medium'],
['20', 'X Board'],
['21', 'X Pass Year'],
['22', 'X RollNo'],
['23', 'X Eng Marks'],
['24', 'X Maths Marks'],
['25', 'X Science Marks'],
['26', 'X Social Marks'],
['27', 'X II Lang Marks'],
['28', 'X Total Marks'],
['29', 'X Percentage'],
['30', 'Subject Choice']]

f_panel()
