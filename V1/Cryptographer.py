#Provides encryption functionality to the resource manager
from cryptography.fernet import Fernet
import csv
import os.path

KEY_PATH = 'data/key.key'

'''with open('data/dec_users.csv', 'wb') as users:
    users.write(readable)'''

def encrypt(source: str, dest: str):
    #Does the key exist?
    if os.path.exists(KEY_PATH):

        #Yes? Read it.
        with open(KEY_PATH, 'rb') as key_file:
            key = key_file.read()

    else:

        #No? Generate a new one
        print('Key file not found, generating new key.')
        key = Fernet.generate_key()

        with open(KEY_PATH, 'wb') as key_file:
            key_file.write(key)

    f = Fernet(key)

    with open(source, 'r') as source_file:
        with open(dest, 'wb') as dest_file:

            reader = csv.reader(source_file)
            writer = csv.writer(dest_file)

            for line in reader:
                writer.writerow(f.encrypt(line))

encrypt('data/users.csv', 'data/new_users.csv')
encrypt('data/chain.csv', 'data/new_chain.csv')
