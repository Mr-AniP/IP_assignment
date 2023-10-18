l=[0.5,-1]
a=1
b=3
d=1
def f(l,x):
        s=0
        for i in l:
            s= s + x**i
        return s
def calculate_area(l,a,b,d):
    if (a-b)%d==0:
        area=0
        for i in range(a,b,d):
            area = area + (d/6)*(f(l,i)+f(l,i+d)+(4*f(l,(((2*i)+d)/2))))
        print(area)
calculate_area(l,a,b,d)