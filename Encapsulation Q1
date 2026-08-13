class bankaccount:
    def __init__(self, accnumber, name, balance):
        self.accnumber=accnumber 
        self.name=name
        self.__balance=balance 
    def deposit(self, amount):
        self.__balance+=amount 
    def withdraw(self, amount):
        if self.__balance<amount:
            print("Insufficient balance")
        else:
            self.__balance-=amount 
    def getbalance(self):
        return self.__balance
a1=bankaccount(100, "Shruti", 500)
a1.deposit(20)
a1.withdraw(200)
print(a1.getbalance())
