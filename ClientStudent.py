import StudentScheduler as s
def takeInput():
    return input("Chooose :\n 1.addStudent \n 2. ViewAllStudent \n 3. studentDetails By roll \n 4.BatchDetails by bid \n 5.batchDetails by roll \n 6.Exit")
def fun1():
    numOfStud = input("Enter how many Student")
    for i in range(0,(int)(numOfStud)):
        name = input("Enter name of Student")
        roll = input("Enter roll of Student")
        res =newScheduler.addStudent(name, roll)
        if(res == 1):
            print("Roll number already Exist")
        else:
            print("Student inserted succesfull")

def fun2():
    listStudn = newScheduler.showAllStudents()
    for it in range(0, listStudn.__len__()):
        print("Name : ", listStudn[it].name, " Roll : ", listStudn[it].rollNumber)
newScheduler = s.StudentScheduler()
menuOption = takeInput()
while(menuOption != "6"):
    if(menuOption == "1"):
        fun1()
        menuOption = takeInput()
    elif(menuOption == "2"):
        fun2()
        menuOption = takeInput()
    elif(menuOption == "3"):
        print("This feature is under development")
        menuOption = takeInput()
    else:
        print("Not valid choice")

'''def f(menuOption):
    return {
        '1':fun1(),
        '2':fun2()
    }.get(menuOption,print("Not valid choice"))
    '''
