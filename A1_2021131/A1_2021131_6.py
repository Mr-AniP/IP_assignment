l1=[2,-1]
tolerence=1e-7
epsilon=1e-14
def check_diff(f,l1):
    #we have used the fact that polynomial function is non- differentiable only for x tends to 0 that too only for a negative exponent of x 
    a=True
    m=True
    for i in l1:
        if i<0:
            m=False
        if i<1:
            if i%1==0 or i==0:
                if (-1)*epsilon < f < epsilon :
                    a=False
            elif i>0 and m==True:
                a=False
                print("We get the root as 0")
                break
            else:
                a=False
                break
    return a
def f(xn):
    s=0
    for i in l1:
        s = s + (xn**i)
    return s
def f_dif(xn):
    s=0
    for i in l1:
        s= s + i*(xn**(i-1))
    return s
xn=1
x0=2
no_return1=False
no_return2=False
while f(xn)!=0:
    a=check_diff(xn,l1)
    if a==False:
        for i in l1:
            if i<0:
                m=False
                if i<1:
                    if i%1==0 or i==0:
                        pass
                    elif i>0 and m==True:
                        pass
                    else :
                        print("We get the root as",xn)
        no_return1=True
        break
    if (-1)*epsilon < f_dif(xn) < epsilon:
        print("We get the root as",xn)
        no_return2=True
        break
    if (-1)*tolerence<(xn-x0)< tolerence:
        break
    x0=xn
    xn = xn - (f(xn)/f_dif(xn))
if no_return1==False and no_return2==False:
    print("We get the root as",xn)        