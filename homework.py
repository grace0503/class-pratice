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
        self.customer = Customer('C64086117','20010503','tainan')
        self.transactions = Transaciton('12345','20200808')

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

class Transaciton():
    def __init__(self,tid,tDate):
        self.tid = tid
        self.tDate =tDate

class Withdraw(Transaciton):
    def __init__(self,tid,tDate,wAmount):
        super().__init__(tid,tDate)
        self.wAmount = wAmount
class Deposit(Transaciton):
    def __init__(self,tid,tDate,dAmount):
        super().__init__(tid,tDate)
        self.dAmount = dAmount
class  Transfer (Transaciton):
    def __init__(self,tid,tDate,tAmount,bankNo,accounts):
        super().__init__(tid,tDate)
        self.tAmount = tAmount
        self.bankNo = bankNo
        self.accounts = accounts


