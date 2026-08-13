class student:
    def __init__(self, name, rollno):
        self.name=name
        self.rollno=rollno 
        self.__marks=[]
    def setmarks(self, marks):
        for mark in marks:
            if mark<0 or mark>100:
                print("MarK Invalid")
                return 
        self.__marks=marks 
    def total(self):
        tot=0
        for mark in self.__marks:
            tot+=mark 
        print(tot)
    def average(self):
        avg=0
        for mark in self.__marks:
            avg+=mark 
        print(avg/5)

s1=student("Shruti",80)
s1.setmarks([50,40,67,30,100])
s2=student("Srinithi",90)
s2.setmarks([50,607,803,50,87])
s3=student("Sarah",100)
print(s1.total())
print(s2.average())
        
