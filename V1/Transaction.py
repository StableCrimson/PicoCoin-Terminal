'''So what do we need to do?
    Deposit
        Add PC to an account 0 DEPOSIT -> PUBLIC_ADDRESS
    Withdraw
        Remove PC from an account 1 PUBLIC_ADDRESS -> WITHDRAW
    Transfer
        Move from one account to another 2 SENDER_PUBLIC -> RECIPIENT_PUBLIC
    Provide a transaction history
        Loop through the data in the blockchain. If the data contains your public key, add it to the list and return it
'''
import TerminalManager as term
import Userbase as users
import ResourceManager as res_man
import Block as block

#Deposit to your account
def deposit(username: str, private_key: str):

    amount = input('How much would you like to deposit?: ')
    public_key = users._create_key(username, private_key)

    #If you didn't enter a number, go fuck yourself
    if not amount.isnumeric():
        term.clear()
        term.print_error('Value entered is not an integer')
        return None

    #Get the user's new balance
    total = users.get_balance(username, private_key) + int(amount)
    term.clear()

    #Create the data for the transaction and throw it into the blockchain
    #If we were able to mine it, update the user's balance
    block_data = ['0', amount, 'DEPOSIT->' + public_key]
    print('Mining... ', end='')
    block.mine_block('|'.join(block_data))
    res_man.update_balance(public_key, total)
    term.print_success('Done!')

#Withdraw from your account
def withdraw(username: str, private_key: str):
    
    amount = input('How much would you like to withdraw?: ')
    public_key = users._create_key(username, private_key)

    #If you didn't enter a number, go fuck yourself
    if not amount.isnumeric():
        term.clear()
        term.print_error('Value entered is not an integer')
        return None

    total = users.get_balance(username, private_key) - int(amount)
    term.clear()

    #Make sure you don't withdraw more than you have
    if total < 0:
        term.print_error('Not enough funds available')
        return None

    print('Mining... ', end='')

    #Create the data for the transaction and throw it into the blockchain
    #If we were able to mine it, update the user's balance
    block_data = ['1', amount, public_key + '->WITHDRAW']
    block.mine_block('|'.join(block_data))
    res_man.update_balance(public_key, total)
    term.print_success('Done!')

#Here's the big boy, move funds from one account to another
def transfer(username: str, private_key: str):
    
    sender_key = users._create_key(username, private_key)
    recipient_key = input('Please enter the public address of the destination account: ')
    recipient_user = res_man.load_user(recipient_key)
    term.clear()

    #Make sure you're not transfering to yourself
    if sender_key == recipient_key:
        term.print_error('Cannot transfer to self')
        return None

    #Okay so you're not sending money to yourself, but does the recipient exist, you schizo?
    if recipient_user[0] == 'NOTFOUND':
        term.print_error('Unable to verify recipient address')
        return None

    amount = input('Please enter the amount you\'d like to transfer: ')

    #If you didn't enter a number, go fuck yourself
    if not amount.isnumeric():
        term.clear()
        term.print_error('Value entered is not an integer')
        return None

    sender_total = users.get_balance(username, private_key) - int(amount)
    recipient_total = int(recipient_user[1]) + int(amount)

    #Make sure you have the necessary funds
    if sender_total < 0:
        term.print_error('Not enough funds available')
        return None

    print('Mining... ', end='')
    block_data = ['2', amount, sender_key + '->' + recipient_key]
    block.mine_block('|'.join(block_data))
    res_man.update_balance(sender_key, sender_total)
    res_man.update_balance(recipient_key, recipient_total)
    term.print_success('Done!')

#Get the transaction history
def get_history(name: str, private_key: str):
    
    public_key = users._create_key(name, private_key)
    history = res_man.get_history(public_key)

    for entry in history:

        #Digest the contents of the block and make it readable before displaying it
        contents = entry['data'].split('|')
        amount = contents[1]
        addresses = contents[2].replace(public_key, name) #Replace the public key with your username
        
        #Get the transaction type
        if contents[0] == '0':
            type = 'DEPOSIT'
        elif contents[0] == '1':
            type = 'WITHDRAW'
        elif contents[0] == '2':
            type = 'TRANSFER'
        else:
            term.print_error('Something went wrong, invalid transaction type. Please have an administrator check the validity of the blockchain')

        print('Transaction #' + entry['index'] + ' | Timestamp: ' + entry['timestamp'] + ' | Transaction type: ' + type)
        print('Amount: ' + amount + ' | ' + addresses + '\n')

