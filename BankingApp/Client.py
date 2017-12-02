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
    dict2 ={
        r.randint(0, 100):{
            "money recieved": money,
            "totalMoney": creditAccount.balance
        }
    }
    creditAccount.transaction.update(dict2)
    print(creditAccount)
    print(newService.accountList.get(account))
    return 0

def reduceMoney(account,money):
    account.balance -= money
    dict2 = {
        r.randint(0, 100): {
            "money recieved": money,
            "totalMoney": account.balance
        }
    }
    account.transaction.update(dict2)

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
        print("Transaction Successfull")




def takeInput():
    return input("Chooose :\n 1.Add Account \n 2. Transfer money\n 3. Debit Money \n 4.Add Money \n5.viewAccount Report\n6.Exit")


def clientOption():
    menuOption = takeInput()
    while(menuOption != "6"):
        if(menuOption == "1"):
            addAccount()
            menuOption = takeInput()

        elif(menuOption == "2"):
            transferMoney()
            menuOption = takeInput()

        elif(menuOption == "3"):
            fromAccount = int(input("Please enter  A/C number"))
            if not newService.accountList.get(fromAccount):
                print('Account doesnot exist')
                clientOption()
            debitAccount = (newService.accountList.get(fromAccount).get("Account"))

            money = int(input("How much amount"))
            bal = newService.accountList.get(fromAccount).get("balance")
            if (bal < money):
                print("Low Balance Not possible")
                clientOption()
            reduceMoney(debitAccount, money)
            print("Debit Successfull")
            menuOption = takeInput()

        elif (menuOption == "4"):
            toAccount = int(input("Please enter  A/C number"))
            if not newService.accountList.get(toAccount):
                print('Account doesnot exist')
                clientOption()
            money = int(input("How much amount"))
            bal = newService.accountList.get(toAccount).get("balance")
            if (bal < money):
                print("Low Balance Not possible")
                clientOption()
            addMoney(toAccount, money)
            print("credit Successfull")
            menuOption = takeInput()
        elif(menuOption == "5"):
            someAccount = int(input("Please enter  A/C number"))
            if not newService.accountList.get(someAccount):
                print('Account doesnot exist')
            print(newService.accountList.get(someAccount))
        else:
            print("Not valid choice")
            menuOption = takeInput()

clientOption()