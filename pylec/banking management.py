def showBalance(balance):
    print(f"Your Balance is ${balance:.2f}")

def deposit():
    amount=float(input("Enter the amount to be deposit: "))

    if amount<0:
        print("please enter valid amount 😕")
        return 0
    else:
        print("Your amount has been deposited 😊")
        return amount
    
def withdrawl(balance):
    amountw=float(input("Enter the amount to be withdwal: "))

    if amountw > balance:
        print("Insufficient Fund 😕")
        return 0
    else:
        print("Your amount has been withdrawled 😊")
        return amountw
         
def bankingManagement():
    balance=0
    isRunning=True
    while isRunning:
        print("Banking Program")
        print("1.Show Balance")
        print("2.Deposit")
        print("3.Withdrawl")
        print("4.Exit")

        choice=input("Enter your choice (1-4): ")

        if choice=='1':
            showBalance(balance)
        elif choice=='2':
            balance += deposit()
        elif choice=='3':
            balance -= withdrawl(balance)
        elif choice=='4':
            isRunning=False
        else:
            print("Invalid Choice")
        
    print("Thankyou for visiting, Have a nice day ✌️😊")  
    return 0  
bankingManagement()