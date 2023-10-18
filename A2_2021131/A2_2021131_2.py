import math
n=int(input())
x_lst=[float(i) for i in input().split()]
y_lst=[float(i) for i in input().split()]
z_lst=[float(i) for i in input().split()]
old_1=[]
for i in range(n):
    old_1.append(1)
l1=[x_lst,y_lst,z_lst,old_1]
loopku=int(input())
q=[]
l112=[]
l112.append(("Input\n"))
l112.append(("n="+str(n)+"\n"))
l112.append(("x="+str(x_lst)+"\n"))
l112.append(("y="+str(y_lst)+"\n"))
l112.append(("z="+str(z_lst)+"\n"))
l112.append(("q="+str(loopku)+"\n"))
for i in range(loopku):
    z=[f for f in input().split()]
    q.append(z)
    l112.append((str(z)+"\n"))
t4=[0,0,0,1]
c112=0
for i in q:
    if i[0]=="S":
        t1=[float(i[1]),0,0,0]
        t2=[0,float(i[2]),0,0]
        t3=[0,0,float(i[3]),0]
    elif i[0]=="T":
        t1=[1,0,0,float(i[1])]
        t2=[0,1,0,float(i[2])]
        t3=[0,0,1,float(i[3])]
    else:
        cos=math.cos(float(i[2]))
        sin=math.sin(float(i[2]))
        if i[1]=="x":
            t1=[1,0,0,0]
            t2=[0,cos,((-1)*sin),0]
            t3=[0,sin,cos,0]
        elif i[1]=="y":
            t2=[0,1,0,0]
            t1=[cos,0,sin,0]
            t3=[((-1)*sin),0,cos,0]
        else:
            t3=[0,0,1,0]
            t1=[cos,((-1)*sin),0,0]
            t2=[sin,cos,0,0]
    def lstmult(l1,l2,n):
        l3=[]
        for i in range(len(l1)):
            m=[]
            for f in l2[i]:
                sd=l1[i]*f
                m.append(sd)
            l3.append(m)
        l4=[]
        for i in range(n):
            s=0
            for f in l3:
                s+=f[i]
            l4.append(s)
        print(l4)
        return l4
    x2=lstmult(t1,l1,n)
    y2=lstmult(t2,l1,n)
    z2=lstmult(t3,l1,n)
    l112.append(("Testcase-"+str(c112+1)+" Output\n"))
    l112.append(("x\'="+str(x2)+"\n"))
    l112.append(("y\'="+str(y2)+"\n"))
    l112.append(("z\'="+str(z2)+"\n"))
    c112+=1
with open("A2_2021131/A2_2021131_2_in_out_store.txt",'w') as f:
    f.writelines(l112)