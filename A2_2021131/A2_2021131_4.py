set_1={"A","B","C","D"}
with open("A2_2021131/Data/Q4_data(testcases)/Admin/AnswerKey.txt",'r',encoding="utf-8") as f3:
            lines=f3.readlines()
            l3=dict()
            for i in lines:
                c=0
                for j in i.split():
                    if c==0:
                        key=int(j)
                    else:
                        val=j
                    c+=1
                l3[key]=val
with open("A2_2021131/Data/Q4_data(testcases)/Admin/RegisteredStudents.txt",'r',encoding="utf-8") as f1:
    register_lines=f1.readlines()
    for i in register_lines:
        l1=[]
        c=0
        for j in reversed(i.split()):
            if c==0:
                l1.append(int(j))
            else:
                l1.append(j)
            c+=1
        student_n=" ".join(l1[1:])
        file="A2_2021131/Data/Q4_data(testcases)/Student/"+student_n+"_"+str(l1[0])+".txt"
        with open(file,'r',encoding="utf-8") as f2:
            lines=f2.readlines()
            lscore=[]
            for i in lines:   
                l2=dict()
                c=0
                score=0
                for j in i.split():
                    if c==0:
                        key=int(j)
                    else:
                        val=j
                    c+=1
                l2[key]=val
                for j in l2:
                    if l2[j]=="-":
                        pass
                    elif l2[j]==l3[j]:
                        score+=4
                    else:
                        if l2[j] in set_1:
                            score-=1
                        else:
                            print("Error")
                            print(student_n," -> not a valid option")
                            retreat=True
                            break
                lscore.append(score)
            a=sum(lscore)
            zf5=student_n+" "+str(l1[0])+" "+str(a)+"\n"
            with open("A2_2021131/Data/Q4_data(testcases)/Admin/FinalReport.txt",'a',encoding="utf-8") as f4:
                f4.write(zf5)
    print("Generated FinalReport.txt successfully!!")