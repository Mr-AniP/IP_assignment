i=1
while i!=0:
    print("-------------------------------------------------------------------------------------------------------")
    print("1.Display Specific Word Count")
    print("2.Display Unique Words")
    print("3.Display all Word Counts")
    print("4.Replace Word")
    print("5.Quit")
    print("-------------------------------------------------------------------------------------------------------")
    m=int(input("ENTER YOUR CHOICE (input choice no. only!) : "))
    if m==5:
        i=0
    else:
        if m==1:
            n=input("ENTER THE WORD : ")
            with open("A2_2021131/Data/question1_input.txt",'r', encoding='utf-8') as f:
                c=0
                lines=f.readlines()
                for i in lines:
                    l1=[ str(g.strip())for g in i.split()]
                    if n in l1:
                        c+=l1.count(n.strip())
                if c!=0:
                    print("Wold count: ",c)
                else:
                    print("Word does not exist")
        elif m==2:
            with open("A2_2021131/Data/question1_input.txt",'r', encoding='utf-8') as f:
                l2=[]
                lines=f.readlines()
                for i in lines:
                    l1=[ str(g.strip())for g in i.split()]
                    l2+=l1
                l3=set(l2)
                print("Unique words :")
                print(*l3, sep=" ; ")
        elif m==3:
            print("Word counts :")
            with open("A2_2021131/Data/question1_input.txt",'r', encoding='utf-8') as f:
                l2=[]
                lines=f.readlines()
                for i in lines:
                    l1=[ str(h.strip())for h in i.split()]
                    l2+=l1
                l3=set(l2)
                for xz in l3:
                    c=0
                    for i in lines:
                        l1=[ str(g.strip())for g in i.split()]
                        if xz in l1:
                            c+=l1.count(xz.strip())
                    print(xz,":",c)
        elif m==4:
            n=input("Enter word to be replaced : ")
            tobe=input("Enter word that would replace it : ")
            line1=[]
            with open("A2_2021131/Data/question1_input.txt",'r', encoding='utf-8') as f:
                c=0
                lines=f.readlines()
                for i in lines:
                    l1=[ str(g.strip())for g in i.split()]
                    a=""
                    for h in range(len(l1)):
                        if l1[h]==n:
                            l1[h]=tobe
                    a=" ".join(l1)
                    xyz="\n"
                    a=a+xyz
                    line1.append(a)
            with open("A2_2021131/Data/question1_input.txt",'w', encoding='utf-8') as f:
                f.writelines(line1)
            print("Replaced Successfully!!")
        else:
            print("Wrong input")
            print("ERROR")
            print("Restsrting the program.....")