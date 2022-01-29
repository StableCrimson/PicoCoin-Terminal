import hashlib

#A single block for a PicoCoin transaction
class Block:

    SIGNATURE = "0110" #This will be in the hash of the block. If it's not there, we can't verify that the transaction this block represents is legitimate
    

    def __init__(self, previous_block_hash, transaction_list, block_id):
        self.previous_block_hash = previous_block_hash
        self.transaction_list = transaction_list
        self.block_id = block_id

        self.block_data = "-".join(transaction_list) + "-" + previous_block_hash + "-" + str(block_id)
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

        #Introduce the idea of transaction signing, if the hash doesn't begin with 0000, then it's not a signed transaction
        nonce = 0
        while not self.block_hash.startswith(self.SIGNATURE):
            nonce += 1
            self.block_data = "-".join(transaction_list) + "-" + previous_block_hash + "-" + str(nonce) + "-" + str(block_id)
            self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()


'''
#Make sure our block works
initial_block = Block("Initial String", ["Silcine pays 15PC to Indyth", "Cynath loses 2PC gambling in Go Fish"])
second_block = Block(initial_block.block_hash, ["Edgar invests his gold in 500PC so he can retire early and do bear things", "Pico pays herself 1PC"])
third_block = Block(second_block.block_hash, ["Zoltan lost 9PC cause he's fucking dead"])

print("Transaction contents:", initial_block.block_data)
print("Block hash:", initial_block.block_hash)
print("Tranaction contents:", second_block.block_data)
print("Block hash:", second_block.block_hash)
print("Tranaction contents:", third_block.block_data)
print("Block hash:", third_block.block_hash)
'''