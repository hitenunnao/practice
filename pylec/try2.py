# to print the reverse of any number
a=int(input("enter: "))
b=a
c=0
while(a>0):
    remainder=a%10
    c=c*10+remainder
    a=a//10
print(c)

# positive odd number series
i=1
a=0
b=1
l=[]
x=int(input("enter the number of terms"))
while(i<=x):
    c=a+b
    a=a+1
    b=b+1
    i=i+1
    l.append(c)
print(l)

# positive even number series
i=1
a=0
b=0
l=[]
x=int(input("enter the number of terms"))
while(i<=x):
    c=a+b
    a=a+1
    b=b+1
    i=i+1
    l.append(c)
print(l)