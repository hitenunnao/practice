# function to print the reverse of any number
def reverse(x):
    n=x
    c=0
    while(n>0):
        remainder=n%10
        c=c*10+remainder
        n=n//10
    print(c)
x=int(input("enter to print the reverse of any number: "))
reverse(x)


# fuction to print positive odd number series
def odd_series(x):
    i=1
    a=0
    b=1
    l=[]
    n=x
    while(i<=n):
        c=a+b
        a=a+1
        b=b+1
        i=i+1
        l.append(c)
    print(l)
x=int(input("enter the number of terms to print positive odd number series: "))
odd_series(x)


# fuction to print positive even number series
def even_series(x):
    i=1
    a=0
    b=0
    l=[]
    n=x
    while(i<=n):
        c=a+b
        a=a+1
        b=b+1
        i=i+1
        l.append(c)
    print(l)
x=int(input("enter the number of terms to print positive even number series: "))
even_series(x)


# this function is used to print the fibonacci series upto the desired number
def fibonacci_series(x):
    n=x
    a=0
    b=1
    c=b
    i=1
    while(i<=n):
        print(a,end="  ")
        i+=1
        a,b=b,c
        c=a+b
x=int(input("enter the number of terms to print the fibonacci series upto the desired number: "))
fibonacci_series(x)


# this function checks the number entered by user is Armstrong or Not..
def armstrong(x):
    n=x
    a=n
    s=0
    while(n>=1):
        b=n%10
        s=s+(b*b*b)
        n=n//10
    if(s==a):
        print("armstrong")
    else:
        print("not armstrong")
x=int(input("enter to function checks the number entered by user is Armstrong or Not..: "))
armstrong(x)


# function to check the enter number is palindrome
def palindrome(x):
    n=x
    a=n
    i=0
    c=0
    while(i<n):
        b=n%10
        c=c*10+b
        n=n//10
    if(c==a):
        print("PALINDROME")
    else:
        print("NOT PALINDROME")
x=int(input("enter to check the number is Palindrome"))
palindrome(x)


# function to find maximum element in the list
def find_Max():
    l=[]
    n=int(input("enter the number of elements you want to enter: "))
    i=0
    while(i<n):
        element=int(input("enter the element: "))
        l.append(element)
        i+=1
    item=0
    max_element=l[0]
    for item in l:
        if item > max_element:
            max_element = item
    return max_element
print(find_Max())   


# function to find minimum element in the list
def find_Min():
    l=[]
    n=int(input("enter the number of elements you want to enter: "))
    i=0
    while(i<n):
        element=int(input("enter the element: "))
        l.append(element)
        i+=1
    item=0
    min_element=l[0]
    for item in l:
        if item < min_element:
            min_element = item
    return min_element
print(find_Min())   


# function to  take input in a list
def list():
    l=[]
    n=int(input("enter the number of elements you want to enter: "))
    i=0
    while(i<n):
        element=int(input("enter the element: "))
        l.append(element)
        i+=1
    return l
print(list())


# function to print number of occurence 
def occurence(x):
    x=int(input("enter the number: "))
    count=0
    check=list()
    for i in check:
        if i == x:
            count+=1
    return count
print(occurence())


# function to delete the duplicates
def duplicate():
    check=list()
    x=int(input("enter the duplicate element to delete: "))
    for item in check:
        if item == x:
            check.pop(item)
    return check
duplicate()


    


