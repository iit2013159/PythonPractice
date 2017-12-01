class Student:
    def __init__(self):
        self.courses = list()

    def getRollNumber(self):
        return self.rollNumber
    def setRollNumber(self,roll):
        self.rollNumber = roll

    def getName(self):
        return self.name
    def setName(self,name):
        self.name = name

    def getCouses(self):
        return self.courses
    def addCourses(self,course ):
        self.courses.append(course)
