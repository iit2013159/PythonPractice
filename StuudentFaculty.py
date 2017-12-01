import StudentCourse as s
class Faculty:
    def __init__(self):
        self.courseNames = list()
    def getId(self):
        return self.id

    def setId(self,id):
        self.id = id

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getCouseNames(self):
        return self.courseNames

    def addCourseNames(self,courseName):
        newCourse = s.Course()
        newCourse.setCourseName(courseName)
        self.courseNames.append(newCourse)
        return "new Course has been added"