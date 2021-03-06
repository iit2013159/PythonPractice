import Student as s
import Batch as b
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
        #self.addStudentToBatch(newStudent) #automatically asssign into a batch depending on courses opted
        return newStudent

    def addBatch(self,newBatch):
        self.listBatch.append(newBatch)

    def showAllStudents(self):
        return self.listStudent

    def getAllBatch(self):
        return self.listBatch

    def addStudentToBatch(self,student):

        listCourseStudent = student.getCouses()
        for i in range(0,listCourseStudent.__len__()):
            batchlist = self.getAllBatch()
            noBatch = 0
            for j in range(0,batchlist.__len__()):
                if(listCourseStudent[i] == batchlist[j].courseName):
                    batchlist[j].addStudent(student)
                    noBatch = 1
            if(noBatch == 0):
                newBatch = b.Batch()
                newBatch.courseName = listCourseStudent[i]
                self.listBatch.append(newBatch)
                i -= 1

