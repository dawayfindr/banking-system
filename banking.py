bal = 0.0
name = input("Name: ")
password = input("Password: ")
while True:
    if name == 'rahul':
        if password == 'choudhary':
            print("\n***WELCOME TO YOUR OWN BANK***\n")
            print('''1. deposit
2. withdraw
3. show balance
4. exit\n''')
            ch = int(input("Enter your choice: "))
            if ch == 1:
                dep = float(input("Enter amount to deposit: "))
                bal = bal + dep
                print("thank you for banking with us. your money has been deposited. \ncurrent balance is ", bal)
                if dep < 0:
                    print("enter a valid amount\n")
                    bal = bal - dep
            elif ch == 2:
                wit = float(input("Enter the amount to withdraw: "))
                bal = bal - wit
                print("amount withdrawn successfully.\ncurrent balance is ", bal)
                if wit > bal:
                    print("\nINSUFFICIENT FUNDS\ncurrent balance is ", bal)
                    bal = bal + wit
            elif ch == 3:
                print("\nyour current balance is ", bal, "\n")
            elif ch == 4:
                break
            else:
                print("enter a valid choice")
        else:
            print("incorrect username or password")
            break
    else:
        print("incorrect username or password")
        break