def val(h,grammy):
    val=h*grammy
    return val
p,q=[int(i) for i in input().split()]
m,n=[int(i) for i in input().split()]
l=[]
stoppro=False
for i in range(m):
    a=input()
    if len(a)==n:
        l.append(a)
    else:
        print("Wrong input")
        print("ERROR")
        stoppro=True
        break
if stoppro!=True:
    count=0
    c=0
    a="0"*(n)
    l1=[]
    reput_d=0
    reput_s=0
    for i in l:
        k=""
        for j in range(n):
            if a[j]=="D":
                k+="D"
            elif a[j]=="S":
                k+="S"
            elif i[j]=="1":
                    if count%2==0:
                        k+="D"
                        count+=1
                        reput_d+=val(m-c,p)
                        q+=1
                        p+=1
                    else:
                        k+="S"
                        count+=1
                        reput_s+=val(m-c,q)
                        p+=1
                        q+=1
            else:
                k+=i[j]
        c+=1
        a=k
        l1.append(k)
    print()
    print(reput_d,reput_s)
    for i in l1:
        print(i)