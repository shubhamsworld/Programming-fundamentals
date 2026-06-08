class Atm:

    # constructor (Constructor is a special function)-> Dont need to call it explicitly, whenever object is created, constructor fun automatically runs 
    def __init__(self):
        self.pin =''
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input(""" Hi, How can I help you today?
              1. Press 1 to create Pin
              2. Press 2 to change Pin
              3. Press 3 to check Balance
              4. Press 4 to Withdraw
              5. Anything else to Exit
""")
        if user_input == '1':
            # create pin
            self.create_pin()
        elif user_input == '2':
            # change pin
            self.change_pin()
        elif user_input == '3':
            # check balance
            self.check_balance()
        elif user_input == '4':
            # withdraw
            self.withdraw()
        else:
            exit()
        


    def create_pin(self):
        user_pin = input("Enter your pin")
        self.pin = user_pin

        user_balance = int(input("Enter balance"))
        self.balance = user_balance
        print("Pin created successfully")
        self.menu()

    def change_pin(self):
        old_pin = input("Enter old pin")
        if old_pin == self.pin:
            # let him change the pin
            new_pin = input("Enter new pin")
            self.pin = new_pin
            print("Pin changed successfully")
            self.menu()
        else:
            print("You entered wrong pin")
            self.menu()

    def check_balance(self):
        user_pin = input("Enter your pin")
        if user_pin == self.pin:
            print("Your balance is", self.balance)
        else:
            print("You entered wrong pin")
        self.menu()

    def withdraw(self):
        user_pin = input("Enter your pin")
        if user_pin == self.pin:
            amount = int(input("Enter the amount"))
            if amount <= self.balance:
                self.balance = self.balance - amount
                print("Withdrawl successful, remaining balance is,",self.balance)
            else:
                print("Insufficient balance")
        else:
            print("You entered wrong pin")
        self.menu()




obj = Atm()