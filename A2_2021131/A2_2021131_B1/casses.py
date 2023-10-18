def computeMe(a):
    s=a*8
    return s
def generateData():
    n=int(input("No. of testcases : "))
    for i in range(n):
        f1="A2_2021131/testcase_"+str(i)+"_input.txt"
        f2="A2_2021131/testcase_"+str(i)+"_output.txt"
        b=input()
        a=computeMe(b)
        with open(f1,'w') as f:
            f.write(b)
        with open(f2,'w') as f:
            f.write(a)
generateData()