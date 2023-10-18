n=int(input("Enter Value of N for cration of 2d NXN square matrix : "))
matrix=[]
for f in range(n):
    l=[i for i in input().split()]
    matrix.append(l)
print("-------------------------------------------------------------------------------------------------------")
print("1.Normal traversal")
print("2.Alternating traversal")
print("3.Spiral traversal from outwards to inwards")
print("4.Boundary traversal")
print("5.Diagnol transversal from right to left")
print("6.Diagnol transversal from leftto right")
print("7.Interesting pattern created by chance during coding the 6th part")
print("-------------------------------------------------------------------------------------------------------")
m=int(input("ENTER YOUR CHOICE (input choice no. only!) : "))
if m==1:
    for i in range(n):
        for j in range(n):
            print(matrix[i][j],end=" ")
    print("")
elif m==2:
    for i in range(n):
        if i%2==0:
            for j in range(n):
                print(matrix[i][j],end=" ")
        else:
            for j in range(1,n+1):
                print(matrix[i][n-j],end=" ")
    print("")
elif m==3:
    for j in range(n):
        for i in range(j,n-j):
            print(matrix[j][i],end=" ")
        for i in range(j+1,n-j):
            print(matrix[i][n-1-j],end=" ")
        for i in range(j+2,n+1-j):
            print(matrix[n-1-j][n-i],end=" ")
        for i in range(j+2,n-j):
            print(matrix[n-i][j],end=" ")
    print("")
elif m==4:
    for i in range(n):
        print(matrix[0][i],end=" ")
    for i in range(1,n):
        print(matrix[i][n-1],end=" ")
    for i in range(2,n+1):
        print(matrix[n-1][n-i],end=" ")
    for i in range(2,n):
        print(matrix[n-i][0],end=" ")
    print("")
elif m==5:
    for sum in range(2*n):
        for i in range(n):
            for j in range(n):
                if i+j==sum:
                    print(matrix[i][j],end=" ")
    print("")
elif m==7:
    for diff in reversed(range(n)):
        for i in reversed(range(n)):
            for j in reversed(range(n)):
                if i-j==diff or j-i==diff :
                    print(matrix[i][j],end=" ")
    print("")
elif m==6:
    for diff in reversed(range(n)):
        for i in (range(n)):
            for j in (range(n)):
                if j-i==diff:
                    print(matrix[i][j],end=" ")
    for diff in range(1,n):
        for i in (range(n)):
            for j in (range(n)):
                if i-j==diff:
                    print(matrix[i][j],end=" ")
    print("")
else:
    print("Wrong input")
    print("ERROR")