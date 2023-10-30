class BankAccount:
    def __init__(self, account_number, pin, balance=0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited ${amount}")
            return True
        return False

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew ${amount}")
            return True
        return False

    def transfer(self, amount, recipient_account):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            recipient_account.balance += amount
            self.transaction_history.append(f"Transferred ${amount} to {recipient_account.account_number}")
            return True
        return False

    def get_transaction_history(self):
        return self.transaction_history

    def get_balance(self):
        return self.balance


def main():
    # Creating a bank account with a PIN
    account1 = BankAccount("20200841", "0841", 1000)
    account2 = BankAccount("20200842", "0842", 1500)

    while True:
        entered_pin = input("Enter your PIN: ")

        if entered_pin == account1.pin:
            print("\nATM Menu:")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Transfer Money")
            print("5. Transaction History")
            print("6. Quit")

            choice = input("Enter your choice (1-6): ")

            if choice == "1":
                print(f"Your balance is ${account1.get_balance()}")

            elif choice == "2":
                amount = float(input("Enter the deposit amount: $"))
                if account1.deposit(amount):
                    print(f"${amount} deposited successfully.")
                else:
                    print("Invalid amount. Please try again.")

            elif choice == "3":
                amount = float(input("Enter the withdrawal amount: $"))
                if account1.withdraw(amount):
                    print(f"${amount} withdrawn successfully.")
                else:
                    print("Invalid amount or insufficient balance. Please try again.")

            elif choice == "4":
                recipient_account_number = input("Enter recipient's account number: ")
                recipient_account = None

                if recipient_account_number == account2.account_number:
                    recipient_account = account2

                if recipient_account is not None:
                    amount = float(input(f"Enter the transfer amount to {recipient_account_number}: $"))
                    if account1.transfer(amount, recipient_account):
                        print(f"${amount} transferred successfully to {recipient_account_number}.")
                    else:
                        print("Invalid amount or insufficient balance. Please try again.")
                else:
                    print(f"Recipient account {recipient_account_number} not found.")

            elif choice == "5":
                print("Transaction History:")
                for transaction in account1.get_transaction_history():
                    print(transaction)

            elif choice == "6":
                print("Thank you for using the ATM. Goodbye!")
                break

            else:
                print("Invalid choice. Please select a valid option.")
        else:
            print("Incorrect PIN. Please try again.")


if __name__ == "__main__":
    main()
