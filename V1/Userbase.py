from venv import create
import ResourceManager as res_man
import TerminalManager as term
import hashlib

#Handle the entire userbase, all of it.
'''
    What does a user need?
    Username: Rhyse
    Balance: 15PC
    Public key: dkfjapoifjapweiof amls ahprg
    Contacts: 'Jacob's public key', 'Brody's public key'

'''

#Create a new user
def create_user():
    
    name = input('Please enter your username: ')
    #TODO Verify that there aren't other users by that name

    private_key = input('Hi ' + name + ', please enter your private key: ')
    term.clear()
    public_key = _create_key(name, private_key)

    #If we were able to create the user, then congratulate them and give them their publi key
    term.print_success('User created successfully! Welcome to PicoCoin, ' + name + '!')
    print('Here\'s your public key: ' + public_key)

    #Save the new user to the file
    res_man.add_user(name, 0, public_key)
    return 0

#Remove a user
def remove_user(username: str):

    key = input('Please enter your private key: ')

    term.clear()

    if not verify_key(username, key):
        term.clear()
        term.print_error('Unable to verify the key')
        return 0

    if get_balance(username, key) != 0:
        term.clear()
        term.print_error('Cannot remove user with funds in account')
        return 0

    choice = input('This action cannot be undone, are you sure? (y/n): ')

    if choice == "y".lower():
        term.clear()
        res_man.remove_user(_create_key(username, key))
    elif choice == 'n'.lower():
        term.clear()
        return 0
    else:
        term.print_error('Invalid input!!!')
        return 0

#Directly changing the balance deposit/withdraw
def direct(username: str, private_key: str, withdraw: bool):

    #amount = ''

    #Change the prompt based on if we are withdrawing or not
    if withdraw:
        amount = input('How much would you like to withdraw?: ')
    else:
        amount = input('How much would you like to deposit?: ')

    #If you didn't put in a number, go fuck yourself
    if not amount.isnumeric():
        term.clear()
        term.print_error('Value entered is not an integer')
        return 0
    
    total = get_balance(username, private_key)

    #If we're withdrawing and you want to take out more than you have, go fuck yourself
    if total < int(amount) and withdraw:
        term.clear()
        term.print_error('Not enough funds available')
        return 0

    if withdraw:
        total -= int(amount)
    else:
        total += int(amount)

    term.clear()
    res_man.update_balance(_create_key(username, private_key), total)
    
#Create the public key for a user
def _create_key(username: str, private_key: str) -> str:

    public_key = hashlib.sha256((username + private_key).encode()).hexdigest()
    return public_key

#Verify the private key of a user
def verify_key(username: str, private_key: str) -> bool:

    public_key = _create_key(username, private_key)

    #Here is where we need to get the data from the user in question
    to_verify = res_man.load_user(username, public_key)
    if to_verify[0] == username and to_verify[2] == public_key:
        return True
    else:
        return False

#Get the user's balance
def get_balance(username: str, private_key: str) -> int:
    balance = res_man.load_user(username, _create_key(username, private_key))
    return int(balance[1])