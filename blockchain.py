'''
NeuralCoin (NC)

t1: Mark sends Kelly 2 NC
t2: Kelly sends McAfee 100 NC
t3: Anna sends Bob 3.4 NC
....

SHA-256
B1: ('AAA', t1, t2, t3) -> 5hd72j
B2: (5hd72j, t4, t5, t6) -> 8fh46d
B3: (8fh46d, t7, t8 ,t9)

'''

import hashlib

class NeuralCoinBlock():
    def __init__(self, pre_block_hash, transaction_list):
        self.pre_block_hash = pre_block_hash
        self.transaction_list = transaction_list

        self.block_data = '-'.join(transaction_list) + '-' + pre_block_hash
        self.block_hash = hashlib.sha256(self.block_data.encode()).hexdigest()

t1 = 'Mark sends 2(NC) to Mike'      
t2 = 'Daniel sends 12(NC) to Jake'      
t3 = 'Finn sends 1.44(NC) to Princess Bubblegum'      
t4 = 'Tom sends 3.9(NC) to Marceline'      
t5 = 'Jade sends 99(NC) to Kelly'
t6 = 'Anna sends 2(NC) to Bob'

init_block = NeuralCoinBlock('init_string', [t1, t2])

print(init_block.block_data)
print(init_block.block_hash)

sec_block = NeuralCoinBlock(init_block.block_hash, [t3, t4])

print(sec_block.block_data)
print(sec_block.block_hash)

