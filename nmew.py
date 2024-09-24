import mysql.connector as mconn
mydb= mconn.connect(host="localhost",user="root",passwd="8587",database="quiz_comp")
mycursor=mydb.cursor()
def menu():
    print("+-------------------------------------------------------------------------------------------------------------------------------+")
    print("                                                QUIZ COMPETITION MANAGEMENT PROGRAM                                      ")
    print("+-------------------------------------------------------------------------------------------------------------------------------+")
    print("        PRESS 1 FOR INSERTING QUESTIONS WITH OPTIONS AND ANSWERS                                       ")
    print("        PRESS 2 FOR ADDING PARTICIPANTS DETAILS                                                                              ")
    print("        PRESS 3 FOR UPDATING SCORES OF PARTICIPANTS                                                                     ")
    print("        PRESS 4 FOR DISPLAYING QUESTIONS WITH ANSWERS                                                             ")
    print("        PRESS 5 FOR DISPLAYING SCORES OF PARTICIPANTS                                                                  ")
    print("        PRESS 6 FOR SEARCHING DETAILS OF A PARTICIPANT                                                                 ")
    print("        PRESS 7 FOR REMOVING ANY QUESTIONS                                                                                     ")                                                                
    print("+--------------------------------------------------------------------------------------------------------------------------------+")
#---------------------------------------------------------------------------TABLES MAKING---------------------------------------------------------------------#
def table1() :
    print("CREATING A NEW TABLE(question1) IN DATABASE ")
    mycursor.execute("create table questions1(qno_no int(3) primary key , qno_desc varchar(5000),opt_a varchar(500), opt_b varchar(500), opt_c varchar(500) ,opt_d varchar(500) , ans varchar(5000))")
    mydb.commit()
    print("TABLE 'questions1' CREATED")
    
#----------------------------------------------------------------#            
def table2():
    print(" CREATING A NEW TABLE(scores) IN DATABASE ")
    mycursor.execute("create table scores(reg_no int(5) primary key , participant_name varchar(50),scores int(50),total_correct int(50),total_wrong int(50),total_attempted int(50))")
    mydb.commit()
    print("TABLE 'scores' CREATED")
    
#-----------------------------------------------------------------#            
def table3():
    print(" CREATING A NEW TABLE(participants) IN DATABASE")
    mycursor.execute("create table participants(reg_no int(5) primary key , pname varchar(50), age_groupscores int(10),city varchar(50), no_of_appearances_made int(10))")
    mydb.commit()
    print("TABLE 'participants' CREATED")
   
#--------------------------------------------------------------------------TABLE SAVING OR DELETING OR DROPPING--------------------------------------------------#
def save():
    mycursor.execute("show tables;")
    myresult=mycursor.fetchall()
    for x in myresult :
        print(x)
    response1=input("DO YOU WANT TO SAVE OR DELETE ANY TABLE FROM ABOVE (S/D) ??:")
    if response1 in "SsSAVEsaveSave":
        print("ALL TABLES ARE SAVED !!")
    elif response1 in "DDELETEdDeletedelete":
        resp=input("WHICH TABLE YOU WANT TO DELETE ? :")
        if resp=="questions1":
            mycursor.execute("drop table questions1")
            mydb.commit()
        elif resp=="scores":
            mycursor.execute("drop table scores")
            mydb.commit()
        elif resp=="paticipants":
            mycursor.execute("drop table participants")
            mydb.commit()
        else:
            print("NO TABLE OF THIS NAME EXIST .")
            save()
#--------------------------------------------------------------------------PROGRAMMING FOR QUIZ---------------------------------------------------------------------#
def questions1():  

    sql=int(input("enter the index_no:"))
    sql1=input("enter the ques_desc:")
    sql2=input("enter the option a:")
    sql3=input("enter the option b:")
    sql4=input("enter the option c:")
    sql5=input("enter the option d:")
    sql6=input("the answer is:")

    sql_in= "insert into questions1 values(" + str( sql) + ",'" + (sql1)+ "'"+",'" + (sql2) + "'"+",'" + (sql3) +"'" +",'"+ (sql4) +"'"+",'" + (sql5) +"'"+ ",'"+(sql6) +"'"")"
    mycursor.execute(sql_in)
    mydb.commit()
    print("your request has been processed.Thank you for making us as a part of your project")

def participants():
    sql6=int(input("enter the participant reg_no:"))
    sql7=input("enter the participant name:")
    sql8=int(input("enter the age group:"))
    sql9=input("enter the city:")
    sql10=int(input("enter the no of appearances made:"))
                                                                   
    sql_int="insert into participants values("+ str(sql6)+ ",'" + (sql7) + "'" + ",'"+str(sql8) + "'" + ",'"+(sql9) +"'"+ ",'"+str(sql10)+"'"")"
    print(sql_int)
    mycursor.execute(sql_int)
    print("participants are all updated")
    mydb.commit()
   
def score_updates():
    a=int(input("enter the reg_no"))
    b=input("enter the participants name")
    c=int(input("enter the scores"))
    d=int(input("enter the total correct answer"))
    e=int(input("enter the incorrect answer"))
    f=int(input("enter the no_of_attempted_questions"))

    sql_insert="insert into scores values("+ str(a) +",'"+ (b) +"'"+",'"+ str(c)+"'"+",'"+ str(d) +"'"+ ",'"+str(e) +"'"+",'"+ str(f)+ "'"")"
    print(sql_insert)
    mycursor.execute(sql_insert)
    mydb.commit()
def display():
    mycursor.execute("select * from questions1")
    data=mycursor.fetchall()
    for rec in data :
        print(rec[0],rec[1],'\n','\tA.',rec[2],'\tB.',rec[3],'\tC.',rec[4],'\tD.',rec[5],'\nANSWER:',rec[6])

def score_display():
    mycursor.execute("select * from scores")
    sc=mycursor.fetchall()
    print("reg_no.\tname\tscores\t       correct_ans\t   incorrect_ans  \t   ques_attempted")
    print("----------------------------------------------------------------------------------------------------------------")
    for B in sc :
        print(B[0],"\t",B[1],"\t",B[2],"\t\t",B[3],"\t\t",B[4],"\t\t",B[5])


def search_part():
    yy=int(input("Enter participant reg_no."))
    u="Select * from participants where reg_no='{}'".format(yy)
    mycursor.execute(u)   
    dis=mycursor.fetchall()
    if dis==[]:
        print("RECORD DOES NOT EXIST")
    else:
        for D in dis:
            print("Participant reg_no:",D[0])
            print("Participant name:",D[1])
            print("Age Group:",D[2])
            print("City:",D[3])
            print("No. of Appearances made :",D[4])


def del_ques():
    qn=int(input("Enter the index no. :"))
    zz="delete from questions1 where qno_no='{}' ".format(qn)
    mycursor.execute(zz)
    if mycursor.rowcount==0:
        print("Record either does not exist or already deleted.")
    else:
        print(mycursor.rowcount, "is deleted.")
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def checking():
    mycursor.execute("show tables;")
    myresults=mycursor.fetchall()
    for tab in myresults:
        print(tab)   
    mydb.commit()
    if myresults==[]:
        table1()
        table2()
        table3()
    elif myresults==[('questions1',)]:
        table2()
        table3()
    elif myresults==[('scores',)]:
        table1()
        table3()
    elif myresults==[('participants',)]:
        table1()
        table2()
    elif myresults==[('questions1',),('scores',)]:
        table3()
    elif myresults==[('questions1',),('participants',)]:
        table2()
    elif myresults==[('scores',),('participants',)]:
        table1()
    elif myresults==[('scores',),('questions1',)]:
        table3()
    elif myresults==[('participants',),('scores',)]:
        table1()
    elif myresults==[('participants',),('questions1',)]:
        table2()
    else :
         print("ALL THE TABLES ARE ALREADY MADE !!")
         
#------------------------------------------------------------------------MAIN PROGRAM FOR QUIZ----------------------------------------------------------------------#
def quiz():
    menu()
    choice=input("enter your wish:")
    if choice=="1":
        questions1()
    elif choice=="2":
        participants()
    elif choice=="3":
        score_updates()
    elif choice=="4":
        display()
    elif choice=="5":
        score_display()
    elif choice=="6":
        search_part()
    elif choice=="7":
        del_ques()
    else:
        print("WRONG INPUT !!!! TRY AGAIN")
        quiz()
#------------------------------------------------------------------------------RUNNING OF PROGRAM-------------------------------------------------------------------#
def reply():
    REP=input(" Do you want to continue(Y/N):")
    if REP in "YESYesYyesy":
        quiz()
        reply()
    elif REP in "NONoNnon":
        print("THANK FOR USING THIS PROGRAM")
    else:
        print("WRONG INPUT !!!! TRY AGAIN")
        reply()
checking()
quiz()        
reply()
save()

