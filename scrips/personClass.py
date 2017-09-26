#imports

import datetime


#classes
class Person(object):
    def __init__(self, name):
        '''
        create a person called name
        '''
        self.name = name
        self.birthDay = None
        self.lastName = name.split(' ')[-1]

    def getLastName(self):
        '''
        return users last name
        '''
        return self.lastName

    def setBirthday(self, month, day, year):
        '''
        sets self's birthday to birthDay
        '''
        self.birthDay = datetime.date(year, month, day)

    def getAge(self):
        '''
        return self's current age in days
        '''
        if self.birthDay == None:
            raise ValueError
        return (datetime.date.today() - self.birthDay).days

    def __lt__(self, other):
        '''
        return True if self's name is lexicographicalyy less than other's last name
        and False otherwise
        '''
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName

    def __str__(self):
        '''
        return self's name
        '''
        return self.name

class MITPerson(Person):

    nextIdNum = 0 # next ID number to assign

    def __init__(self, name):
        #initialiaze Person attributes
        Person.__init__(self,name)
        self.idNum = MITPerson.nextIdNum
        MITPerson.nextIdNum += 1

    def getIdNum(self):
        return self.idNum

    def __lt__(self, other):
        # sorting  MIT people uses their ID number, not name
        return self.idNum < other.idNum


    def speak(self, utterance):
        # example using the last name:
        #return (self.getLastName() + ' says: ' + utterance )
        # example using the fist name:
        return (self.name + ' says: ' + utterance)

class Professor(MITPerson):

    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department

    def speak(self, utterance):
        new = 'In course ' + self.department + ' we say: '
        return MITPerson.speak(self, new + utterance)

    def lectune(self, topic):
        return self.speak('Its obvious that ' + topic)

class Student(MITPerson):
    pass

class UG(Student):

    def __init__(self, name, classYear):
        MITPerson.__init__(self,name)
        self.year = classYear

    def getClass(self):
        return self.year

    def speak(self, utterance):
        return (MITPerson.speak(self, ' Dude, ' + utterance ))


class Grad(Student):
    pass

class TransferStudent(Student):
    pass

class Grades(object):
    '''
    A mapping from to student to a list of grades
    '''

    def __init__(self):
        '''
        Create empty grade book
        '''
        self.students = [] # list of student objects
        self.grades = {} # maps idNum --> list of grades
        self.isSorted = True # true if self.student is sorted

    def addStudent (self, student):
        '''
        Assume student is a type of student
        add student to the grade book
        '''
        if student in self.students:
            raise ValueError ('Duplicate student')
        self.students.append(student)
        self.grades[student.getIdNum()] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        '''
        Assumes grade is a float
        Add grade to the list of grades student
        '''
        try:
            self.grades[student.getIdNum()].append(grade)
        except:
            raise ValueError ('Student not in grade book')


    def getGrades(self, student):
        '''
        Return a list of grades for student
        '''
        try: # return a copy of student grades
            return self.grades[student.getIdNum()][:]
        except:
            raise ValueError ('Student not in grade book')

    def allStudents(self):
        '''
        Return a list of the students in the grade book
        '''
        # # first method using a copy

        # if not self.isSorted:
        #     self.students.sort()
        #     self.isSorted = True
        # # return a copy of list students
        # return self.students[:]

        # second method using generator

        if not self.isSorted:
            self.students.sort()
            self.isSorted = True
        for s in self.students:
            yield s

## functions

def gradeReport(course):
    '''
    Assumes: course is of type of grades
    '''
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot / numGrades
            report.append(str(s) + '\' means grade is ' + str(average))
        except ZeroDivisionError:
            report.append((str(s) + '\'s has no grades'))

    return '\n'.join(report)

def isStudent(obj):
    return isinstance(obj, Student)

if __name__ == "__main__":
    # import data
    p1 = Person('Mark Zuckerberg')
    p1.setBirthday(5,14,84)
    p2 = Person('Drew Houston')
    p2.setBirthday(3, 4, 83)
    p3 = Person('Bill Gates')
    p3.setBirthday(10, 28, 55)
    p4 = Person('Adrew Gates')
    p5 = Person('Steve Wozniak')

    #import data into a list
    personList = [p1, p2, p3, p4, p5]
    print('=====================================')
    print('The person of p1 is: ', p1)
    print('=== names in the list ====')
    for e in personList:
        print(e)
    print('=====================================')
    #sort the list
    personList.sort()
    print('=== sorted names in the list ====')
    for e in personList:
        print(e)
    print('=====================================')
    m3 = MITPerson('Mark Zuckerberg')
    #m3.setBirthday(5,14,84)
    Person.setBirthday(m3, 5, 14, 84)
    m2 = MITPerson('Drew Houston')
    Person.setBirthday(m2, 3, 4, 83)
    m1 = MITPerson('Bill Gates')
    Person.setBirthday(m1, 10, 28, 55)
    MITPersonList = [m1, m2, m3]
    for e in MITPersonList:
        print(e)
    print('=====================================')
    print('===  MIT List sorted by id number  ==')
    MITPersonList.sort()
    for e in MITPersonList:
        print(e)
    print('=====================================')
    print(m1.speak('Hi there! '))
    print('=====================================')
    d1 = MITPerson('Eric')
    d2 = MITPerson('John')
    d3 = MITPerson('John')
    d4 = Person('John')
    print(d1 < d2)
    #print(d1 < d4 ) #AttributeError: 'Person' object has no attribute 'idNum'
    #actually runs the code d1.__lt__(d4)
    #it compares the idNums and d4 doesn't have one
    #it's a person object
    print(d4 < d1)
    # actually runs the code d4.__lt__(d1)
    # it compares based on the name
    print('=====================================')
    #import data
    s1 = UG('Matt Damon', 2017)
    s2 = UG('Ben Affleck', 2017)
    s3 = UG('Lin Manuel Mirande', 2018)
    print(s1)
    print(s1.getClass())
    print(s1.speak('Where is the quiz?'))
    print(s2.speak('I have no idea mate!'))
    print('=====================================')
    # examples of the speak method per object
    faculty = Professor('Doctor Arrogant', 'six')
    print(m1.speak('hi there!'))
    print(s1.speak('hi there!'))
    print(faculty.speak('hi there!'))
    print(faculty.lectune('Computer science rocks'))
    print('=====================================')
    ug1 = UG('Matt Damon', 2018)
    ug2 = UG('Ben Affleck', 2019)
    ug3 = UG('Drew Houston', 2017)
    ug4 = UG('Mark Zuckerberg', 2017)
    g1 = Grad('Bill Gates')
    g2 = Grad ('Steve Wonziak')

    six000 = Grades()
    six000.addStudent(g1)
    six000.addStudent(ug2)
    six000.addStudent(ug1)
    six000.addStudent(g2)
    six000.addStudent(ug4)
    six000.addStudent(ug3)

    six000.addGrade(g1, 100)
    six000.addGrade(g2, 25)
    six000.addGrade(ug1, 95)
    six000.addGrade(ug2, 85)
    six000.addGrade(ug3, 75)

    print(gradeReport(six000))

    # add more grades
    six000.addGrade(g1, 90)
    six000.addGrade(g2, 45)
    six000.addGrade(ug1, 80)
    six000.addGrade(ug2, 75)
    print('=====================================')
    print(gradeReport(six000))
    print('=====================================')
    #sort list
    for s in six000.allStudents():
        print(s)
    print('=====================================')
    # data hiding aspect using student
    for s in six000.students:
        print(s)
