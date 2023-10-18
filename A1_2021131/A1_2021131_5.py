def vifn(f):
    ldef=[]
    num=f
    while num!=0:
        lm=num%10
        ldef.append(lm)
        num=int(num/10)
    return ldef
def getReverse(f):
    l1=[]
    num=f
    count=0
    while num!=0:
        lm=num%10
        l1.append(lm)
        num=int(num/10)
        count=count+1
    rev=0
    x=0
    for i in l1:
        x=x+1
        rev= rev + i*(10**(count-x))
    return rev
def findDigitSum(f):
    s=0
    l1=[]
    l1=vifn(f)
    for i in l1:
        s=s + i
        if (-1)<s<10:
            an=s
        else:
            an=findDigitSum(s)
    return s
def findSquareDigitSum(f):
    s=0
    l1=[]
    l1=vifn(f)
    for i in l1:
        s=s + i**2
    if (-1)<s<10:
        an=s
    else:
        an=findSquareDigitSum(s)
    return an
def checkPalindrome(f):
    m=getReverse(f)
    if m==f:
        an=True
    else:
        an=False
    return an
def checkNarcissistic(f):
    ldef=[]
    num=f
    count=0
    while num!=0:
        lm=num%10
        ldef.append(lm)
        num=int(num/10)
        count= count + 1
    s=0
    for i in ldef:
        s=s + i**(count)
    if s== f:
        an=True
    else:
        an=False
    return an
i=1
while i!=0:
    print("-------------------------------------------------------------------------------------------------------")
    print("1.Find the reverse of the number")
    print("2.Check whether a number is a palindrome or not")
    print("3.Check whether a number is a Narcissistic or not")
    print("4.Find the sum of the digits of the number")
    print("5.Find the sum of squares of digits of a number")
    print("6.Select 6 to exit the application")
    print("-------------------------------------------------------------------------------------------------------")
    m=int(input("ENTER YOUR CHOICE (input choice no. only!) : "))
    if m==6:
        i=0
    else:
        n=int(input("ENTER A NUMBER : "))
        if n>(-1):
            if m==1:
                ans=getReverse(n)
                print(ans)
            elif m==2:
                ans=checkPalindrome(n)
                print(ans)
            elif m==3:
                ans=checkNarcissistic(n)
                print(ans)
            elif m==4:
                ans=findDigitSum(n)
                print(ans)
            elif m==5:
                ans=findSquareDigitSum(n)
                print(ans)
            else:
                print("ERROR")
                print("Restsrting the program.....")
        else:
            print("Wrong input")
            print("ERROR")
            print("Restsrting the program.....")