def babolonian_sqrt(f):
    if f<0:
        print("error")
    else:
        limit=1e-14
        x0= 1+ int((f)**1/2)
        i=1
        while i==1:
            x1 = (x0 + (f/x0)) / 2
            if (-1)*limit<(x1-x0)<limit:
                break
            x0 =x1
        return x1
c= 299792458
nu=98*c/100
t_spacecraft=24
#sdesf=(1-((nu/c)**2))**(1/2)
gamma= babolonian_sqrt(1-((nu/c)**2))
tdash_staionaryobserver= t_spacecraft/gamma
print(tdash_staionaryobserver) #,(t_spacecraft/sdesf))
#print(babolonian_sqrt(4), (4**(1/2)))