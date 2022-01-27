from Wallet import Wallet
import KeyManager as stauber

#Manage the users on the blockchain
users = []

#Create a new user
def newUser():
    
    userName = input("Enter the name of the user you'd like to create: ")

    #Can we make a user with that name?
    if checkUserName(userName):
        print("User with this name already exists")
        return 0

    privateKey = input("Please enter your private key: ")

    users.append(Wallet(userName, privateKey))

#Is the user here?
def checkUserName(userName):

    for user in users:
        if userName == user.userName:
            return user
        
    return False

#Does a user have this address?
def checkPublicKey(key):

    for user in users:
        if key == user.publicKey:
            return user

    return False

#Get the balance of a registered user
def getBalance():

    name = input("Please enter your name: ")

    #Make sure you exist
    if checkUserName(name):
        print("User found!")
    else:
        print("Cannot find user or user does not exist. Please check the spelling.")
        return 0

    key = input("Please enter your private key: ")

    if not stauber.verifyKey(key, checkUserName(name).publicKey):
        print("Unable to authenticate.")
        return 0

    print("The current balance for user " + name + " is: " + str(checkUserName(name).balance) + "PC.")

#Remove a registered user
def removeUser():

    #Make sure the user even exists
    name = input("Enter the name of the user you'd like to remove: ")

    if checkUserName(name):
        print("User found")
    else:
        print("Cannot find user or user does not exist. Please check the spelling.")
        return 0

    #Make sure this person is authorized to remove the user
    key = input("Please enter the private key of the user: ")

    if stauber.verifyKey(key, checkUserName(name).publicKey):
        print("Key authenticated successfully, user " + name + "removed.")

        users.remove(checkUserName(name))

    else:
        print("Unable to authenticate, key may be invalid.")
        return 0



'''
#Debug
newUser("Rhyse", "key")
newUser("Jacob", "keyTwo")

for user in users:
    print(user.userName)

print("Current balance for account", users[0].userName, "is", users[0].balance, "PicoCoin")
print("Current balance for account", users[1].userName, "is", users[1].balance, "PicoCoin")
removeUser()

for user in users:
    print(user.userName)

#'''