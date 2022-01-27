#Manage a record of the blocks

chain = []

#Add a block to the chain
def addBlock(newBlock):
    chain.append(newBlock)

#Get the most recent transaction
def getLastTransaction():
    
    if len(chain) == 0:
        return 0
    else:
        return chain[len(chain) - 1]

#Print all of the previous transactions
def printHistory():

    if len(chain) == 0:
        print("No history to display.")
    else:
        for block in chain:
            print("\nTransaction contents:", block.block_data)
            print("Block hash:", block.block_hash)
        print("\n")