import math
# In this file we have coded our A2_2021131.py again but in a different way
t4=[0,0,0,1]
c112=0
def l1Generator(x):
    l1=[1 for i in x]
    return l1
def matmul(A,B):
    C=[]
    for i in range(len(A)):
        dlp=[]
        for j in range(len(B[0])):
            s=0
            for k in range(len(A[i])):
                s+= A[i][k] * B[k][j]
            dlp.append(s)
        C.append(dlp)
    return C
def scale(x,y,z,sx,sy,sz):
    t1=[sx,0,0,0]
    t2=[0,sy,0,0]
    t3=[0,0,sz,0]
    l=[t1,t2,t3,t4]
    l1=l1Generator(x)
    var=[x,y,z,l1]
    res=matmul(l,var)
    return res[0],res[1],res[2]
def translate(x,y,z,tx,ty,tz):
    t1=[1,0,0,tx]
    t2=[0,1,0,ty]
    t3=[0,0,1,tz]
    l=[t1,t2,t3,t4]
    l1=l1Generator(x)
    var=[x,y,z,l1]
    res=matmul(l,var)
    return res[0],res[1],res[2]
def rotate(x,y,z,axis,phi):
    cos=math.cos(phi)
    sin=math.sin(phi)
    if axis=="x":
        t1=[1,0,0,0]
        t2=[0,cos,((-1)*sin),0]
        t3=[0,sin,cos,0]
    elif axis=="y":
        t2=[0,1,0,0]
        t1=[cos,0,sin,0]
        t3=[((-1)*sin),0,cos,0]
    else:
        t3=[0,0,1,0]
        t1=[cos,((-1)*sin),0,0]
        t2=[sin,cos,0,0]
    l=[t1,t2,t3,t4]
    l1=l1Generator(x)
    var=[x,y,z,l1]
    res=matmul(l,var)
    return res[0],res[1],res[2]
if __name__=="__main__":
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
    for i in q:
        if i[0]=="S":
            xn,yn,zn=scale(x_lst,y_lst,z_lst,float(i[1]),float(i[2]),float(i[3]))
        elif i[0]=="T":
            xn,yn,zn=translate(x_lst,y_lst,z_lst,float(i[1]),float(i[2]),float(i[3]))
        else:
            xn,yn,zn=rotate(x_lst,y_lst,z_lst,i[1],float(i[2]))
        l112.append(("Testcase-"+str(c112+1)+" Output\n"))
        l112.append(("x\'="+str(xn)+"\n"))
        l112.append(("y\'="+str(yn)+"\n"))
        l112.append(("z\'="+str(zn)+"\n"))
        c112+=1
    with open("A3_2021131/A2_2021131_2_in_out_store.txt",'w') as f:
        f.writelines(l112)