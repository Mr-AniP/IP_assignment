print("Welcome to program which makes your own polynomial function!!")
print("So let us start....") 
degree=int(input("Degree of your polynomial : "))
coeff=[]
for i in range(0,degree+1,1):
    print("coefficient ",(i+1)," : ", end='')
    coeff_input=float(input())
    print("",end='')
    coeff.append(coeff_input)
lower_bound=int(input("Lower Bound for x : "))
upper_bound=int(input("Upper Bound for x : "))
increament_value=int(input("Steps in which you would vary x : "))
def f(x):
    s=0
    for f in range(0 , degree+1, 1):
        lm=(x**f)*coeff[degree-f]
        s = s + lm
    return s
print("-------------------------------------------------------------------------------------------------------")
for g in range(lower_bound, upper_bound+1 , increament_value):
    if f(g)>0:
        xyz=round(f(g))
    else:
        xyz=0
    print("|"+("*"*xyz))
print("-------------------------------------------------------------------------------------------------------")