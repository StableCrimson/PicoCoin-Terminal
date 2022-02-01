import csv, os.path
from posixpath import split
import TerminalManager as term
#Take care of the files

USER_PATH = 'data/users.csv'
CHAIN_PATH = 'data/chain.csv'

#Check if the files even exist.
def _file_exists(path: str) -> bool:

    if os.path.exists(path):
        # TODO Implement a debug flag term.print_success('File \'' + path + '\' found!')
        return True
    else:
        term.print_error('File \'' + path + '\' not found. Generating empty file') #If the file doesn't exist, create it.
        open(path, 'x')
        return False

#Get the data of a single user
def load_user(public_key: str) -> list[str]:

    with open(USER_PATH, 'r') as userbase:
        reader = csv.reader(userbase)


        for entry in reader:
            
            if entry[2] == public_key:
                return entry
        
        term.print_error('Unable to find user')
        return ['NOTFOUND', 'NOTFOUND', 'NOTFOUND']

#Add a user to the userbase
def add_user(name: str, balance: int, public_key: str):

    with open(USER_PATH, 'a') as userbase:
        writer = csv.writer(userbase)
        writer.writerow([name, balance, public_key])
        #term.print_success('DEBUG Successfully saved user ' + name + ' to the userbase')

#Remove a user from the userbase
def remove_user(public_key: str):

    users = []

    with open(USER_PATH, 'r') as userbase:
        reader = csv.reader(userbase)
        
        for entry in reader:
            users.append(entry)

            if entry[2] == public_key:
                users.remove(entry)
                term.print_success('User ' + entry[0] + ' successfully removed')

    with open(USER_PATH, 'w') as userbase:
        writer = csv.writer(userbase)

        for entry in users:
            writer.writerow(entry)

def update_balance(public_key: str, balance: int):

    users = []

    with open(USER_PATH, 'r') as userbase:
        reader = csv.reader(userbase)
        
        for entry in reader:
            users.append(entry)

            if entry[2] == public_key:
                entry[1] = balance
                #DEBUG term.print_success('Balance for user ' + entry[0] + ' successfully updated')

    with open(USER_PATH, 'w') as userbase:
        writer = csv.writer(userbase)

        for entry in users:
            writer.writerow(entry)

#Write a new block
def write_block(block: dict):

    if _file_exists(CHAIN_PATH):

        with open(CHAIN_PATH, 'a') as blockchain:
            writer = csv.writer(blockchain)
            writer.writerow(block.values())

#Get the last block in the list
def last_block():

    if _file_exists(CHAIN_PATH):

        with open(CHAIN_PATH, 'r') as blockchain:
            reader = csv.reader(blockchain)
            
            lines = 0

            for line in reader:
                lines += 1

            #If the number of lines is 0, the file is empty
            if lines == 0:
                return False
            else:
                
                block = {

                    'index': line[0],
                    'timestamp': line[1],
                    'data': line[2],
                    'proof': line[3],
                    'previous_hash': line[4]
                }

                return block

#Get the transactions that involve a specific user
def get_history(public_key: str) -> list():

    if _file_exists(CHAIN_PATH):

        with open(CHAIN_PATH, 'r') as blockchain:
            reader = csv.reader(blockchain)
            
            lines = 0
            history = list()

            for line in reader:

                lines += 1

                if lines == 0:
                    return False

                data = line[2].split('|')

                if data[2].startswith(public_key) or data[2].endswith(public_key):
                
                    block = {

                        'index': line[0],
                        'timestamp': line[1],
                        'data': line[2],
                        'proof': line[3],
                        'previous_hash': line[4]
                    }
                    history.append(block)

            return history