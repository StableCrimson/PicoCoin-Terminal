import KeyManager as stauber
import Chain, Users

#TODO Make sure the amount of coin we are moving is <= the user's current balance

#Begin a new transaction
def startTransaction():
    fromAccount = input("Transfer from: ")
    toAccount = input("Transfer to: ")

    #Make sure we're not transferring to the same account
    if fromAccount == toAccount:
        print("Cannot transfer to self")
        return 0

    amount = int(input("Transfer amount (PC): "))

    #Make sure the amount isn't less than 0
    if amount <= 0:
        print("Cannot make a transaction with 0 or less PC.")
        return 0

    verifyTransaction(fromAccount, toAccount, amount)

#Make sure we can verify the transaction as legitimate before moving funds around
def verifyTransaction(fromAccount, toAccount, amount):

    #See if the users exist
    if not Users.checkPublicKey(fromAccount):
        print("No user found with key:", fromAccount)
        return 0
    else:
        print("Sender verified! User: " + Users.checkPublicKey(fromAccount).userName)
    if not Users.checkPublicKey(toAccount):
        print("No user found with key:", toAccount)
        return 0
    else:
        print("Receiver verified! User: " + Users.checkPublicKey(toAccount).userName)

    #Get the user's private key and verify before we begin the transaction
    private = input("Please enter your private key: ")

    if stauber.verifyKey(private, Users.checkPublicKey(fromAccount).publicKey): #Since we're not using keys as from and to rn, I'm simply using a placeholder. In the future, the "from" and "to" will be public keys, and you will be asked to enter the private key to authenticate
        print("Authentication success!")
    else:
        print("Unable to verify key, please try again.")
        startTransaction()

    print(amount, "PicoCoin |", fromAccount, "->", toAccount)

    verify = input("Is this correct? (y/n): ")

    id = 0
    if Chain.getLastTransaction() != 0:
        id = int(Chain.getLastTransaction().block_id) + 1

    if verify == "y":
        print("Beginning transaction id:", id) #TODO Retrieve the ID of the next block in the chain
        initTransaction(fromAccount, toAccount, amount, id)
    elif verify == "n":
        startTransaction()
    else:
        print("Invalid input!")
        startTransaction()

#Initiate the transaction and record it in the blockchain
def initTransaction(fromAccount, toAccount, amount, id):

    #Just for the same of making things nicer
    sender = "(" + Users.checkPublicKey(fromAccount).userName + ")" + "-" + fromAccount
    receiver = "(" + Users.checkPublicKey(toAccount).userName + ")" + "-" + toAccount

    transactionContent = str(amount) + " PicoCoin | " + sender + " -> " + receiver + " | verified"
    
    #If there was no previous transaction, then feed 0 as the previous hash because this is the genesis block
    if Chain.getLastTransaction() == 0:
        Chain.addBlock("GENESIS", [transactionContent], 0)
        Users.checkPublicKey(fromAccount).balance -= amount
        Users.checkPublicKey(toAccount).balance += amount
    else:
        Chain.addBlock(Chain.getLastTransaction().block_hash, [transactionContent], str(id))
        Users.checkPublicKey(fromAccount).balance -= amount
        Users.checkPublicKey(toAccount).balance += amount

    #Debug
    print(Chain.getLastTransaction().block_data)

    #Do we want to make another transaction?
    choice = input("Would you like to make another transaction? (y/n): ")

    if choice == "y":
        startTransaction()
    elif choice == "n":
        return 0
    else:
        print("Invalid selection, going back to menu screen.")
        return 0