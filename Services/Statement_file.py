from Services.ATM_Operations import account

def statement():
    print("\nTransaction Statement:")
    for transaction in account.statement:
        print(f"{transaction[0]}: {transaction[1]}")