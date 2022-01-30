import csv, os.path
from posixpath import split
import TerminalManager as term
#Take care of the files

USER_PATH = 'data/users.csv'

#Check if the files even exist.
def _file_exists(path: str) -> bool:

    if os.path.exists(path):
        term.print_success('File \'' + path + '\' found!')
        return True
    else:
        term.print_error('File \'' + path + '\' not found. Generating empty file') #If the file doesn't exist, create it.
        open(path, 'x')
        return False

#Get the data of a single user
def load_user(name: str, public_key: str) -> list[str]:

    with open(USER_PATH, 'r') as userbase:
        reader = csv.reader(userbase)


        for entry in reader:
            
            if entry[0] == name and entry[2] == public_key:
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
                term.print_success('Balance for user ' + entry[0] + ' successfully updated')

    with open(USER_PATH, 'w') as userbase:
        writer = csv.writer(userbase)

        for entry in users:
            writer.writerow(entry)

#add_user('Rhyse', 12, '568aefd')
#user = load_user('Jacob', 'b78d7a3abd660d67a8e9b9dfa7e839619b1cb7fb74cf329b71ef0f700991eb79')
#print(user[0], user[2])