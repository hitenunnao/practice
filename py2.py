a=[1,2,3,4,5]
for i in a:
    if(i==3):
        break       #use of break: so as the iteration has fully stoped and the output will be 1 2
    print(i)
    
b=[6,7,8,9,10]
for i in b:
    if(i==7):
        continue      #use of continue: so as the iteration has stoped for the the particular iteration and the output will be 6 8 9 10
    print(i) 

c=[1,2,3,4,5]
for i in range(0,3):        #this method will show index number of the list
    print(i)

tup=['mango','apple','kiwi','banana','orange'] 
for i in tup:
    print(i)
    