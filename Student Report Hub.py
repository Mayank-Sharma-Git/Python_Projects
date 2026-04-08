"    STUDENT REPORT HUB    "

# Importing Libraries (pickle and os)

import pickle

import os

# Creating Method to add Student in a binary file

def addstudent():
    
    file = open('student.bin','ab')

    sid = int(input("Assign Student ID: "))
    sname = input("Student's Name: ")
    srn = int(input("Student's Roll No.: "))
    sage = int(input("Student's Age: "))
    sphone = int(input("Student's Phone numeber: "))
    pickle.dump(sid,file)
    pickle.dump(sname,file)
    pickle.dump(srn,file)
    pickle.dump(sage,file)
    pickle.dump(sphone,file)

    print("Student Addded")
    input("Press ENTER to Continue...")


    file.close()


# Creating A Method to View All the Students from student.bin file

def viewstudents():

    file = open('student.bin','rb')

    try:
        while True:
            for i in range(5):
                V1 = pickle.load(file)
                print("  ",V1,end='')
                
            print("\n")
            
    except:
        pass
    input("Press ENTER to Continue...")
    file.close()


# Creating A Method to Update a Student's information

def updatestudent():
    file = open('student.bin','rb')
    file1 = open('temp.bin','ab')

    flag = 0
    
    V1 = int(input("Student's ID: "))
   
    V3 = input("Enter 'R' to Change Roll No., 'P' For Phone number Change , 'A' for Age Update:  ")
    try:
        if V3=='R':
            while True:
                V2 = pickle.load(file)
                if V1==V2:
                    pickle.dump(V2,file1)

                    sname = pickle.load(file)
                    pickle.dump(sname,file1)

                    print("Old Roll No.: ",pickle.load(file))
                    srn1 = int(input("New Roll No.: "))
                    pickle.dump(srn1,file1)

                    sage = pickle.load(file)
                    pickle.dump(sage,file1)

                    sphone = pickle.load(file)
                    pickle.dump(sphone,file1)
                    
                    flag = 1
                    print("Roll No. Updated!")
                    break

                else:
                    pickle.dump(V2,file1)

                    sname = pickle.load(file)
                    pickle.dump(sname,file1)

                    srn = pickle.load(file)
                    pickle.dump(srn,file1)

                    sage = pickle.load(file)
                    pickle.dump(sage,file1)

                    sphone = pickle.load(file)
                    pickle.dump(sphone,file1)
                    
        if V3=='P':
            while True:
                V2 = pickle.load(file)
                if V1==V2:
                    pickle.dump(V2,file1)

                    sname = pickle.load(file)
                    pickle.dump(sname,file1)

                    srn = pickle.load(file)
                    pickle.dump(srn,file1)

                    sage = pickle.load(file)
                    pickle.dump(sage,file1)

                    print("Old Number: ", pickle.load(file))
                    sphone1 = int(input("New Phone Number: "))
                    pickle.dump(sphone1,file1)

                    flag = 1
                    print("Phone Updated!")
                    break

                else:
                    pickle.dump(V2,file1)

                    sname = pickle.load(file)
                    pickle.dump(sname,file1)

                    srn = pickle.load(file)
                    pickle.dump(srn,file1)

                    sage = pickle.load(file)
                    pickle.dump(sage,file1)

                    sphone = pickle.load(file)
                    pickle.dump(sphone,file1)

        if V3=='A':
            while True:
                V2 = pickle.load(file)
                if V1==V2:
                    pickle.dump(V2,file1)

                    sname = pickle.load(file)
                    pickle.dump(sname,file1)

                    srn = pickle.load(file)
                    pickle.dump(srn,file1)

                    print("Old Age: ",pickle.load(file))
                    sage = int(input("New Age: "))
                    pickle.dump(sage,file1)

                    sphone = pickle.load(file)
                    pickle.dump(sphone,file1)

                    flag = 1
                    print("Age Updated")
                    break


                else:
                    pickle.dump(V2,file1)

                    sname = pickle.load(file)
                    pickle.dump(sname,file1)

                    srn = pickle.load(file)
                    pickle.dump(srn,file1)

                    sage = pickle.load(file)
                    pickle.dump(sage,file1)

                    sphone = pickle.load(file)
                    pickle.dump(sphone,file1)

    except:
        
        if flag==0:
            print("Student does not Exists")
        input("Press ENTER to Continue...")

    file.close()
    file1.close()
    os.remove('student.bin')
    os.rename('temp.bin','student.bin')


#Creating Method to Delete A Student

    
def deletestudent():
    
    file = open('student.bin','rb')
    file1 = open('temp.bin','ab')

    flag = 0
    
    V1 = int(input("Student ID: "))
    try:
        while True:
            V2 = pickle.load(file)
            
            if V2==V1:
                pickle.load(file)
                pickle.load(file)
                pickle.load(file)
                pickle.load(file)

                print("Student Deleted Sucessfully")
                flag = 1
                break
            else:
                pickle.dump(V2,file1)

                sname = pickle.load(file)
                pickle.dump(sname,file1)

                srn = pickle.load(file)
                pickle.dump(srn,file1)

                sage = pickle.load(file)
                pickle.dump(sage,file1)

                sphone = pickle.load(file)
                pickle.dump(sphone,file1)


    except:
        if flag==0 :
            print("Student Does Not Exists")
        input("Press ENTER to Continue...")
    
    file.close()
    file1.close()
    os.remove('student.bin')
    os.rename('temp.bin','student.bin')


#Method To Add A Subject

def addsubject():

    file = open('subject.bin','ab')

    subid = int(input("Enter Subject ID :"))
    subname = input("Enter Subject Name :")
    maxmarks = int(input("Enter Max a Student Can Obtain :"))

    pickle.dump(subid,file)
    pickle.dump(subname,file)
    pickle.dump(maxmarks,file)
    print("Subject Added!")

    input("Press ENTER To Continue...")

    file.close()

# Method To View All Subjects

def viewsubjects():

    file = open('subject.bin','rb')
    try:
        while True:
            V1 = pickle.load(file)
            V2 = pickle.load(file)
            V3 = pickle.load(file)

            print("\nSubject ID :",V1)
            print("Subject Name :",V2)
            print("Subject Max Marks :",V3)
            print("_"*25)

    except:
        input("Press ENTER To Continue...")
        pass

    file.close()


# Method to Remove A Subject

def removesubject():

    file = open('subject.bin','rb')
    file1 = open('temp.bin','wb')

    flag = 0
    
    V1 = int(input("Subject ID :"))
    
    try:
        while True:
            SubID = pickle.load(file)
            
            if SubID==V1:
                pickle.load(file)
                pickle.load(file)
                print("Subject Removed Sucessfully!")
                flag = 1
                break

            else:
                pickle.dump(SubID,file1)

                SubName = pickle.load(file)
                pickle.dump(SubName,file1)

                SubMarks = pickle.load(file)
                pickle.dump(SubMarks,file1)
    except:
        if flag==0:
            print("Subject does not exists")
        
        pass
    input("Press ENTER To Continue...")

    file.close()
    file1.close()
    os.remove('subject.bin')
    os.rename('temp.bin','subject.bin')

# Method For returning Student Name Through Student ID

def sudname(ID):

    file = open('student.bin','rb')

    sudname = []

    try:
        while True:
            V1 = pickle.load(file)
            if V1==ID:
                sudname.append(pickle.load(file))
                break

    except:
        pass
    
    file.close()
    return sudname  

# Method For returning Subject Name Through Subject ID

def subname(ID):

    file = open('subject.bin','rb')
    subname = []

    try:
        while True:
            V1 = pickle.load(file)
            
            if ID==V1:
                subname.append(pickle.load(file))
                break

    except:
        pass
    file.close()
    return subname



# Method for Inserting Marks For A Student

def insertmarks():

    file = open('results.bin','ab')

    SudID = int(input("Student ID :"))

    studentname = sudname(SudID)
    if not studentname:
        print("Student Not Found")
        return

    pickle.dump(SudID,file)
    pickle.dump(studentname[0],file)

    count = int(input("How many subjects?: "))   
    pickle.dump(count,file)

    for i in range(count):
        SubID = int(input("Subject ID :"))
        pickle.dump(SubID,file)

        subjectname = subname(SubID)

        if not subjectname:
            print("Subject Not Exists")
            return
        
        pickle.dump(subjectname[0],file)

        marks = int(input("Marks: "))
        pickle.dump(marks,file)

    file.close()
   

# Method to View Marks By Student

def marksbystudent():

    file = open('results.bin','rb')
            
    sudid = int(input("Student ID :"))

    studentname = sudname(sudid)

    print("Student ID :",sudid,"   ","Student Name :",studentname[0])
    
    try:
        while True:
            
            
                V1 = pickle.load(file)
                if V1==sudid:
                    pickle.load(file)
                    
                    print("\nSubject ID :",pickle.load(file))
                    print("Subject Name :",pickle.load(file))
                    print("marks :",pickle.load(file))
                    print("_"*25)

                
    except:
        input("Press ENTER To Continue...")
        pass
    

    file.close()


    
# Method To View Marks By Subject

def marksbysubject():

    file = open('results.bin','rb')
            
    subid = int(input("Subject ID :"))

    subjectname = subname(subid)

    if not subjectname:
        print("Subject Not Exists")
        return

    print("Subject ID :",subid,"   ","Subject Name :",subjectname[0])
    
    try:
        while True:
            sid = pickle.load(file)
            sname = pickle.load(file)
            
            
            while True:
                

                suid = pickle.load(file)
                suname = pickle.load(file)
                marks = pickle.load(file)
                
                if suid==subid:
                
                    print("\nStudent ID :",sid)
                    print("Student Name :",sname)
                    print("Marks :",marks)
                    print("_"*25)

                
    except:
        input("Press ENTER To Continue...")
        pass
    

    file.close()






#Creating Dashboard

    
while True:
    print("""


            1. Adding a Student
            
            2. View All Students
            
            3. Update Student Info.(Roll No.)
            
            4. Deleting a Student
            ___________________________________________
            
            5. Adding a Subject

            6. View all Subjects
            
            7. Changing or Removing a Subject
            ___________________________________________
            
            8. Enter Marks for a Student
            
            9. View Marks by Student
            
            10. View Marks by Subject

            ___________________________________________

            
            0. Exit




    """)

# Creating Control Block


    Var1 = int(input("Enter What you wanna do: "))

    if Var1==0:
        print("Student Reporting System Logging off")
        break
    elif Var1==1:
        addstudent()
    elif Var1==2:
        viewstudents()
    elif Var1==3:
        updatestudent()
    elif Var1==4:
        deletestudent()
    elif Var1==5:
        addsubject()
    elif Var1==6:
        viewsubjects()
    elif Var1==7:
        removesubject()
    elif Var1==8:
        insertmarks()
    elif Var1==9:
        marksbystudent()
    elif Var1==10:
        marksbysubject()
    

                                        





























