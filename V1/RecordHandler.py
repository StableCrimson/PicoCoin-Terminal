from Wallet import Wallet
from Block import Block

#Load the userbase
def loadUsers():

    users = []

    with open('Logs/users.txt') as userBase:
        lines = userBase.readlines()

        for line in lines:
            
            parsed = line.split(",")
            
            userName = parsed[0]
            userBalance = int(parsed[1])
            userKey = parsed[2]

            users.append(Wallet(userName, userKey, userBalance))
        
        return users

            #print("User " + userName + " found, with a balance of " + userBalance + "dPC and a public key of: " + userKey)

#Load the transaction history
def loadTransactions():

    with open('Logs/history.txt') as transactionHistory:
        lines = transactionHistory.readlines()

        for line in lines:

            parsed = line.split(",")
            id = parsed[0]
            content = parsed[1]
            hash = parsed[2]

            print("Transaction #" + id, content, hash)

#Save a new user to the history
def saveUser(userName, userKey, userBalance):
    with open('Logs/users.txt', 'a') as userBase:
        userBase.writelines("\n" + userName + "," + str(userBalance) + "," + userKey)
        print("Write success")

#Save a new transaction to the history
def saveTransaction(id, content, hash):

    with open('Logs/history.txt', 'a') as transactionHistory:
        transactionHistory.writelines(str(id) + "," + content + "," + hash + "\n");
        print("Transaction saved")

#Update the user balance
def updateBalance(balance, publicKey):

    with open('Logs/users.txt') as userBase:

        lines = userBase.readlines()

        for line in lines:

            parsed = line.split(",")
            name = parsed[0] #TODO something
            key = parsed[2]

            if key == publicKey:
                userBase.writelines(line, (name + "," + str(balance) + "," + key))
                return True

#Debugging
updateBalance(19, "2c70e12b7a0646f92279f427c7b38e7334d8e5389cff167a1dc30e73f826b683")
#loadUsers()
#saveUser("Noelle", "420", "69")
#loadTransactions()