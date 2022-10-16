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
import datetime

# To display any command list as a a table
def f_display(l):
    # print()
    # length =-1
    # for x in range(len(l)):
    #     for y in range(len(l[x])):
    #         if len(str(l[x][y])) > length:
    #             length = len(str(l[x][y]))

    # for x in range(len(l)):
    #     print('+{}++{}+'.format('-'*9, '-'*(length+2)))
    #     print('| {:^{}} '.format(l[x][0], 7), end='|')
    #     print('| {:<{}} '.format(l[x][1], length), end='|')
    #     print()
    # print('+{}++{}+'.format('-'*9, '-'*(length+2)))
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
        print('| {:<{}} '.format(l[x][0], length0), end='|')
        print('| {:<{}} '.format(l[x][1], length1), end='|')
        print()
    print('+{}++{}+'.format('-'*(length0+2), '-'*(length1+2)))


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

    flag = True
    while flag:
        ayr = input('\nEnter academic year (FORMAT:20XX-XX):=> ')
        if len(str(ayr)) == 7:
            flag = False
            acad_yr = ayr[:4] + ayr[5:]
        else:
            print('\nEnter valid academic year.')

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
        f_display_adm(acad_yr)
    elif int(cmd) == 3:
        f_update_adm(acad_yr)
    elif int(cmd) == 4:
        print()#$
    elif int(cmd) == 5:
        f_panel()
    else:
        print('\nEnter valid command\n')
        f_adm()

def f_enter_adm(acad_yr):

    tb_name = f"adm{acad_yr}"

    try:
        print('Creating Table...')
        cur.execute(f'CREATE TABLE {tb_name} (AdmNo int(5) PRIMARY KEY AUTO_INCREMENT,RollNo int(5) UNIQUE, StudentName varchar(30), Mail varchar(30) UNIQUE, DoB date, BirthPlace varchar(100), MotherTongue varchar(20), MotherName varchar(30), FatherName varchar(30), Nationality varchar(30), Caste varchar(10), Address varchar(100), ParentOccupation varchar(30),  ParentOccupationCategory varchar(25), ParentPay int(11), ParentMobile varchar(20), ParentOfficeAddress varchar(100), ParentOfficeTelephone int(10), XLastAttended date, XMedium varchar(20), XBoard varchar(20), XPassYear YEAR, XRollNo int(15) UNIQUE, XEng int(3) DEFAULT 0, XMaths int(3) DEFAULT 0, XScience int(3) DEFAULT 0, XSocial int(3) DEFAULT 0, XIILang int(3) DEFAULT 0, XTotalMarks int(3) DEFAULT 0, XPercentage decimal(5,2) DEFAULT 0, Class varchar(5) DEFAULT "XI", Sub varchar(4))')
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
    pa_mob = input("Enter Parent's Mobile Number: ")
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

    try:
        qry = 'INSERT INTO {} (StudentName, Mail, DoB, BirthPlace, MotherTongue, MotherName, FatherName, Nationality, Caste, Address, ParentOccupation, ParentOccupationCategory, ParentPay, ParentMobile, ParentOfficeAddress, ParentOfficeTelephone, XLastAttended, XMedium, XBoard, XPassYear, XRollNo, XEng, XMaths, XScience, XSocial, XIILang, XTotalMarks, XPercentage, Sub) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ,%s ,%s, %s, %s ,%s, %s, %s, %s, %s, %s, %s ,%s, %s, %s, %s, %s, %s)'.format(tb_name)

        val = (stu_name, stu_mail, stu_dob, stu_bplace, stu_motong, stu_moname,stu_faname, stu_nat, stu_caste, stu_add, pa_occ, pa_occcat, pa_pay, pa_mob, pa_oadd, pa_otel, x_lastatt, x_med, x_board, x_passyr, x_rollno, x_eng, x_maths, x_sci, x_ss, x_2lang, x_totmrks, x_per, sub_choice)

        cur.execute(qry, val)#29
        mydb.commit()
        print(f'\n...{stu_name}, Welcome to AECS-3, Tarapur\n')

        qry = 'SELECT MAX(AdmNo) FROM {}'.format(tb_name)
        cur.execute(qry)
        res = cur.fetchone()
        print(f'\nYour Admission Number is: {res[0]}\n')
    except Error as e:
        print('\nPlease enter valid information.')
        print(e)
        print()
        f_enter_adm(acad_yr)

    flag = True
    while flag:
        choice = input('Want to enter data for one more student? (Yes/No): ')
        if choice.lower() == "yes":
            f_enter_adm(acad_yr)
            flag = False
        elif choice.lower() == "no":
            f_adm(acad_yr)
            flag = False
        else:
            print('Enter valid command')
            flag = True

def f_display_adm(acad_yr):

    tb_name = f"adm{acad_yr}"

    #display table of admno and name
    qry = f'SELECT AdmNo, StudentName FROM {tb_name}'
    cur.execute(qry)
    res = cur.fetchall()

    if len(res) == 0:
        print(f'\nNo students in XI the for academic year {acad_yr}')
        f_adm(acad_yr)
    else:
        res.insert(0, ['Admission Number', 'Name of the Student'])
        
        f_display(res)

        #ask for admno and give full details
        admno = int(input('Enter Admission Number of the Student to Display Data: '))
        print(len(res))
        for x in range(1,len(res)):
            if admno == res[x][0]:
                qry = f'SELECT * FROM {tb_name} WHERE AdmNo = {admno}'
                cur.execute(qry)
                data = cur.fetchone()
                print(data)

                # create lol for display
                data_header = ['Admission Number','Roll No', 'Student Name', 'Mail', 'Date of Birth', 'Birth Place', 'Mother Tongue', 'Mother Name', 'Father Name', 'Nationality', 'Caste', 'Address', 'Parent Occupation', 'Parent Occupation Category', 'Parent Pay', 'Parent Mobile', 'Parent Office Address', 'Parent Office Telephone', 'X Last Attended', 'X Medium', 'X Board', 'X Passing Year', 'X RollNo', 'X Eng Marks', 'X Maths Marks', 'X Science Marks', 'X Social Marks', 'X II Lang Marks', 'X Total Marks', 'X Percentage Marks', 'Class', 'Sub']

                bigdata = []
                for i in range(len(data)):
                    l=[]
                    l.append(data_header[i])
                    l.append(data[i])
                    print(l)
                    bigdata.append(l)

                # create date to display
                for i in range(len(bigdata)):
                    if type(bigdata[i][1]) == type(datetime.date(2005, 7, 2)):
                        bigdata[i][1] = str(bigdata[i][1])
                if bigdata[1][1] == None:
                    bigdata[1][1] = 'Unassigned'
                f_display(bigdata)

        flag = True
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

def f_update_adm(acad_yr):
    tb_name = f"adm{acad_yr}"




def f_rc_xi(acad_yr):

    tb_name = f'rc{acad_yr}'

    # ask admission no 
    # adm_no = input()
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
    cur.execute('USE csproj')
    print('\n...Database csproj Created\n')

cur = mydb.cursor()

# Starting Interface

print('\n+--------------+')
print('| JC REGISTRAL |')
print('+--------------+\n')

#$ THINK FOR THE SYMBOL
print('====================================================================')
print('\nWelcome to JC REGISTRAL\nIt is a tool for all registration process of Junior College Students\n')
print('====================================================================')
#  from Admission in XI to getting Transfer Certifcate of Class XII

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
    ['4','Assign Roll Number'],
    ['5','Back to Home']]

xii_home = [['Command', 'Function'],
    ['1','Check/Enter Fees Details'],
    ['2','Generate Report Card'],
    ['3','Check Rank List'],
    ['4','Check Transfer Certificate'],
    ['5','Back to Home']]

sub_c = [['Command', 'Subjects'],
    ['1', 'Physics, Chemistry, Maths, English, Computer Science'],
    ['2', 'Physics, Chemistry, Maths, English, Biology']]

adm_up = [['Command', 'To Change'],
['1', 'Student Name'],
['2', 'Mail'],
['3', 'Date of Birth'],
['4', 'Birth Place'],
['5', 'Mother Tongue'],
['6', 'Mother Name'],
['7', 'Father Name'],
['8', 'Nationality'],
['9', 'Caste'],
['10', 'Address'],
['11', 'Parent Occupation'],
['12', 'Parent Occupation Category'],
['13', 'Parent Pay'],
['14', 'Parent Mobile'],
['15', 'Parent Office Address'],
['16', 'Parent Office Telephone'],
['17', 'X Last Attended'],
['18', 'X Medium'],
['19', 'X Board'],
['20', 'X RollNo'],
['21', 'X Eng Marks'],
['22', 'X Maths Marks'],
['23', 'X Science Marks'],
['24', 'X Social Marks'],
['25', 'X II Lang Marks'],
['26', 'X Total Marks'],
['26', 'X Percentage Marks'],
['27', 'Sub']]


print('\n...Running the panel\n')
f_panel()
