def newfn(s,a_ch_d,p,b_ch_d):
    res=0
    c=0
    tie=False
    for i in s:
        if i not in a_ch_d:
            print("ERROR")
            print("Restsrting the program.....")
            tie=True
            break
        res += (int(a_ch_d[i]))*(len(a_ch_d)**(len(s)-1-c))
        c+=1
    l1=[]
    while res!=0:
        a=res%p
        l1.append(a)
        res=int((res-a)/p)
    for i in reversed(l1):
        for x,y in b_ch_d.items():
            if i==y:
                print(x,end="")
    print("")
    return tie
octal={"0":"000", "1":"001","2":"010","3":"011","4":"100","5":"101","6":"110","7":"111"}
hexd={"0":"0000", "1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000", "9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}   
binarr={"0":0,"1":1}
hd={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15}
dec={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
oct={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7}
mix={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"A":10,"B":11,"C":12,"D":13,"E":14,"F":15,"G":16,"H":17,"I":18,"J":19,"K":20,"L":21,"M":22,"N":23,"O":24,"P":25,"Q":26,"R":27,"S":28,"T":29,"U":30,"V":31,"W":32,"X":33,"Y":34,"Z":35}
h=1
while h!=0:
    print("-------------------------------------------------------------------------------------------------------")
    print("1.Convert Decimal to Binary")
    print("2.Convert Decimal to Hexadecimal")
    print("3.Convert Decimal to Octal")
    print("4.Convert Binary to Decimal")
    print("5.Convert Binary to Hexadecimal")
    print("6.Convert Binary to Octal")
    print("7.Convert Hexadecimal to Decimal")
    print("8.Convert Hexadecimal to Binary")
    print("9.Convert Hexadecimal to Octal")
    print("10.Convert Octal to Decimal")
    print("11.Convert Octal to Binary")
    print("12.Convert Octal to Hexadecimal")
    print("13.Convert Radix-A to Radix-B")
    print("14.Quit")
    print("-------------------------------------------------------------------------------------------------------")
    m=int(input("ENTER YOUR CHOICE (input choice no. only!) : "))
    if m==14:
        h=0
    elif m==13:
        print("-------------------------------------------------------------------------------------------------------")
        print("Note-> We will use standard set of characters")
        print("-------------------------------------------------------------------------------------------------------")
        n=int(input("A(<=36) (Radix no.) : "))
        p=int(input("B(<=36) (Radix no.) : "))
        mix_1=dict()
        mix_2=dict()
        count=0
        for i in mix:
            if count==n:
                break
            mix_1[i]=mix[i]
            count+=1
        count=0
        for i in mix:
            if count==p:
                break
            mix_2[i]=mix[i]
            count+=1
        s=input("ENTER A NUMBER of radix A : ")
        tie=newfn(s,mix_1,p,mix_2)
        if tie ==False:
            print("-------------------------------------------------------------------------------------------------------")
            print("Extra-Content-Warning")
            s112=input("Note-> If you would like to give your own character set or would like to go beyond 36 radix then Enter \"Yes\" else Enter \"No\" : ")
            print("-------------------------------------------------------------------------------------------------------")
            if s112=="No":
                pass
            elif s112=="Yes":
                n=int(input("A (Radix no.): "))
                a_ch_d=dict()
                print("Enter the all the digits of Radix A in order of increasing values seperated by space")
                a_ch=[str(i) for i in input().split()]
                p=int(input("B (Radix no.): "))
                print("Enter the all the digits of Radix B in order of increasing values seperated by space")
                b_ch=[str(i) for i in input().split()]
                c=0
                for i in a_ch:
                    a_ch_d[i]=c
                    c+=1
                b0=False
                if len(a_ch)!=n or len(b_ch)!=p:
                    b0=True
                    print("ERROR")
                    print("RESTARTING THE PROGRAM...")
                if b0==False:
                    s=input("ENTER A NUMBER of radix A : ")
                    res=0
                    c=0
                    for i in s:
                        if i not in a_ch_d:
                            print("ERROR")
                            print("Restsrting the program.....")
                            break
                        res += (int(a_ch_d[i]))*(len(a_ch_d)**(len(s)-1-c))
                        c+=1
                    l1=[]
                    while res!=0:
                        a=res%p
                        t=b_ch[a]
                        l1.append(t)
                        res=int((res-a)/p)
                    for i in reversed (l1):
                        print(i,end="")
                    print("")
            else:
                print("Wrong input")
                print("ERROR")
                print("Restsrting the program.....")
    elif m==1:
        s=input("ENTER A NUMBER (whose radix = 10) ")
        newfn(s,dec,2,binarr)
    elif m==2:
        s=input("ENTER A NUMBER (whose radix = 10) ")
        newfn(s,dec,16,hd)
    elif m==3:
        s=int(input("ENTER A NUMBER (whose radix = 10) "))
        newfn(s,dec,8,oct)
    elif m==4:
        s=input("ENTER A NUMBER (whose radix = 2) ")
        newfn(s,binarr,10,dec)
    elif m==5:
        s=input("ENTER A NUMBER (whose radix = 2) ")
        newfn(s,binarr,16,hd)
    elif m==6:
        s=input("ENTER A NUMBER (whose radix = 2) ")
        newfn(s,binarr,8,oct)
    elif m==7:
        newfn(s,hd,10,dec)
    elif m==8:
        s=input("ENTER A NUMBER (whose radix = 16) ")
        res=str()
        for i in s:
            if i not in hexd:
                print("ERROR")
                print("Restsrting the program.....")
                break
            res += hexd[i]
        print(res)
    elif m==9:
        s=input("ENTER A NUMBER (whose radix = 16) ")
        newfn(s,hd,8,oct)
    elif m==10:
        s=input("ENTER A NUMBER (whose radix = 8) ")
        newfn(s,oct,10,dec)
    elif m==11:
        s=input("ENTER A NUMBER (whose radix = 8) ")
        res=str()
        for i in s:
            if i not in octal:
                print("ERROR")
                print("Restsrting the program.....")
                break
            res += octal[i]
        print(res)
    elif m==12:
        s=input("ENTER A NUMBER (whose radix = 8) ")
        newfn(s,oct,16,hd)
    else:
        print("Wrong input")
        print("ERROR")
        print("Restsrting the program.....")