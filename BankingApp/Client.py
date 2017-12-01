import Account as a
import service as s
newService = s.service()
def addAccount():
    numOfAccount = int(input("how many A/C"))
    while((numOfAccount) > 0):
        name =input("Please Enter Name")
        address = input("your address ")
        contactNo = input("Your contact Number")
        balance = input("First time deposit money")
        newAccount = a.Account(name,address,contactNo,balance,newService)
        print(newAccount.accountNumber)
        numOfAccount -= 1

def transferMoney():
    fromAccount = int(input("Please enter sender A/C number"))
    money = input("How much amount")
    bal = newService.accountList.get(fromAccount).get("balance")
    if(bal < money):
        print("Low Balance Not possible")
    toAccount = int(input("Please Enter reciever A/C number"))


def takeInput():
    return input("Chooose :\n 1.Add Account \n 2. Transfer money\n 3. Debit Money \n 4.Add Money \n5.Exit")



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
    else:
        print("Not valid choice")
