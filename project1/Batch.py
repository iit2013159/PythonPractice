import StudentScheduler as s
import random as r


class Batch:

    def __init__(self):
        self.id = r.randint(1, 100)
        self.students = list()
        self.facultyName = "Not assigned"

    def __str__(self):
        return "Id :" + str(self.id) + "\nCourseName : " + self.courseName + "\nFaculty Name : " + self.facultyName

    def getId(self):
        return self.id

    def getCourseName(self):
        return self.courseName

    def setCourseName(self, cousrseName):
        self.courseName = cousrseName

    def getFacultyName(self):
        return self.facultyName

    def setFacultyName(self, facultyName):
        self.facultyName = facultyName

    def getStudents(self):
        return self.students

    def addStudent(self, newStudent):
        self.students.append(newStudent)
