import random as r
import service as s
count = 0
class Account:
    def generateAccountNo(self):
        self.accountNumber = r.randint(0,100)

    def __init__(self):
        self.transaction = dict()
    def __init__(self,name,address,contact,balance,newService):
        self.name = name
        self.address = address
        self.contact = contact
        self.balance = balance
        self.generateAccountNo()
        self.addToSericeBase(newService)

    def addToSericeBase(self,newService):
        dict1 = {
                self.accountNumber:{
                    "name":self.name,
                    "address":self.address,
                    "balance":self.balance,
                    "contact":self.balance
                }
            }
        newService.insertDict(dict1)
        print(newService.accountList)

