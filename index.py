# Academic Year
#     XI
#         Admission(genral details)
#         Fees Details
#         Report
#     XII
#         Admission(genral details)
#         Fees Details
#         Report
#         Ranks List
#         TC
# About

#*FUNCTIONS

import mysql.connector
from mysql.connector import Error

# To display any command list as a a table
def f_display(l):
    print()
    length =-1
    for x in range(len(l)):
        for y in range(len(l[x])):
            if len(str(l[x][y])) > length:
                length = len(str(l[x][y]))

    for x in range(len(l)):
        print('+{}++{}+'.format('-'*9, '-'*(length+2)))
        print('| {:^{}} '.format(l[x][0], 7), end='|')
        print('| {:<{}} '.format(l[x][1], length), end='|')
        print()
    print('+{}++{}+'.format('-'*9, '-'*(length+2)))

# to display the about window
def f_about():
    print('About')
    #$about tkinter
    f_panel()

# For working with XI data
def f_xi():
    print('+----+')
    print('| XI |')
    print('+----+')

    acad_yr = input('\nEnter academic year (FORMAT:20XXXX):=> ')

    f_display(xi_home)

    cmd = input('\nEnter command:=> ')

    if not cmd.isnumeric():
        print('\nEnter valid command\n')
        f_xi()
    elif int(cmd) == 1:
        f_adm(acad_yr)
    elif int(cmd) == 2:
        print('fees')
        #$checkout
        #!No update
    elif int(cmd) == 3:
        f_rc_xi(acad_yr)
        #! No update
    elif int(cmd) == 4:
        f_panel()
    else:
        print('\nEnter valid command\n')
        f_xi()

def f_adm(acad_yr):
    f_display(xi_adm)

    cmd = input('\nEnter command:=> ')

    if not cmd.isnumeric():
        print('\nEnter valid command\n')
        f_adm()
    elif int(cmd) == 1:
        f_enter_adm(acad_yr)
    elif int(cmd) == 2:
        print('display')
        #$tkinter or main only for one person
    elif int(cmd) == 3:
        print('update')
        #$updating tkinter
    elif int(cmd) == 4:
        f_panel()
    else:
        print('\nEnter valid command\n')
        f_adm()

def f_enter_adm(acad_yr):

    tb_name = f"adm{acad_yr}"

    try:
        print('Creating Table...')
        cur.execute(f'CREATE TABLE {tb_name} (AdmNo int(5) PRIMARY KEY AUTO_INCREMENT, StudentName varchar(25), Mail varchar(25) UNIQUE, DoB date, BirthPlace varchar(25), MotherTongue varchar(20), MotherName varchar(25), FatherName varchar(25), Nationality varchar(25), Caste varchar(5), Address varchar(50), ParentOccupation varchar(25),  ParentOccupationCategory varchar(25), ParentPay int(11), ParentMobile INTEGER, ParentOfficeAddress varchar(50), ParentOfficeTelephone int(10), XLastAttended date, XMedium varchar(10), XBoard varchar(20), XPassYear YEAR, XRollNo int(15), XEng int(3), XMaths int(3), XScience int(3), XSocial int(3), XIILang int(3), XTotalMarks int(3), XPercentage decimal(5,2), Class varchar(3) DEFAULT "XI", Sub varchar(4))')
        print(f'...Table {tb_name} Created')

        cur.execute(f"ALTER TABLE {tb_name} AUTO_INCREMENT=580")
        print('...Table Altered')
    
    except Error:
        print('...Table not Created...')
        cur.execute("SHOW TABLES")
        for x in cur:
            # print(x)
            # print(x[0])
            # print(tb_name)
            # print()
            if x[0] == tb_name:
                print('...Table already existed')

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
    stu_caste = input("Enter Students Caste(SC/ST/OBC/Gen): ")
    stu_add = input("Enter Students Address: ")
    

    print('\n+-----------------+')
    print('| Parents Details |')
    print('+-----------------+')
    
    pa_occ = input("Enter Parent's Occupation: ")
    pa_occcat = input("Enter Parent's Occupation Category(DAE/NON-DAE): ")
    pa_pay = int(input("Enter Annual Income: "))
    pa_mob = int(input("Enter Parent's Mobile Number: "))
    pa_oadd = input("Enter Office Address: ")
    pa_otel = int(input("Enter Office Telephone Number: "))
    


    print('\n+----------------+')
    print('| Class X Details |')
    print('+-----------------+')
    
    x_lastatt = input("Enter School Last Attended(FORMAT: YYYY-MM-DD): ")
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
        sub_choice = "Bio"
    else:
        sub_choice = "CS"

    # try:
    # cur.execute(f'''INSERT INTO {tb_name} (StudentName, Mail, DoB, BirthPlace, MotherTongue, MotherName, FatherName, Nationality, Caste, Address, ParentOccupation, ParentPay, ParentMobile, ParentOfficeAddress, ParentOfficeTelephone, XLastAttended, XMedium, XBoard, XPassYear, XRollNo, XEng, XMaths, XScience, XSocial, XIILang, XTotalMarks, XPercentage, Sub) VALUES ({stu_name}, {stu_mail}, {stu_dob}, {stu_bplace}, {stu_motong}, {stu_moname},{stu_faname}, {stu_nat}, {stu_caste}, {stu_add}, {pa_occ}, {pa_pay}, {pa_mob}, {pa_oadd}, {pa_otel}, {x_lastatt}, {x_med}, {x_board}, {x_passyr}, {x_rollno}, {x_eng}, {x_maths},{x_sci}, {x_ss}, {x_2lang}, {x_totmrks}, {x_per}, {sub_choice})''')

    qry = 'INSERT INTO {} (StudentName, Mail, DoB, BirthPlace, MotherTongue, MotherName, FatherName, Nationality, Caste, Address, ParentOccupation, ParentOccupationCategory, ParentPay, ParentMobile, ParentOfficeAddress, ParentOfficeTelephone, XLastAttended, XMedium, XBoard, XPassYear, XRollNo, XEng, XMaths, XScience, XSocial, XIILang, XTotalMarks, XPercentage, Sub) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s ,%s, %s, %s ,%s, %s, %s, %s, %s, %s, %s ,%s, %s, %s, %s, %s, %s)'.format(tb_name)

    val = (stu_name, stu_mail, stu_dob, stu_bplace, stu_motong, stu_moname,stu_faname, stu_nat, stu_caste, stu_add, pa_occ,pa_occcat, pa_pay, pa_mob, pa_oadd, pa_otel, x_lastatt, x_med, x_board, x_passyr, x_rollno, x_eng, x_maths,x_sci, x_ss, x_2lang, x_totmrks, x_per, sub_choice)

    cur.execute(qry, val)#29
    mydb.commit()
    print(f'\n...Welcome, {stu_name} to AECS-3, Tarapur\n')

    qry = 'SELECT MAX(AdmNo) FROM {}'.format(tb_name)
    cur.execute(qry)
    res = cur.fetchone()
    print(f'\nYour Admission Number is: {res}\n')


    choice = input('Want to enter data for one more student? (Yes/No): ')
    if choice.lower() == "yes":
        f_enter_adm(acad_yr)
    elif choice.lower() == "no":
        f_adm(acad_yr)
    else:
        f_adm(acad_yr)

    # except Error:
    #     print('table error')
    #     cur.execute("SHOW TABLES")
    #     for x in cur:
    #         print(x)
    #         print()
    #         if x[0] == f'adm{acad_yr}':
    #             cur.execute(f'''INSERT INTO {tb_name} (StudentName, Mail, DoB, BirthPlace, MotherTongue, MotherName, MotherName, FatherName, Nationaity, Caste, Address, ParentOccupation, ParentPay, ParentMobile, ParentOfficeAddress, ParentOfficeTelephone, XLastAttended, XMedium, XBoard, XPassYear, XRollNo, XEng, XMaths, XScience, XSocial, XIILang, XTotalMarks, XPercentage, Sub) VALUES ({stu_name, stu_mail,stu_dob,stu_bplace,stu_motong,stu_moname,stu_faname,stu_nat,stu_caste,stu_add,pa_occ,pa_pay,pa_mob,pa_oadd,pa_otel,x_lastatt,x_med,x_board,x_passyr,x_rollno,x_eng,x_maths,x_sci,x_ss,x_2lang,x_totmrks,x_per,sub_choice})''')
    #             choice = input('Want to enter data for one more student? (Yes/No): ')
    #             if choice.lower() == "yes":
    #                 f_enter_adm(acad_yr)
    #             elif choice.lower() == "no":
    #                 pass
    #             else:
    #                 pass

def f_rc_xi(acad_yr):

    tb_name = f'rc{acad_yr}'

    # try:
    #     print('Creating Table...')
    #     cur.execute(f'CREATE TABLE {tb_name} (AdmNo int(5) PRIMARY KEY AUTO_INCREMENT, )')
    #     print(f'...Table {tb_name} Created')

    #     # cur.execute(f"ALTER TABLE {tb_name} AUTO_INCREMENT=580")
    #     # print('...Table Altered')
    
    # except Error:
    #     print('...Table not Created...')
    #     cur.execute("SHOW TABLES")
    #     for x in cur:
    #         # print(x)
    #         # print(x[0])
    #         # print(tb_name)
    #         # print()
    #         if x[0] == tb_name:
    #             print('...Table already existed')

    adm_no = input()
    xi_rollno = int(input("Enter Roll Number: "))
    xi_tt1eng = int(input("Enter English marks: "))
    xi_tt1math = int(input("Enter Mathematics marks: "))
    xi_tt1chem = int(input("Enter Chemistry marks: "))
    xi_tt1phy = int(input("Enter Physics marks: "))
    xi_tt1cs = int(input("Enter Computer Science marks: "))
    xi_pt1eng = int(input("Enter English marks: "))
    xi_pt1math = int(input("Enter Mathematics marks: "))
    xi_pt1chem = int(input("Enter Chemistry marks: "))
    xi_pt1phy = int(input("Enter Physics marks: "))
    xi_pt1cs = int(input("Enter Computer Science marks: "))
    
    xi_tt2eng = int(input("Enter English marks: "))
    xi_tt2math = int(input("Enter Mathematics marks: "))
    xi_tt2chem = int(input("Enter Chemistry marks: "))
    xi_tt2phy = int(input("Enter Physics marks: "))
    xi_tt2cs = int(input("Enter Computer Science marks: "))
    xi_pt2eng = int(input("Enter English marks: "))
    xi_pt2math = int(input("Enter Mathematics marks: "))
    xi_pt2chem = int(input("Enter Chemistry marks: "))
    xi_pt2phy = int(input("Enter Physics marks: "))
    xi_pt2cs = int(input("Enter Computer Science marks: "))
    
    xi_toeng = int(input("Enter English marks: "))
    xi_tomath = int(input("Enter Mathematics marks: "))
    xi_tochem = int(input("Enter Chemistry marks: "))
    xi_tophy = int(input("Enter Physics marks: "))
    xi_tocs = int(input("Enter Computer Science marks: "))
    
    xi_totalmarks = int(input("Enter Total marks obtained: "))
    xi_perc = int(input("Enter Percentage: "))

    xi_we = input("Enter work experience: ")
    xi_gs = input("Enter grade for genral studies: ")
    xi_hpe = input("Enter grade for health and physical eduaction: ")
    xi_wd = int(input("Enter total working days: "))
    xi_pd = int(input("Enter total present days: "))
    xi_tr = input("Enter teachers remark: ")
    xi_res = input("Enter result: ")
    xi_doi = int(input("Enter Date Of Issue: "))
    
    #$ tkinter

def xii():
    f_display(xii_home)
    #$fees same 
    #$rc same proceess
    #$rank list only display
    #$TC
    

def f_panel():
    f_display(home)

    cmd = input('\nEnter command:=> ')

    if not cmd.isnumeric():
        print('\nEnter valid command\n')
        f_panel()
    elif int(cmd) == 1:
        f_xi()
    elif int(cmd) == 2:
        xii()
    elif int(cmd) == 3:
        f_about()
    elif int(cmd) == 4:
        print('\nThank You.')
        print('Visit Again.:)\n')
    else:
        print('\nEnter valid command\n')
        f_panel()

#* CODE BEGINS

#connecting mysql database
try:
    print('\nConnecting Database...\n')
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'mysqlpw',
        database = 'csproj'
    )
    print('\n...Database Connected\n')
except Error:
    print('\n...No database found\n')
    mydb = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = 'mysqlpw'
    )
    cur = mydb.cursor()
    cur.execute('CREATE DATABASE csproj')
    print('\n...Database Created\n')

cur = mydb.cursor()

# Starting Interface

print('\n+--------------+')
print('| JC REGISTRAL |')
print('+--------------+')

# command lists
home = [['Command', 'Function'],
    ['1','To Check/Enter data for Class XI'],
    ['2','To Check/Enter data for Class XII'],
    ['3','About'],
    ['4','Exit']]

xi_home = [['Command', 'Function'],
    ['1','Check/Enter Admission Details'],
    ['2','Display Fees Details'],
    ['3','Generate Report Card'],
    ['4','Back to Home']]

xi_adm = [['Command', 'Function'],
    ['1','Enter Admission Details'],
    ['2','Display Admission Details'],
    ['3','Update Admission Details'],
    ['4','Back to Home']]

xii_home = [['Command', 'Function'],
    ['1','Check/Enter Fees Details'],
    ['2','Generate Report Card'],
    ['3','Check Rank List'],
    ['4','Check Transfer Certificate'],
    ['5','Back to Home']]

sub_c = [['Command', 'Subjects'],
    ['1', 'Physics, Chemistry, Maths, English, Computer Science'],
    ['2', 'Physics, Chemistry, Maths, English, Biology']]

print('\n...Running the panel\n')
f_panel()
