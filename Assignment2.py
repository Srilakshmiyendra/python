#Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.
class Shoppingcart:
    def __init__(self):
        self.items = []

    def additems(self,itemname,quantity):
        item = (itemname,quantity)
        self.items.append(item)

    def removeitems(self,itemname):
        for item in self.items:
            if itemname==item[0]:
                self.items.remove(item)
                break

    def totalcal(self):
        total = 0
        for item in self.items:
         total+=item[1]
        return total

cart=Shoppingcart()

cart.additems("Dairy milk chocolate",150)
cart.additems("5 Star chocolate",30)
cart.additems("milkybar chocolate",40)
cart.additems("Jelly",12)

print("total number of items in cart:")

for item in cart.items:
    print(item[0],'=',item[1])

total=cart.totalcal()
print("Total Quantity:",total)    

#update cart
cart.removeitems("Jelly")
print("Update items after removing Jelly from cart:")
for item in cart.items:
    print(item[0],'=',item[1])

total=cart.totalcal()
print("Total Quantity:",total)


#Write a Python program to create a class representing a bank. Include methods for managing customer accounts and transactions.


class Bank:
    
    def __init__(self):
        self.customers = {}

    # Create a new account
    def createaccount(self, account_number, initial_balance=0):
        if account_number in self.customers:
            print("Account number already exists.")
        else:
            self.customers[account_number] = initial_balance
            print("Account created successfully.")
    #deposit
    def deposit(self, account_number, amount):
        if account_number in self.customers:
            self.customers[account_number] += amount
            print("Deposit successful.")
        else:
            print("Account number does not exist.")

    #withdrawal
    def withdrawal(self, account_number, amount):
        if account_number in self.customers:
            if self.customers[account_number] >= amount:
                self.customers[account_number] -= amount
                print("Withdrawal successful.")
            else:
                print("Insufficient funds.")
        else:
            print("Account number does not exist.")

    
    def checkbalance(self, account_number):
        if account_number in self.customers:
            balance = self.customers[account_number]
            print(f"Account balance: {balance}")
        else:
            print("Account number does not exist.")


bank = Bank()

acno1= 765767
depamt1 = 1000
print("New a/c No.: ",acno1,"Deposit Amount:",depamt1)
bank.createaccount(acno1, depamt1)

acno2= 6757645
depamt2 = 2000
print("New a/c No.: ",acno2,"Deposit Amount:",depamt2)
bank.createaccount(acno2, depamt2)

depamt3 = 600
print("\nDeposit Rs.",depamt3,"to A/c No.",acno1)
bank.deposit(acno1, depamt3)
wdamt1 = 350
print("Withdraw Rs.",wdamt1,"From A/c No.",acno2)
bank.withdrawal(acno2, wdamt1)

print("A/c. No.",acno1)
bank.checkbalance(acno1)

print("A/c. No.",acno2)
bank.checkbalance(acno2)

wdamt3 = 200
print("Withdraw Rs.",wdamt3,"From A/c No.",acno2)
bank.withdrawal(acno2, wdamt3)

acno3 = 87765
print("A/c. No.",acno3)
bank.checkbalance(acno3)                
