import datetime as dt
import ResourceManager as res_man
import TerminalManager as term
import hashlib, json

SIGNATURE = '001100'

#Just compile this all into a dictionary and return it
def create_block(index: int, data: str, proof: int, previous_hash: str):

    block = {

            'index': index,
            'timestamp': str(dt.datetime.now()),
            'data': data,
            'proof': proof,
            'previous_hash': previous_hash

        }

    res_man.write_block(block)

#Mine a block
def mine_block(data: str):

    #If there is no previous block, create the genesis
    if not res_man.last_block():

        term.print_header('No previous block found, creating GENESIS')
        previous_block = {'GENESIS': 'GENESIS'}
        previous_proof = '0'
        index = 0
        proof = 0
        previous_hash = 'GENESIS'
        create_block(index, data, proof, previous_hash)

    else:

        previous_block = res_man.last_block()
        previous_proof = int(previous_block['proof'])
        index = int(previous_block['index']) + 1
        proof = proof_of_work(index, previous_proof, data)
        previous_hash = hash_block(previous_block)
        create_block(index, data, proof, previous_hash)

#Compute the proof of work for the block
def proof_of_work(index: int, previous_proof: str, data: str) -> int:

    proof = 0
    signed = False

    while not signed:

        to_digest = digest(index, data, proof, previous_proof)
        hash = hashlib.sha256(to_digest).hexdigest()

        if hash.startswith(SIGNATURE):
            signed = True
        else:
            proof += 1

    return proof

#Do a calculation for the proof
def digest(index: int, data: str, proof: int, previous_proof: int) -> bytes:
    digested = str(proof ** 2 - previous_proof ** 2 + index) + data
    return digested.encode()

#Hash an entire block
def hash_block(block: dict) -> str:
    encoded_block = json.dumps(block, sort_keys=True).encode()
    return hashlib.sha256(encoded_block).hexdigest()