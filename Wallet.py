import KeyManager as stauber

#This is in charge of handling the user account and keeping a total of the current balance
class Wallet:

    #Initialize
    def __init__(self, userName, privateKey):
        self.userName = userName
        self.publicKey = stauber.createKey(privateKey)

        print("User", userName, "created successfully!")
        print("Your public key is:", self.publicKey)

firstUser = Wallet("Rhyse", "Th15is@password")

#Make sure we can create a user, set a private key, generate a public key, and verify the public key belongs to that user.
test = input("Verify your public key works: ")
print(stauber.verifyKey(firstUser.privateKey, test))