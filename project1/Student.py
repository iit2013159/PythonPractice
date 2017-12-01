class Student:
    def __init__(self):
        self.courses = list()
    def __str__(self):
        courseStr =""
        for k in range(0, self.courses.__len__()):
            courseStr += self.courses[k]+ " , "
        return "Name :" +self.name + "\nCourses :"+courseStr+"\nRoll :" +self.rollNumber
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
