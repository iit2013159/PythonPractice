import Account as a
import service as s
import random as r
newService = s.service()

def addAccount():
    numOfAccount = int(input("how many A/C"))
    while((numOfAccount) > 0):
        name =input("Please Enter Name")
        address = input("your address ")
        contactNo = input("Your contact Number")
        balance = int(input("First time deposit money"))
        newAccount = a.Account(name,address,contactNo,balance,newService)
        print(newAccount.accountNumber)
        numOfAccount -= 1


def optionTransferMoney():
    option = int(input("Choose:\n1.Continue transfer\n2.Go back to menu"))
    if(option == 1):
        transferMoney()
    elif(option == 2):
        clientOption()
    else:
        print("Not valid option\t Choose wisely again")
        optionTransferMoney()

def addMoney(account,money):

    creditAccount =(newService.accountList.get(account).get("Account"))
    creditAccount.balance += money
    creditAccount.transaction[r.randint(0,100)] ={
        "money recieved":money,
        "totalMoney":creditAccount.balance
    }
    print(creditAccount)
    print(newService.accountList.get(account))
    return 0

def reduceMoney(account,money):
    account.balance -= money
    account.transaction[r.randint(0, 100)] = {
        "money sent": money,
        "totalMoney": account.balance
    }

def transferMoney():
    fromAccount = int(input("Please enter sender A/C number"))
    if not newService.accountList.get(fromAccount):
        print('Account doesnot exist')
        optionTransferMoney()
    debitAccount = (newService.accountList.get(fromAccount).get("Account"))

    money = int(input("How much amount"))
    bal = newService.accountList.get(fromAccount).get("balance")
    if(bal < money):
        print("Low Balance Not possible")
        optionTransferMoney()
    toAccount = int(input("Please Enter reciever A/C number"))
    if not newService.accountList.get(toAccount):
        print("Reciever account doesNot exist")
        optionTransferMoney()
    if(addMoney(toAccount,money) == 0):
        reduceMoney(debitAccount,money)
        print(newService.accountList.get(fromAccount))




def takeInput():
    return input("Chooose :\n 1.Add Account \n 2. Transfer money\n 3. Debit Money \n 4.Add Money \n5.Exit")


def clientOption():
    menuOption = takeInput()
    while(menuOption != "5"):
        if(menuOption == "1"):
            addAccount()
            menuOption = takeInput()
        elif(menuOption == "2"):
            transferMoney()
            menuOption = takeInput()
        elif(menuOption == "3"):
            print("This feature is under development")
            menuOption = takeInput()
        elif (menuOption == "4"):
            print("This feature is under development")
            menuOption = takeInput()
        else:
            print("Not valid choice")
            menuOption = takeInput()

clientOption()