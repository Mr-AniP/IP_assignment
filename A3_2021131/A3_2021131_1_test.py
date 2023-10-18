import A3_2021131_1 as t
def test_matmul(A,B,true_C):
    c=t.matmul(A,B)
    try:
        assert (c==true_C) , "False"
        v=True
    except:
        v=False
    return v
def test_scale(x,y,z,sx,sy,sz,true_x,true_y,true_z):
    a,b,c=t.scale(x,y,z,sx,sy,sz)
    try:
        assert (a==true_x and b==true_y and c==true_z) , "False"
        v=True
    except:
        v=False
    return v
def test_translate(x,y,z,tx,ty,tz,true_x,true_y,true_z):
    a,b,c=t.translate(x,y,z,tx,ty,tz)
    try:
        assert (a==true_x and b==true_y and c==true_z) , "False"
        v=True
    except:
        v=False
    return v
def test_rotate(x,y,z,axis,phi,true_x,true_y,true_z):
    a,b,c=t.rotate(x,y,z,axis,phi)
    try:
        assert (a==true_x and b==true_y and c==true_z) , "False"
        v=True
    except:
        v=False
    return v
i=1
while i!=0:
    print("--------------------------------------------------------------------------------------------------------------------------")
    print("Welcome to our application!!")
    print()
    print("You may chosse to do any of the following ->")
    print("1. Run test_matmul")
    print("2. Run test_scale")
    print("3. Run test_translate")
    print("4. Run test_rotate")
    print("5. Exit Application")
    print()
    mnm=int(input("Enter choice no. : "))
    if mnm==5:
        i=0
        print("Exiting...")
    elif mnm==1:
        a=int(input("No. of rows of A : ")) 
        assert a>0 ,"It can\'t be negative"
        print("Input A in a matrix form ")
        A=[]
        for nb in range(a):
            A.append([float(f) for f in input().split()])
        a=int(input("No. of rows of B : ")) 
        assert a>0 ,"It can\'t be negative"
        print("Input B in a matrix form ")
        B=[]
        for nb in range(a):
            B.append([float(f) for f in input().split()])
        a=int(input("No. of rows of true_C : ")) 
        assert a>0 ,"It can\'t be negative"
        print("Input true_C in a matrix form ")
        T_c=[]
        for nb in range(a):
            T_c.append([float(f) for f in input().split()])
        print(test_matmul(A,B,T_c))
    elif mnm==2:
        n=int(input("Input the value of n (dimension of space) : "))
        x_lst=[float(i) for i in input("x : ").split()]
        y_lst=[float(i) for i in input("y : ").split()]
        z_lst=[float(i) for i in input("z : ").split()]
        sx=float(input("Sx : "))
        sy=float(input("Sy : "))
        sz=float(input("Sz : "))
        x_t=[float(i) for i in input("true_x : ").split()]
        y_t=[float(i) for i in input("true_y : ").split()]
        z_t=[float(i) for i in input("true_z : ").split()]
        print(test_scale(x_lst,y_lst,z_lst,sx,sy,sz,x_t,y_t,z_t))
    elif mnm==3:
        n=int(input("Input the value of n (dimension of space) : "))
        x_lst=[float(i) for i in input("x : ").split()]
        y_lst=[float(i) for i in input("y : ").split()]
        z_lst=[float(i) for i in input("z : ").split()]
        tx=float(input("Tx : "))
        ty=float(input("Ty : "))
        tz=float(input("Tz : "))
        x_t=[float(i) for i in input("true_x : ").split()]
        y_t=[float(i) for i in input("true_y : ").split()]
        z_t=[float(i) for i in input("true_z : ").split()]
        print(test_translate(x_lst,y_lst,z_lst,tx,ty,tz,x_t,y_t,z_t))
    elif mnm==4:
        n=int(input("Input the value of n (dimension of space) : "))
        x_lst=[float(i) for i in input("x : ").split()]
        y_lst=[float(i) for i in input("y : ").split()]
        z_lst=[float(i) for i in input("z : ").split()]
        axis=input("Axis : ")
        phi=float(input("phi : "))
        x_t=[float(i) for i in input("true_x : ").split()]
        y_t=[float(i) for i in input("true_y : ").split()]
        z_t=[float(i) for i in input("true_z : ").split()]
        print(test_rotate(x_lst,y_lst,z_lst,axis,phi,x_t,y_t,z_t))
    else:
        print("Wrong input")
        print("Restarting...")
print("Thank you for using our Application")