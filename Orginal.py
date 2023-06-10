class Bank:
    Total_Bank_balance = 0
    Total_Loan_Of_Bank = 0

    def __init__(self, name, taka) -> None:
        self.name = name
        self.taka = taka
        Bank.Total_Bank_balance += self.taka


class User:
    def __init__(self, name):
        self.name = name
        self.c_account = False
        self.trs_history = []
        self.full_balance = 0
        self.total_loan = 0

    def Sing_in(self, email, password):
        self.email = email
        self.c_account = True

    def Deposite(self, amount):
        if self.c_account:
            self.full_balance += amount
            self.trs_history.append(f'Deposit {amount} Taka')
            Bank.Total_Bank_balance += amount
            print("Successfully Deposit")
        else:
            print("Login First")

    def Withdraw(self, amount):
        if self.c_account:
            if self.full_balance >= amount:
                self.full_balance -= amount
                print("Withdraw Successfully Done!")
                self.trs_history.append(f'Withdraw {amount} Taka')
                Bank.Total_Bank_balance -= amount
                print("Successfully Withdraw")
            else:
                print("Insufficient Balance")
        else:
            print("Login First")

    def Transfer(self, amount, R_account):
        if self.c_account:
            if self.full_balance >= amount:
                self.full_balance -= amount
                R_account.full_balance += amount
                self.trs_history.append(f'Transfer {amount} Taka to {R_account.email}')
                R_account.trs_history.append(f'Received {amount} Taka from {self.name}')
            else:
                print("Check your balance before transferring funds")
        else:
            print("Login First")

    def Take_Loan(self, amount,ad_name):
        if ad_name.g_variable:
            if self.c_account:
                limit = self.full_balance * 2
                if amount <= limit:
                    self.full_balance += amount
                    self.total_loan += amount
                    Bank.Total_Loan_Of_Bank += amount
                    self.trs_history.append(f'Take {amount} Taka Loan')
                    print("Successfully received loan")
                else:
                    print("Out of Limit")
            else:
                print("Login First")
        else:
            print("This Service Is Not Available")

    def Check_Balance(self):
        print(f'Sir {self.name} Your balance now {self.full_balance} Taka')

    def Check_History(self):
        return self.trs_history


class Admin(User):
    def __init__(self) -> None:
        self.a_account = False
        self.g_variable = True

    def Sing_in(self, name, password):
        self.a_account = True

    def Bank_Balance(self):
        if self.a_account==True:
             r= Bank.Total_Bank_balance
             print(f'Total Balance of Your Bank:--{r}')
        else:
            print("AS AN ADMIN YOU SHOULD LOGING FIRST")

    def Check_Customer_Loan(self, user):
       if self.a_account==True:
            return user.total_loan
       else:
            print("AS AN ADMIN YOU SHOULD LOGING FIRST")

    def Give_Them_Loan(self, h):
        if self.a_account==True:
            if h == 0:
                self.g_variable = False
        else:
            print("AS AN ADMIN YOU SHOULD LOGING FIRST")


bank = Bank('dbbl', 10000)

user1 = User('karim')
user2 = User('rahim')
user3 = User('slim')
user4 = User('amir')



admin1 = Admin()
admin2=Admin()

admin1.Sing_in('admin', '0000123')
#admin2.Sing_in('admin2', '57584850123')

user1.Sing_in('karim@gmail.com', 'user1pass')
user2.Sing_in('rahim@gmail.com', 'user2pass')
user3.Sing_in('selim@gmail.com', 'user3pass')
user4.Sing_in('amir@gmail.com', 'user4pass')

user1.Deposite(5000)
user2.Deposite(3000)
user3.Deposite(2000)
user4.Deposite(1000)

user1.Withdraw(2000)
user2.Withdraw(1000)
user3.Withdraw(500)
user4.Withdraw(100)

user1.Check_Balance()
user2.Check_Balance()
user3.Check_Balance()
user4.Check_Balance()

user1.Transfer(1000, user2)
user2.Transfer(500, user3)
user3.Transfer(200, user4)
user4.Transfer(100, user1)

user1.Check_Balance()
user2.Check_Balance()
user3.Check_Balance()
user4.Check_Balance()

admin1.Check_Customer_Loan(user1)
admin1.Check_Customer_Loan(user2)
admin1.Check_Customer_Loan(user3)
admin1.Check_Customer_Loan(user4)

admin1.Give_Them_Loan(0)
user1.Take_Loan(500,admin1)
admin2.Give_Them_Loan(1)
user2.Take_Loan(3000,admin2)

admin1.Bank_Balance()
