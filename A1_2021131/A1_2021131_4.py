def Fn(b1,b2,b3):
    a= (b1 and not b1)
    return a
l1=[True, False]
satisfy=False
for b1 in l1:
    for b2 in l1:
        for b3 in l1:
            if Fn(b1,b2,b3)==True :
                satisfy=True
                print("Satisfiable")
                print(b1,b2,b3)
                break
if satisfy==False:
    print("Unsatisfiable")