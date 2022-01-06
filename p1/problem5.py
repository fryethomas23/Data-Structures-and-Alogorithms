import hashlib
import json
from datetime import datetime

class Block:

    def __init__(self, timestamp, data, previous_hash):
      self.timestamp = timestamp
      self.data = data
      self.previous_hash = previous_hash
      self.hash = self.calc_hash()
      self.prev = None
    
    # Hashes block data
    def calc_hash(self):
        sha = hashlib.sha256()

        # Turns block attributes into json string
        block_str = json.dumps(vars(self), sort_keys=True)

        hash_str = block_str.encode('utf-8')

        sha.update(hash_str)

        return sha.hexdigest()
    
    def set_prev(self, block):
        self.prev = block

    def get_prev(self):
        return self.prev

    def get_hash(self):
        return self.hash   

# Block chain using a linked list.
class BlockChain:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add_block(self, data):
        if self.size == 0:
            self.head = Block(datetime.now().timestamp(), data, 0)
            self.tail = self.head
            self.size += 1
        else:
            new_block = Block(datetime.now().timestamp(), data, self.tail.get_hash())
            new_block.set_prev(self.tail)
            self.tail = new_block
            self.size += 1

    def get_tail(self):
        return self.tail

    def get_head(self):
        return self.head

    def __repr__(self):
        block = self.tail
        string = "\nBlock Chain\n_____________________"

        count = self.size - 1
        while block:
            block_info = json.dumps(
                vars(block), 
                default=lambda o: f'<Block {count-1}>', 
                indent=4
            )
            string += f"\nBlock {count}: \n{block_info}\n"
            count -= 1
            block = block.get_prev()
        
        return string

if __name__ == "__main__":
    print("Test 1:")
    chain = BlockChain()
    chain.add_block('cool kid')
    chain.add_block('very cool kid')
    print(chain)
    # Block Chain
    # _____________________
    # Block 1:
    # {
    #     "timestamp": 1641496639.091338,
    #     "data": "very cool kid",
    #     "previous_hash": "58fecf108fcee7e1710f0f0f44787e10e57bc886029c3e5665a73b89a56b48ed",
    #     "hash": "59a3ee51488d1b078b72df20137bfb8e5d64be5757bd101476b1443c74026547",
    #     "prev": "<Block 0>"
    # }

    # Block 0:
    # {
    #     "timestamp": 1641496639.090334,
    #     "data": "cool kid",
    #     "previous_hash": 0,
    #     "hash": "58fecf108fcee7e1710f0f0f44787e10e57bc886029c3e5665a73b89a56b48ed",
    #     "prev": null
    # }

    print("Test 2:")
    chain = BlockChain()
    chain.add_block('kinda cool kid')
    print(chain)
    # Block Chain
    # _____________________
    # Block 0:
    # {
    #     "timestamp": 1641496639.094335,
    #     "data": "kinda cool kid",
    #     "previous_hash": 0,
    #     "hash": "5b24cd9863dd7b69ede704fefd2e8661a757ff6f40cc367452ebec0073fbaca4",
    #     "prev": null
    # }

    print("Test 3:")
    chain = BlockChain()
    print(chain)
    # Block Chain
    # _____________________
