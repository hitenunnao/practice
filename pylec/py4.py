def f1(a):
    if(a>=18):
        print("you are eligible to vote")
    else:
        return("you are note eligible")
def f2(a,b):
    c=a+b
    return("sum=",c)
x=int(input("enter your age"))
y=f1(x)
print(y)
# or
# print(f1(x))
x=int(input("enter"))
y=int(input("enter"))
print(f2(x,y))

def f3(n):
    a=1
    while(a<11):
        print(n*a)
        a=a+1
tab=int(input("enter"))
f3(tab)

