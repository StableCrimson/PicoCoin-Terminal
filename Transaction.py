from Block import Block
import KeyManager as stauber
import Chain

#Begin a new transaction
def startTransaction():
    fromAccount = input("Transfer from: ")
    toAccount = input("Transfer to: ")
    amount = int(input("Transfer amount (PC): "))

    print(amount, "PicoCoin |", fromAccount, "->", toAccount)

    verify = input("Is this correct? (y/n): ")

    if verify == "y":
        verifyTransaction(fromAccount, toAccount, amount)
    elif verify == "n":
        startTransaction()
    else:
        print("Invalid input!")
        startTransaction()

#Make sure we can verify the transaction as legitimate before moving funds around
def verifyTransaction(fromAccount, toAccount, amount):

    #Get the user's private key and verify before we begin the transaction
    private = input("Please enter your key: ")

    if stauber.verifyKey(private, "391564c95f94223095ac7a28e80a09b1779ab739fa6c89ffe6be41235f27c063"): #Since we're not using keys as from and to rn, I'm simply using a placeholder. In the future, the "from" and "to" will be public keys, and you will be asked to enter the private key to authenticate
        print("Authentication success!")
        print("Beginning transaction id:", "PLACEHOLDER") #TODO Retrieve the ID of the next block in the chain
        initTransaction(fromAccount, toAccount, amount)
    else:
        print("Unable to verify key, please try again.")
        startTransaction()

#Initiate the transaction and record it in the blockchain
def initTransaction(fromAccount, toAccount, amount):

    transactionContent = str(amount) + " PicoCoin | " + fromAccount + " -> " + toAccount + " | verified"
    
    #If there was no previous transaction, then feed 0 as the previous hash because this is the genesis block
    if Chain.getLastTransaction() == 0:
        Chain.addBlock(Block("GENESIS", [transactionContent]))
    else:
        Chain.addBlock(Block(Chain.getLastTransaction().block_hash, [transactionContent]))

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