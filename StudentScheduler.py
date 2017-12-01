import Student as s

class StudentScheduler:
    def __init__(self):
        self.listStudent = list()
        self.listBatch = list()

    def addStudent(self,name,roll):
        for i in range(0,self.listStudent.__len__()):
            if(self.listStudent[i].rollNumber == roll):
                return 1
        newStudent = s.Student()
        newStudent.setName(name)
        newStudent.setRollNumber(roll)
        self.listStudent.append(newStudent)
        self.addStudentToBatch(newStudent) #automatically asssign into a batch depending on courses opted
        return 0

    def addBatch(self,newBatch):
        self.listBatch.append(newBatch)

    def showAllStudents(self):
        return self.listStudent

    def getAllBatch(self):
        return self.listBatch

    def addStudentToBatch(self,student):
        batchlist = self.getAllBatch()
        for i in range(0,batchlist.__len__()):
            listCourseStudent = student.getCouses()
            for j in range(0,listCourseStudent.__len__()):
                if(listCourseStudent[j] == batchlist[i].courseName):
                    batchlist[i].addStudent(student)

