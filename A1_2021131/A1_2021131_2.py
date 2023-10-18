import math
pi=math.pi
print("Started....")
n=int(input("Enter no. of students : "))
for i in range(n):
    print("Student no. ",i+1 ,"Get ready! It's your turn")
    def menu(f):
        type_shape=input("Enter Geometrical Dimension (2D or 3D) : ")
        if type_shape =="2D":
            print("--------------------------------------------#_2D-Menu_#--------------------------------------------")
            print("1.SQUARE")
            print("2.RECTANGLE")
            print("3.RHOMBUS")
            print("4.PARALLELOGRAM")
            print("5.CIRCLE")
            print("6.!GO TO PREVIOUS STEP!--CHOSE GEOMETRIC DIMENSION AGAIN")
            print("7.!!!STOP!!!--GO TO NEXT STUDENT")
            print("8.!!!TERMINATE!!!--END PROGRAM")
            print("")
            m=int(input("ENTER YOUR CHOICE (input choice no. only!) : "))
            if m== 5 :
                print("YOU HAVE CHOOSEN CIRCLE")
                r=float(input("Input the radius of the circle : "))
                p= pi*2*r
                a= pi*r*r
                print("Perimeter = ",p)
                print("Area = ",a)
                print("Thank you for using me")
            elif m==4 :
                print("YOU HAVE CHOOSEN PARALLELOGRAM")
                l=float(input("Input the length of the PARALLELOGRAM : "))
                b=float(input("Input the breadth of the PARALLELOGRAM : "))
                h=float(input("Input the height of the PARALLELOGRAM : "))
                p= 2*(l+b)
                a= b*h
                print("Perimeter = ",p)
                print("Area = ",a)
                print("Thank you for using me")
            elif m==3:
                print("YOU HAVE CHOOSEN RHOMBUS")
                a =float(input("Input the side of the RHOMBUS : "))
                d1=float(input("Input the diagnol-1 of the RHOMBUS : "))
                d2=float(input("Input the diagnol-2 of the RHOMBUS : "))
                p= 4*a
                a= d1*d2
                print("Perimeter = ",p)
                print("Area = ",a)
                print("Thank you for using me")
            elif m==2:
                print("YOU HAVE CHOOSEN RECTANGLE")
                l =float(input("Input the length of the RECTANGLE : "))
                b=float(input("Input the breadth of the RECTANGLE : "))
                p= 2*(l+b)
                a= l*b
                print("Perimeter = ",p)
                print("Area = ",a)
                print("Thank you for using me")
            elif m==1:
                print("YOU HAVE CHOOSEN SQUARE")
                s =float(input("Input the side of the SQUARE : "))
                p= 4*s
                a= s*s
                print("Perimeter = ",p)
                print("Area = ",a)
                print("Thank you for using me")
            elif m==6:
                print("Going back...")
                print("Student no. ",f+1 ,"Get ready! It's your turn")
                menu(f)
            elif m==7:
                print("Aborting the process...")
                print("Thank you for using me")
            elif m==8:
                ending=input("Are you sure (enter YES or No) : ")
                if ending=="YES":
                    print("Thank for using me")
                    print("Exiting.........")
                    con=True
                    return con
                else:
                    menu(f)
            else:
                print("ERROR")
                print("Wrong input")
                print("Restarting")
                print("Welcome again its your turn")
                menu(f)
        elif type_shape =="3D":
            print("--------------------------------------------#_3D-Menu_#--------------------------------------------")
            print("1.CUBE")
            print("2.CUBOID")
            print("3.RIGHT CIRCULAR CONE")
            print("4.HEMISPHERE")
            print("5.SPHERE")
            print("6.SOLID CYLINDER")
            print("7.HOLLOW CYLINDER")
            print("8.!GO TO PREVIOUS STEP!--CHOSE GEOMETRIC DIMENSION AGAIN")
            print("9.!!!STOP!!!--GO TO NEXT STUDENT")
            print("10.!!!TERMINATE!!!--END PROGRAM")
            print("")
            m=int(input("ENTER YOUR CHOICE (input choice no. only!) : "))
            if m== 1 :
                print("YOU HAVE CHOOSEN CUBE")
                s=float(input("Input the radius of the CUBE: "))
                csa=4*s*s
                tsa=6*s*s
                vol=s*s*s
                print("CSA : ",csa)
                print("TSA : ",tsa)
                print("VOLUME : ",vol)
                print("Thank you for using me")
            elif m==2 :
                print("YOU HAVE CHOOSEN CUBOID")
                l=float(input("Input the length of the CUBOID : "))
                b=float(input("Input the breadth of the CUBOID : "))
                h=float(input("Input the height of the CUBOID : "))
                csa=2*h*(l+b)
                tsa=2*(l*b + b*h +l*h)
                vol=l*b*h
                print("CSA : ",csa)
                print("TSA : ",tsa)
                print("VOLUME : ",vol)
                print("Thank you for using me")
            elif m==3:
                print("YOU HAVE CHOOSEN RIGHT CIRCULAR CONE")
                l =float(input("Input the slant height of the RIGHT CIRCULAR CONE : "))
                r=float(input("Input the radius of the RIGHT CIRCULAR CONE : "))
                h=float(input("Input the height of the RIGHT CIRCULAR CONE : "))
                csa=pi*r*l
                tsa=pi*r*(r+l)
                vol=(pi*r*r*h)/3
                print("CSA : ",csa)
                print("TSA : ",tsa)
                print("VOLUME : ",vol)
                print("Thank you for using me")
            elif m==4:
                print("YOU HAVE CHOOSEN HEMISPHERE")
                r =float(input("Input the radius of the HEMISPHERE: "))
                csa=2*r*r*pi
                tsa=3*r*r*pi
                vol=(r*r*r*2*pi)/3
                print("CSA : ",csa)
                print("TSA : ",tsa)
                print("VOLUME : ",vol)
                print("Thank you for using me")
            elif m==5:
                print("YOU HAVE CHOOSEN SPHERE")
                r =float(input("Input the radius of the SPHERE : "))
                csa=4*r*r*pi
                tsa=csa
                vol=(r*r*r*4*pi)/3
                print("CSA : ",csa)
                print("TSA : ",tsa)
                print("VOLUME : ",vol)
                print("Thank you for using me")
            elif m==6:
                print("YOU HAVE CHOOSEN SOLID CYLINDER")
                r=float(input("Input the radius of the SOLID CYLINDER : "))
                h=float(input("Input the height of the SOLID CYLINDER: "))
                csa=pi*r*h*2
                tsa=csa + 2*pi*r*r
                vol=pi*r*r*h
                print("CSA : ",csa)
                print("TSA : ",tsa)
                print("VOLUME : ",vol)
                print("Thank you for using me")
            elif m==7:
                print("YOU HAVE CHOOSEN HOLLOW CYLINDER")
                r1=float(input("Input the outer radius of the HOLLOW CYLINDER : "))
                r2=float(input("Input the inner radius of the HOLLOW CYLINDER: "))
                h=float(input("Input the height of the HOLLOW CYLINDER: "))
                csa=2*pi*h*(r1+r2)
                tsa= csa + pi*((r1*r1) -(r2*r2))*2
                vol=pi*((r1*r1) -(r2*r2))*h
                print("CSA : ",csa)
                print("TSA : ",tsa)
                print("VOLUME : ",vol)
                print("Thank you for using me")
            elif m==8:
                print("Going back...")
                print("Student no. ",f+1 ,"Get ready! It's your turn")
                menu(f)
            elif m==9:
                print("Aborting the process...")
                print("Thank you for using me")
            elif m==10:
                ending=input("Are you sure (enter YES or No) : ")
                if ending=="YES":
                    print("Thank for using me")
                    print("Exiting.........")
                    con=True
                    return con
                else:
                    menu(f)
            else:
                print("ERROR")
                print("Wrong input")
                print("Restarting")
                print("Welcome again its your turn")
                menu(f)
        else:
            print("ERROR")
            print("Wrong input")
            print("Restarting")
            print("Welcome again its your turn")
            menu(f)
    jin=menu(i)
    if jin==True:
        break
print("End of program")