def check_prime(f):
    count=0
    check=False
    if f>1 and f%1==0:
        for i in range(1,f+1):
            a=f%i
            if a==0:
                count=count+1
        if count==2:
            check=True
        return check
    else:
        print("wrong input")
def sum_of_digits(f):
    if f>0:
        f=f
    else:
        f=(-1)*f
    a=str(f)
    count=0
    for i in a:
        if i!=".":
            count=count+1 
    c1=0
    num = f
    while num!=0:
        c1=c1+1
        num=int(num/10)
    s=0
    f=f * (10**(count-c1))
    while f!=0:
        a=f%10
        s=s+a
        f=int(f/10)
    return s
def sum_fibonacchi(f):
    s=0
    a1=1
    a2=1
    for i in range(1,f+1):
        a3=a2+a1
        s=s+a3
        a1=a2
        a2=a3
    return s
def collatz_cojecture(f):
    count=0
    while f!=1:
        count=count+1
        if f%2==0:
            f=f/2
        elif f%2==1:
            f= (3*f) +1
        else:
            print("wrong input")
            break
    return count
i=1
while i!=0:
    print("-------------------------------------------------------------------------------------------------------")
    print("1.Check whether a number is a prime number or not")
    print("2.Find the sum of the digits of the number")
    print("3.Find the sum of Fibonacchi series of n terms ")
    print("4.Implement collatz conjecture")
    print("5.Select 6 to exit the application")
    print("-------------------------------------------------------------------------------------------------------")
    m=int(input("ENTER YOUR CHOICE (input choice no. only!) : "))
    if m==5:
        i=0
    elif m==3:
        n=int(input("ENTER THE NUMBER OF TERMS : "))
        s=sum_fibonacchi(n)
        print("Sum = ",s)
    elif m==1 or m==4 :
        n=int(input("ENTER A NUMBER : "))
        if m==1:
            s=check_prime(n)
            print(s)
        else:
            s=collatz_cojecture(n)
            print("No. of steps = ",s)
    elif m==2:
        n=float(input("ENTER A NUMBER : "))
        s=sum_of_digits(n)
        print("Sum = ",s)
    else:
        print("Wrong input")
        print("Restarting")