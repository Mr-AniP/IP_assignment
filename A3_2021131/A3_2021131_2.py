costomerlist=[]
class LaundryService:
    def __init__(self,name,contact,email,type_cloth,brandval,season):
        if name not in costomerlist:
            costomerlist.append(name)
        self.id=1+costomerlist.index(name)
        self.name=name
        self.contact=contact
        self.mail=email
        self.type=type_cloth
        self.brand=brandval
        self.season=season
    def customerDetails(self):
        print("Laundry Services by DHOBHIWALA")
        print("")
        print("The details are as follows -->")
        print("")
        print("Customer ID : ",self.id)
        print("Customer's Name : ",self.name)
        print("Customer's Contact Number : ",self.contact)
        print("Customer's e-mail id: ",self.mail)
        print("Type of Cloth : ",self.type)
        print("Branded or not : "+ ("Branded" if self.brand==True else "Unbranded"))
    def calculateCharge(self):
        if self.type=="Cotton":
            c=50
        elif self.type=="Silk":
            c=30
        elif self.type=="Woolen":
            c=90
        elif self.type=="Polyester":
            c=20
        else:
            c=0
        c= (1.5*c) if self.brand==True else c
        c= (c/2) if self.season=="Winter" else (2*c) 
        return c
    def findDetails(self):
        self.customerDetails()
        c=self.calculateCharge()
        print("Total Charge : ",c)
        print("To be returned in 4 days!"if c>200 else "To be returned in 7 days!")
def main_execute():
    na=input("Name of customer : ")
    co=int(input("Contact of customer : "))
    ma=input("Email of customer : ")
    tc=input("Type of cloth : ")
    b=bool(int(input("Branded? : ")))
    s=input("Season : ")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
    clo_wash=LaundryService(na,co,ma,tc,b,s)
    clo_wash.findDetails()
    print("")
    print("Thank you for using our services")
    print("---------------------------------------------------------------------------------------------------------------------------------------------------")
ifg=1
while ifg!=0:
    print("Welcome to Laundry Services by DHOBHIWALA")
    print("1.Continue")
    print("2.Quit")
    print("*-#-#-*")
    n=int(input("Enter your choice : "))
    print("*-#-#-*")
    if n==1:
        main_execute()
        
    elif n==2:
        ifg=0
        print("Exiting...")
        print("Thank you for using our services")
    else:
        print("ERROR")
        print("Wrong input")
        print("Restarting")    