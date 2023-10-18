# PLEASE_NOTE : I have asked to input cost and Depriciation rate 
c=int(input("Initial Cost of your car (Do not input comma) : "))
c_int_cost=c
r=int(input("Depriciation rate : "))
depriciation_rate=r
value=50
cost_of_owning=c_int_cost
mc_new=(1*c_int_cost/100) 
time=15
for y in range(15):
    value=value*11/10
    value_derived=value*6000
    if y<5:
        mc_later = mc_new*(y+1)
    else:
        mc_later= mc_later*3/2
    maintainence_cost=mc_later
    cost_of_owning=cost_of_owning-maintainence_cost - (c_int_cost*depriciation_rate/100)
    if cost_of_owning<value_derived:
        time=y +1
        break
print("The year which is the Best time to sell your car is : ", time,"st year"if time==1 else "nd year" if time==2 else "rd year" if time==3 else "th year")