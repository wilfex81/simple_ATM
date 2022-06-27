class UserAccount():
    
    def __init__(self):
        '''
        We assume that the user was given a valid account number and pin
        when he/she opened an account.
        '''

        self.UserName = input("Enter your name: ")
        self.AccountNumber = input("Enter your account number: ")
        self.AccountPin = input("Enter your account pin: ")
        self.Balance = 0.00
        print('------------------------------------')
        print(f'***Welcome to The Great Bank {self.UserName}***')
        print('------------------------------------')
    
    def validateAccountNumber(self):
        '''
        This function should validate the account number of the user.
        The account number should be digits only.
        '''
        for acount in self.AccountNumber:
            if acount.isdigit() and len(self.AccountNumber) == 10:
                continue
            else:
                print("Please enter a valid account number")
                exit()
        break
        return self.AccountNumber

    def validatePin(self):
        '''
        This function should validate the pin of the user.
        '''
    
        #commented out because we are do not have any pin yet
        # tries = 3
        #  for number_of_tries in tries:
        #         if number_of_tries in tries == 0:
        #             print("You have exceeded the number of tries")
        #             exit()
        #         if number_of_tries in tries == 1:
        #             print("You have 1 try left")
        #         if number_of_tries in tries == 2:
        #             print("You have 2 tries left")
                
        #         tries -= 1
        #         if pin == self.AccountPin:
        #             continue

        for pin in self.AccountPin:
            if pin.isdigit() and len(self.AccountPin) == 4:
                continue
            else:
                print("Please enter a valid pin")
                exit()
        return self.AccountPin
    

    def Deposit(self):
        '''
        Ask the user the amount they want to Deposit
        save the amount the user enters
        This function takes the inital amount and adds the amount the user enters.
        It then returns the new amount.
        '''
        amount = 0.00
        deposited_amount = float(input("Enter the amount you want to deposit in Ksh: "))
        if deposited_amount <= 50000.00:
            try: 
                self.Balance = amount + deposited_amount
                print("Amount deposited: " + str(deposited_amount))
                print("Balance is now: " + str(self.Balance))
            except ValueError:
                print("Amount must be a number")
        else:
            print("Amount must be less than 50000")

        return "Balance is now: " + str(amount)

    def accountBalance(self):
        '''
        This function should return the Balance of the user.
        '''
        print("Balance is now: " + str(self.Balance))

        return self.Balance

    def Withdraw(self):
        '''
        This function subtracts the amout the user wants to withdraw,
        from the initial amount
        '''
        try:
            amount = float(input("Enter the amount you want to withdraw in Ksh: "))
            self.Balance = self.Balance - amount
            print("Amount withdrawn: " + str(amount))
            print("Balance is now: " + str(self.Balance))
        except ValueError:
            print("Please enter a valid amount")
        return self.Balance
        
    def Exit(self):
        '''
        Exit function
        '''
        return "Thank you for using our ATM service"

if __name__ == "__main__":

    account = UserAccount()
    account.validateAccountNumber()
    account.validatePin()

    while True:
        print('**Select an option to continue using our services**')
        print('------------------------------------')
        print("""
        1. Balance
        2. Withdraw
        3. Deposit
        4. Exit
        """)

        option = input('Enter your option: ')
        if option == "1":
            account.accountBalance()
        elif option == "2":
            account.Withdraw()
        elif option == "3":
            account.Deposit()
        elif option == "4":
            account.Exit()
        
            print('------------------------------------')
            print("**Thank you for using our service**")
            print('Please come back soon')
            print('Goodbye')
            print('------------------------------------')
            break
        else:
            print("**Sorry, Invalid choice**".upper())

        



        
