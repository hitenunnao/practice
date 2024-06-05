#creating and testing funnction
def myfuc():            #this is the basic example to show how the syntax of fuction looks
    print("hello world!")
myfuc()

# now creating it with parameters
def myfucwithparameter(x):
    print(x)
myfucwithparameter(69)

#now creating it with multiple parameters
def myfucwithparameters(x,y,z):
    if(x<y):
        if(y<z):
            print("small number is x=",x)
        elif(x>z):
            print("smallest number is z=",z)
    else:
        print("smallest number is y=",y)
myfucwithparameters(4,3,2)

def try1(*car):
    print("list of car",car)
try1("hyrider","baleno","fortuner","santro","i10","i20")
