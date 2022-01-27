import hashlib

#Take a private key and generate a public one
def createKey(privateKey):
    publicKey = hashlib.sha256(privateKey.encode()).hexdigest()
    return publicKey

#Take in a public and private key and authenticate
def verifyKey(privateKey, publicKey):
    if createKey(privateKey) == publicKey:
        return True
    else:
        return False

'''
#Debugging purposes
private = input("Please enter your private key: ")
print("Your public key is:", createKey(private))

print(verifyKey(private, "391564c95f94223095ac7a28e80a09b1779ab739fa6c89ffe6be41235f27c063"))
'''
