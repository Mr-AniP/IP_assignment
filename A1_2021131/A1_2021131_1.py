s=input()
n=int(input())
if s=="Right-angled triangle":
    for i in range(n):
        for f in range(i+1):
            print(f+1,end='')
        print("")
elif s=="Isosceles triangle":
    if n%2==0:
        for i in range(n):
            x=(2*i)
            print((n-i)*" ",end="")
            for f in range(x+1):
                print(f+1,end='')
            print((n-i)*" ",end="")
            print("") 
    else:
        print("ERROR")
elif s=="Kite" :
    if n%2==0:
        for i in range(n):
            x=(2*i)
            print((n-i)*" ",end="")
            for f in range(x+1):
                print(f+1,end='')
            print((n-i)*" ",end="")
            print("")
            a=n
        while a>(-1):
            if a!=(n-1) and a!=n :
                x=(2*a)
                print((n - a)*" ",end="")
                for f in range(x+1):
                    print(f+1,end='')
                print((n-a)*" ",end="")
                print("")
            a=a-1 
    else:
        print("ERROR")
elif s=="Half Kite":
    for i in range(n):
        for f in range(i+1):
            print(f+1,end='')
        print((n-i)*" ",end="")
        print("")
    a=n-1
    while a>(-1):
        if a!=(n-1) :
            for f in range(a+1):
                print(f+1,end='')
            print("")
        a=a-1 
elif s=="X":
    if n%2==0:
        a=n-1
        while a>(-1):
            x=(2*a)
            print((n - a)*" ",end="")
            for f in range(x+1):
                print(f+1,end='')
            print((n-a)*" ",end="")
            print("")
            a=a-1 
        for i in range(n):
            if i!=0:
                x=(2*i)
                print((n-i)*" ",end="")
                for f in range(x+1):
                    print(f+1,end='')
                print((n-i)*" ",end="")
                print("") 
    else:
        print("ERROR")
else :
    print("ERROR")