def nested1():
    rows=int(input("enter rows: "))
    column=int(input("enter columns: "))
    symbol=input("enter symbol: ")
    for i in range(rows):
        for x in range(column):
            print(symbol,end=" ")
        print()
nested1()

def nested2():
    symbol=input("enter symbol: ")
    for i in range(1,5):
        for x in range(0,i):
            print(x,end=" ")
        print()
nested2()

def nested3():
    symbol=input("enter symbol: ")
    for i in reversed(range(1,5)):
        for x in range(0,i):
            print(symbol,end=" ")
        print()
nested3()