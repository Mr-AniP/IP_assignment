x="Apple"
y="App"
def playStr(x,y):
    l1=['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z','B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z']
    n=""
    l2=[]
    for i in x:
        if i in l2:
             pass
        else:
            l2.append(i)
    a1=0
    e1=0
    i1=0
    u1=0
    o1=0
    co1=0
    for f in l2:
        if f=="a" or f=="A":
            a1=a1+1
        elif f=="e" or f=="E":
            e1=e1+1
        elif f=="i" or f=="I":
            i1=i1+1
        elif f=="u" or f=="U":
            u1=u1+1
        elif f=="a" or f=="A":
            o1=o1+1
        elif f in l1:
            co1=co1+1
        else:
            print("error")
            break
    l2=[]
    for g in y:
        if g in l2:
             pass
        else:
            l2.append(g)
    a2=0
    e2=0
    i2=0
    u2=0
    o2=0
    co2=0
    for h in l2:
        if h=="a" or h=="A":
            a2=a2+1
        elif h=="e" or h=="E":
            e2=e2+1
        elif h=="i" or h=="I":
            i2=i2+1
        elif h=="u" or h=="U":
            u2=u2+1
        elif h=="a" or h=="A":
            o2=o2+1
        elif h in l1:
            co2=co2+1
        else:
            print("error")
            break
    if a1!=0 and e1!=0 and i1!=0 and u1!=0 and o1!=0 :
        print(True)
    else:
        print(False)
    a=""
    for j in x:
        if y==a:
            q2=True
            break
        a = a + j
    if q2==True:
        print(True)
    else:
        print(False)
    print(co2) 
playStr(x,y)