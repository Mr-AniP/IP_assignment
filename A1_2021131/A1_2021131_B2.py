print("Please note : that you have to input d-vector and e-vector line by line and output(x1,y1,z1) will be printed as a list[x1, y1, z1]")
e=[]
ex=float(input("ex : "))
e.append(ex)
ey=float(input("ey : "))
e.append(ey)
ez=float(input("ez : "))
e.append(ez)
d=[]
dx=float(input("dx : "))
d.append(dx)
dy=float(input("dy : "))
d.append(dy)
dz=float(input("dz : "))
d.append(dz)
x0=float(input("x0 : "))
y0=float(input("y0 : "))
z0=float(input("z0 : "))
r=float(input("R : "))
def p(t,e,d):
    a=[]
    x = e[0] + t*d[0]
    y = e[1] + t*d[1]
    z = e[2] + t*d[2]
    a.append(x)
    a.append(y)
    a.append(z)
    return a
def sphere(a,x0,y0,z0,r):
    c=(((a[0])-x0)**2) + (((a[1])-y0)**2) + (((a[2])-z0)**2)
    if c == r**2 :
        b=0
    elif c>r**2 :
        b=1
    else :
        b=-1
    return b
count=0
if dx==0 and dy==0 and dz==0:
    coun=count+1
    m=[]
    m==[0.0,0.0,0.0]
    print(m)
else:
    for t in range(10002):
        m=p(t,e,d)
        n=sphere(m,x0,y0,z0,r)
        if n==0:
            if m==[0.0,0.0,0.0]:
                print(m)
                count=count+1
                continue
            else:
                print(m)
                count=count+1
        m=p((-t),e,d)
        n=sphere(m,x0,y0,z0,r)
        if n==0:
            if m==[0.0,0.0,0.0]:
                print(m)
                count=count+1
                continue
            else:
                print(m)
                count=count+1
if count==0:
    print("No point of intersection")