a=int(input("enter the number  "))        #table
i=1
while(i<11):
    print(i*a)
    i=i+1

a=int(input("enter value  "))    #factorial
i=1
while(a>=1):
    i=a*i
    a=a-1
print(i)  

a=int(input("enter"))       #swapping numbers
b=int(input("enter"))
print("before swapping value of a and b are:",a,b)
c=a
a=b
b=c
print("values of a and b after swapping are:",a,b)

a=int(input("enter age"))       #conditinal statements
if(a>=18):
    print("you are eligible")
else:
    print("you are not eligible")

a=[4,5,6]           #impementing for loop
for i in a:
    print(i)