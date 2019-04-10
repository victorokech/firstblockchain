class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # create new block and add it to chain
        pass

    @staticmethod
    def hash(block):
        # hashing a block
        pass

    @property
    def last_block(self):
        # returns the last block
        pass