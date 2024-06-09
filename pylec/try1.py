ans="yes"
while(ans=='yes'):
    a=int(input("enter: "))
    b=a
    c=0
    while(a>0):
        d=a%10
        c=c*10+d
        a=a//10
        
    if(b==c):
        print("Palindrome")
    else:
        print("Not Palindrome")
    ans=input("would you continue: ")

string=input("enter a letter")
if(string==string[::-1]):
     print("Palindrome")
else:
     print("Not Palindrome")