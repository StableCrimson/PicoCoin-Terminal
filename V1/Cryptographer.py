#Provides encryption functionality to the resource manager
from Crypto.Cipher import AES

#Encode a string
def encode(data):

    key= b'SILCINEEDGARPICO'
    cipher = AES.new(key, AES.MODE_EAX)
    nonce = cipher.nonce
    print('Success')
    encrypted_data, tag = cipher.encrypt_and_digest(bytes(data, 'UTF-8'))
    return nonce, encrypted_data, tag

def decode(nonce, data, tag) -> str:

    print(data)
    cipher = AES.new(tag, AES.MODE_EAX, nonce=nonce)
    plaintext = cipher.decrypt(bytes.decode(data))

    try:
        cipher.verify(data)
        print(plaintext)
        return plaintext
    except ValueError:
        print('Incorrect key or message corrupted')

nonce, secret, tag = encode('Helloworld!')
secret = decode(nonce, secret, tag)
print(secret)

#TODO Add PyCryptodome to the dependency list if I can get this to work