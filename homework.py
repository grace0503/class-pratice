class Customer : 
    def __init__(self,id,birthday,address):
        self.id = id
        self.birthday = birthday
        self.address = address
        self.account = Account('grace','20200805','10000')
class Account():
    def __init__(self,accNo,date,balance):
        self.accNo = accNo
        self.date = date
        self.balance = balance

class CheckingAcc(Account):
    def __init__(self,accNo,date,balance,checkNum):
        super().__init__(accNo,date,balance)
        self.checkNum =checkNum
class FixedAcc(Account):
    def __init__(self,accNo,date,balance,interest,period):
        super().__init__(accNo,date,balance)
        self.period = period
        self.interest = interest
class SavingAcc(Account):
    def __init__(self,accNo,date,balance,lowerBound):
        super().__init__(accNo,date,balance)
        self.lowerBound = lowerBound

