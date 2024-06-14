def armstrong(x):
    n=x
    a=n
    s=0
    while(n>=1):
        b=n%10
        s=s+(b*b*b)
        n=n//10         
    if(s==a):
        print("ARMSTRONG")
    else:
        print("NOT ARMSTRONG")
x=int(input("enter to function checks the number entered by user is Armstrong or Not..: "))
armstrong(x)

for i in range(0,1):
    print(i)    

