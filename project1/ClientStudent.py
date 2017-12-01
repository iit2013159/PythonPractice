import StudentScheduler as s
def takeInput():
    return input("Chooose :\n 1.addStudent \n 2. ViewAllStudent \n 3. studentDetails By roll \n 4.BatchDetails by bid \n 5.Exit")
def fun1():
    numOfStud = input("Enter how many Student")
    for i in range(0,(int)(numOfStud)):
        name = input("Enter name of Student")
        roll = input("Enter roll of Student")

        res =newScheduler.addStudent(name, roll)
        if(res == 0):
            print("Roll number already Exist")
        else:
            noOfCourse = int(input("How many Courses"))
            for x in range(0, noOfCourse):
                courseName = input("Enter course Name")
                res.addCourses(courseName)
            newScheduler.addStudentToBatch(res)
            print("Student inserted succesfull")
            print(res)

def fun2():
    listStudn = newScheduler.showAllStudents()
    for it in range(0, listStudn.__len__()):
        print("Name : ", listStudn[it].name, " Roll : ", listStudn[it].rollNumber)
newScheduler = s.StudentScheduler()
menuOption = takeInput()
while(menuOption != "5"):
    if(menuOption == "1"):
        fun1()
        menuOption = takeInput()
    elif(menuOption == "2"):
        fun2()
        menuOption = takeInput()
    elif(menuOption == "3"):
        roll = input("Please enter the roll of student")
        for i in range(0,newScheduler.listStudent.__len__()):
            if(newScheduler.listStudent[i].rollNumber == roll):
                print (newScheduler.listStudent[i])
        menuOption = takeInput()
    elif (menuOption == "4"):
        for i in range(0,newScheduler.listBatch.__len__()):
            print(newScheduler.listBatch[i])
        menuOption = takeInput()
    else:
        print("Not valid choice")
        menuOption = takeInput()

'''def f(menuOption):
    return {
        '1':fun1(),
        '2':fun2()
    }.get(menuOption,print("Not valid choice"))
    '''
