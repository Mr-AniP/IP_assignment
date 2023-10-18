def find_k():
    no=True
    x=int(input("x : "))
    y=int(input("y : "))
    z=int(input("z : "))
    a= ((2*y)-z)/x
    b= (x + z)/(2*y)
    c= ((2*y)-x)/z
    if a==1 and b==1 and c==1:
        print("x,y,z forms an AP")
        no=False
    else:
        if a%1==0:
            print("YES")
            print("x is multiplied by ",a)
            no=False
        elif b%1==0:
            print("YES")
            print("y is multiplied by ",b)
            no=False
        elif c%1==0:
            print("YES")
            print("z is multiplied by ",c)
            no=False
    if no==True:
        print("NO")
find_k()