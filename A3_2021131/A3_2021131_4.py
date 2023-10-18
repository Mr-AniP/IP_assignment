class Person():
    def __init__(self,a,b,c):
        self.fn=a
        self.ln=b
        self.a=c
    def object_info(self):
        print(str(self.fn)+" "+str(self.ln)+" "+str(self.a))
def sort_attribute(p,pep):
    tan=1
    if p=="Firstname":
        def f(l):
            return l.fn
        pep.sort(key=f)
    elif p=="Lastname":
        def g(l):
            return l.ln
        pep.sort(key=g)
    elif p=="Age":
        def h(l):
            return l.a
        pep.sort(key=h)
    else:
        print("Wrong Querry")
        tan=0
    if tan==1:
        for fgh in pep:
            fgh.object_info()
wer=1
while wer!=0:
    print("Welcome to the application !!")
    n,k=[int(i) for i in input("Enter space-seperated values of the no. of people enrolled and no. of queries : ").split()]
    p=[]
    for i in range(n):
        fn,ln,a=[jj for jj in input("Enter Firstname, Lastname and Age of Person "+str(i+1)+" in a space-seperated manner : ").split()]
        ob=Person(fn,ln,int(a))
        p.append(ob)
    qu=[]
    for i in range(k):
        q=input("Querry- "+str(i+1)+" : ")
        qu.append(q)
    for q in qu:
        sort_attribute(q,p)
    print("Thanks for using the Application !! ")
    def n2123():
        n123=input("If you wish to exit the Application then press \'Y\' else press \'N\' : ")
        if n123=="Y":
            return 1
        elif n123=="N":
            return 0
        else:
            print("Wrong Input")
            n123()
    wer=n2123()