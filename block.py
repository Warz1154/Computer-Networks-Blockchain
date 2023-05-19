import hashlib
class Block:
    def _init_(self, data, previous):
        self.hash = hashlib.sha256()
        self.previous = previous
        self.nonce = 0
        self.data = data
#While the hash is too big while it's bigger than the difficulty requirments >>increment the nonce by 1>>then reset the hash
    def mine(self, difficulty):
        self.hash.update(str(self).encode('utf-8'))
        size = 2 ** (256 - difficulty)
        while int(self.hash.hexdigest(), 16) > size:
            self.nonce += 1
            self.hash = hashlib.sha256()
            self.hash.update(str(self).encode('utf-8'))

    def _str_(self):
        return "{}{}{}".format(self.previous.hexdigest(), self.data, self.nonce)