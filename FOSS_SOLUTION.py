mod=1000000007
t=int(input("Enter no.of test cases : "))

for i in range(t):
    r=int(input("Enter no.of row :  "))
    c=int(input("Enter no.of columns :  "))

    m=min(r,c)
    n=max(r,c)

    sq=((1/12)*(m*(m-1)*(m+1)*(2*n-m)))%mod
    print("number of squares formed is :", sq)


''' test cases

    4
    2
    4
    3
    4
    4
    4
    1000
    500
'''
