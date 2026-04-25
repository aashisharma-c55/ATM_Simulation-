from Services.ATM_Operations import balance
from Services.ATM_Operations import withdraw
from Services.ATM_Operations import deposit
from Services.Statement_file import statement


while True:
    print("\n--- Game Menu ---")
    print("1. - Display Balance")
    print("2. - Deposit Money")
    print("3. - Withdraw Money")
    print("4. - Bank Statement (transaction record)")
    print("5. - Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        balance()
    elif choice == 2:
        amount = float(input("Amount to deposit: "))
        deposit(amount)      
    elif choice == 3:
        amount = float(input( "Amount to withdraw: "))
        withdraw(amount)   
    elif choice == 4:
        statement()    
    elif choice == 5:
        print("Thank you ..\n" 
        "Have a Great day!")
        break
    else:
        print("Invalid choice!\nPlease try again...")    