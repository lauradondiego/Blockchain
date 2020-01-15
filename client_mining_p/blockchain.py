# Paste your version of blockchain.py from the basic_block_gp
# folder here

import hashlib
import json
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request

# there is a pip file so, run -pipenv shell- in terminal
# then do -pipenv install- to install all of the dependencies
# hashlib import on line 1 does hash functions for you
# uuid import on line 4 means importos a universally unique id
# flask import from line 6 is a microframework
# cd in any python run the file
# test the routes in the browser http://localhost:5000/mine and http://localhost:5000/chain
# with flask, you have to control c out of the server then restart it by running the file to see tests
# I added a test hello world in the chain endpoint and it works when restarted
# UNLESS YOU CHANGE DEBUGGER TO TRUE WHICH I DID SO NOW IT GOES AUTOMATICALLY


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # Create the genesis block
        self.new_block(previous_hash=1, proof=100)

    def new_block(self, proof, previous_hash=None):
        """
        Create a new Block in the Blockchain

        A block should have:
        * Index
        * Timestamp
        * List of current transactions
        * The proof used to mine this block
        * The hash of the previous block

        :param proof: <int> The proof given by the Proof of Work algorithm
        :param previous_hash: (Optional) <str> Hash of previous Block
        :return: <dict> New Block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            # imported up top
            'transactions': self.current_transactions,
            # coming from the init up in Blockchain class
            'proof': proof,
            # proof is coming from passing it in
            'previous_hash': previous_hash
            # hash of previous block coming from passing it in
        }

        # Reset the current list of transactions
        self.current_transactions = []
        # Append the chain to the block
        self.chain.append(block)
        # Return the new block
        return block

    def hash(self, block):
        """
        Creates a SHA-256 hash of a Block

        :param block": <dict> Block
        "return": <str>
        """

        # Use json.dumps to convert json into a string
        # Use hashlib.sha256 to create a hash
        # It requires a `bytes-like` object, which is what
        # .encode() does.
        # It convertes the string to bytes.
        # We must make sure that the Dictionary is Ordered,
        # or we'll have inconsistent hashes

        # TODO: Create the block_string
        string_object = json.dumps(block, sort_keys=True).encode()
        # look up doc for json.dumps() & sort keys sorts them alphabetically & .encode

        # TODO: Hash this string using sha256
        raw_hash = hashlib.sha256(string_object)
        # imported up top

        hex_hash = raw_hash.hexdigest()
        # hexdigest() converts hash to a string of hexadecimal

        # By itself, the sha256 function returns the hash in a raw string
        # that will likely include escaped characters.
        # This can be hard to read, but .hexdigest() converts the
        # hash to a string of hexadecimal characters, which is
        # easier to work with and understand

        # TODO: Return the hashed block string in hexadecimal format
        return hex_hash

        # now def hash is complete

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, block):
        """
        Simple Proof of Work Algorithm
        Stringify the block and look for a proof.
        Loop through possibilities, checking each one against `valid_proof`
        in an effort to find a number that is a valid proof
        :return: A valid proof for the provided block
        """
        # TODO
        block_string = json.dumps(block)
        proof = 0
        while self.valid_proof(block_string, proof) is False:
            proof += 1
        return proof
        # return proof

    @staticmethod
    def valid_proof(block_string, proof):
        """
        Validates the Proof:  Does hash(block_string, proof) contain 3
        leading zeroes?  Return true if the proof is valid
        :param block_string: <string> The stringified block to use to
        check in combination with `proof`
        :param proof: <int?> The value that when combined with the
        stringified previous block results in a hash that has the
        correct number of leading zeroes.
        :return: True if the resulting hash is a valid proof, False otherwise
        """
        # TODO
        # find out if it has 3 leading zeros below
        guess = f"{block_string}{proof}".encode()
        # ADD .ENCODE() IF YOU GET ERRORS WHEN YOU TEST MINE ENDPOINT IN BROSWER
        # now find the hash below
        guess_hash = hashlib.sha256(guess).hexdigest()
        # compare below to see if equal to first 3 zeros
        return guess_hash[:3] == "000"
        # return True or Fals


# Instantiate our Node
app = Flask(__name__)

# Generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# Instantiate the Blockchain
blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    # Run the proof of work algorithm to get the next proof
    # call the function you just wrote
    proof = blockchain.proof_of_work(blockchain.last_block)
    # Forge the new Block by adding it to the chain with the proof

    previous_hash = blockchain.hash(blockchain.last_block)
    block = blockchain.new_block(proof, previous_hash)
    # read the helper text that pops up it is super helpful!!!

    response = {
        # TODO: Send a JSON response with the new block
        'new_block': block
    }
    # CHECK THE MINE ENDPOINT TO MAKE SURE ITS WORKING

    return jsonify(response), 200
    # ^ success response in json
    # (dont spend too much time learning flask, recognize 200 is success!)


@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        # TODO: Return the chain and its current length
        'test': "hello there testing with auto debug set to true",
        'length': len(blockchain.chain),
        'chain': blockchain.chain

    }
    return jsonify(response), 200


# Run the program on port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
