from datetime import datetime
def con():
    m=input("Would you like to continue ? Y/N : ")
    if m=="N":
        return 0
    elif m=="Y":
        return 1
    else:
        print("Wrong input")
        print("Restarting")
        con()
print("BANK OF INDRAPRASTHA INSTITUTE OF INFORMATION TECHNOLOGY (IIITD)")
print()
print()
print("Welcome to the EMERGENCY FUNDS MANAGMENT BANK OF IIITD !!!!")
print()
N=input("ENTER YOUR USERNAME : ")
P=input("ENTER YOUR PASSWORD : ")
I=float(input("ENTER INITIAL AMOUNT AS STARTING BALANCE (IN RUPEES) : "))
l=dict()
class BankAccount():
    def __init__(self,n,p,ini):
        self.name=n
        self.password=p
        self.amt=ini
        l[n]=p
        s="A3_2021131/" + n + ".txt"
        with open(s,'w') as file123:
            pass
    def deposit(self,val):
        tmt=self.authenticate(0)
        if tmt==True:
            self.amt+=val
            s="A3_2021131/" + self.name + ".txt"
            with open(s,'a') as file123:
                file123.write(str(datetime.now())+"The amount of Rupees " + str(val) +" has been added Current balance -> "+ str(self.amt)+"\n")
    def withdraw(self,val):
        tmt=self.authenticate(0)
        if tmt==True:
            if self.amt>=val:
                self.amt-=val
                s="A3_2021131/" + self.name + ".txt"
                with open(s,'a') as file123:
                    file123.write(str(datetime.now())+"The amount of Rupees " + str(val) +" has been debited Current balance -> "+ str(self.amt)+"\n")
            else:
                print("Low balance!! Cannot be debited at this time!")
    def bankStatement(self):
        tmt=self.authenticate(0)
        if tmt==True:
            print()
            print("Hey "+str(self.name)+"! Your transactions history : ")
            print()
            s="A3_2021131/" + self.name + ".txt"
            with open(s,'r') as file123:
                l123=[f.strip() for f in file123.readlines()]
                for mnm in l123:
                    print(mnm) 
    def authenticate(self,c):
        p=input("Provide your secret password : ")
        if self.password==p:
            return True
        else:
            assert c<2,"Too many wrong attempts!!"
            return self.authenticate(c+1)
acc=BankAccount(N,P,I)
i=1
print()
print("----------------------------------------------------------------------------------------------------------------------------------------------")
print()
while i!=0:
    print("Select what you would intend to do : ")
    print()
    print("1.Deposit a sum into your account")
    print("2.Withdraw a sum from your account")
    print("3.Would like to see your Bank-Statement")
    print("4.Exit / Quit")
    print()
    n=int(input("ENTER CHOICE NO. : "))
    print()
    try:
        if n==4:
            print("Exiting the Application...")
            print()
            i=0
        elif n==1:
            amot=float(input("Provide the amount to be deposited (IN RUPEES) : "))
            if amot<0:
                raise Exception("Anount is negative")
            acc.deposit(amot)
            i=con()
            print()
        elif n==2:
            amot=float(input("Provide the amount to be withdrawn (IN RUPEES) : "))
            if amot<0:
                raise Exception("Anount is negative")
            acc.withdraw(amot)
            i=con()
            print()
        elif n==3:
            acc.bankStatement()
            print()
            i=con()
            print()
        else:
            print("No such choice")
            print("Restarting")
    except ValueError:
        print("No such choice")
        print("Enter only choice number")
        print("Restarting")
print("Thank you for using our bank application")
print("HAVE A NICE DAY")