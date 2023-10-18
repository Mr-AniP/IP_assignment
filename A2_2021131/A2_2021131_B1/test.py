def replicate_strings(a):
    l=[a for i in range(8)]
    s="".join(l)
    return s
def testing(mn):
    for i in range(mn):
        f1="A2_2021131/testcase_"+str(i)+"_input.txt"
        f2="A2_2021131/testcase_"+str(i)+"_output.txt"
        with open(f1,'r') as f:
            m=f.readline()
        a=replicate_strings(m)
        with open(f2,'r') as f:
            m=f.readline()
        if a==m:
            print("SUCCESS")
        else:
            print("FAILED")
testing(int(input("Enter the no. of cases to be tested(= no. of cases generated using casses.py): ")))