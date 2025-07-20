user = {}

def create_account():
    name = input("Enter Your Name: ")
    if name in user:
        print("Account Already Exists.")
    else:
        user[name] = 0
        print(f"Account Created for {name} with balance ₹0.")

def deposit():
    name = input("Enter Your Name: ")
    if name in user:
        amount = int(input("Enter amount to deposit: ₹"))
        user[name] += amount
        print(f"₹{amount} deposited. New balance: ₹{user[name]}")
    else:
        print("No account found.")

def withdraw():
    name = input("Enter Your Name: ")
    if name in user:
        amount = int(input("Enter amount to withdraw: ₹"))
        if amount <= user[name]:
            user[name] -= amount
            print(f"₹{amount} withdrawn. New balance: ₹{user[name]}")
        else:
            print("Not enough balance.")
    else:
        print("No account found.")

def check_balance():
    name = input("Enter Your Name: ")
    if name in user:
        print(f"Balance for {name}: ₹{user[name]}")
    else:
        print("No account found.")

def main():
    while True:
        print("\n=== Simple Bank System ===")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")

        if choice == '1':
            create_account()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            check_balance()
        elif choice == '5':
            print("Thank you for using our bank!")
            break
        else:
            print("Invalid choice. Try again.")

main()
