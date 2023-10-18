def fn1(i):
    return i.cgpa
def cgpa(m):
    g=float(input(m))
    try:
        assert 0<=g<=10, "CGPA==Invalid"
        return g
    except:
        print("The cgpa is invalid")
        return cgpa("Re-enter it : ")
class Student():
    def __init__(self,n,c,b):
        self.name=n
        self.cgpa=c
        self.branch=b
        self.isPlaced=False
    def isEligible(self,c):
        if self.isPlaced==False and self.branch in c.branches and self.cgpa>=c.requiredcgpa:
            print(f"Student {self.name} is eligible for Company {c.name}")
            return True
        else:
            print(f"Student {self.name} is not eligible for Company {c.name}")
            return False
    def apply(self,c):
        c.appliedStudents.append(self)
    def getPlaced(self):
        self.isPlaced=True
class Company():
    def __init__(self,n,rc,b,p):
        self.name=n
        self.requiredcgpa=rc
        self.branches=b
        self.positionOpen=p
        self.appliedStudents=[]
        self.hired=[]
        self.applicationOpen=True
    def closeApplication(self):
        self.applicationOpen=False
        print(f"The following students were hired by the company {self.name}")
        for i in self.hired:
            print(i.name)
        print(f"The company {self.name} hired {len(self.hired)} students")
    def hire(self):
        if self.applicationOpen==True:
            self.appliedStudents.sort(reverse=True,key=fn1)
            c=0
            for i in self.appliedStudents:
                if c<self.positionOpen:
                    self.hired.append(i)
                    c+=1
                    i.getPlaced()
                else:
                    break
            self.closeApplication()
n=int(input("ENTER NO. OF STUDENTS : "))
print()
stu=[]
for hgt in range(n):
    nam=input("Enter Name of student "+str(hgt+1)+" : ")
    g=cgpa("Enter Cgpa of student "+str(hgt+1)+" : ")
    bran=input("Enter Branch of student "+str(hgt+1)+" : ")
    print()
    s=Student(nam,g,bran)
    stu.append(s)
n=int(input("ENTER NO. OF Companies : "))
for hgt in range(n):
    print()
    nam=input("Enter Name of the Comapny "+str(hgt+1)+" : ")
    g=cgpa("Enter Required Cgpa of the Comapny "+str(hgt+1)+" : ")
    bran=[i for i in input("Enter space-seperated Branches of Company "+str(hgt+1)+" : ").split()]
    po=int(input("Enter number of Positions Open of the Comapny "+str(hgt+1)+" : "))
    print()
    s=Company(nam,g,bran,po)
    for i in stu:
        if i.isEligible(s)==True:
            i.apply(s)
    print()
    s.hire()