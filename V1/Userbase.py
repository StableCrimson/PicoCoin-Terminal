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

    private_key = input('Hi ' + name + ', please enter your private key: ')
    term.clear()
    public_key = _create_key(name, private_key)

    #If we were able to create the user, then congratulate them and give them their publi key
    term.print_success('User created successfully!')
    term.print_header('Welcome to your PicoCoin wallet, ' + name + '!')

    #Save the new user to the file
    res_man.add_user(name, 0, public_key)
    return 0

#Remove a user
def remove_user(username: str):

    key = input('Please enter your private key: ')

    term.clear()

    #If we can't verify your key, can't delete
    if not verify_key(username, key):
        term.clear()
        term.print_error('Unable to verify the key')
        return 0

    #If you have money in your account, can't delete
    if get_balance(username, key) != 0:
        term.clear()
        term.print_error('Cannot remove user with funds in account')
        return 0

    choice = input('This action cannot be undone, are you sure? (y/n): ')

    match choice.lower():
        case "y":
            term.clear()
            res_man.remove_user(_create_key(username, key))
        case 'n':
            term.clear()
            return 0
        case _:
            term.print_error('Invalid input!')
            return 0
    
#Create the public key for a user
def _create_key(username: str, private_key: str) -> str:

    public_key = hashlib.sha256((username + private_key).encode()).hexdigest()
    return public_key

#Verify the private key of a user
def verify_key(username: str, private_key: str) -> bool:

    public_key = _create_key(username, private_key)

    #Here is where we need to get the data from the user in question
    to_verify = res_man.load_user(public_key)
    if to_verify[2] == public_key:
        return True
    else:
        return False

#Get the user's balance
def get_balance(username: str, private_key: str) -> int:
    balance = res_man.load_user(_create_key(username, private_key))
    return int(balance[1])