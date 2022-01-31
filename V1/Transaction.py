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
    print('Mining...', end='')
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

    #Get the user's new balance

    #Create the data for the transaction and throw it into the blockchain
    #If we were able to mine it, update the user's balance
    block_data = ['1', amount, public_key + '->WITHDRAW']
    print('Mining...', end='')
    block.mine_block('|'.join(block_data))
    res_man.update_balance(public_key, total)
    term.print_success('Done!')
