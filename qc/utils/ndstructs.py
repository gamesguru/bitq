import time

from .. import __version__


class Block:
    def __init__(self, index, relayer, tx=[]):
        self.index = index
        self.ver = __version__

        self.relayer = relayer
        self.time = int(time.time() * 1000)

        self.nonce = None
        self.tx = tx


class Transaction:
    def __init__(self, time, index, relayer, sender, receiver):
        self.time = time
        self.index = index

        self.relayer = relayer
        self.sender = sender
        self.receiver = receiver


class Coin:
    def __init__(self, no):
        self.no = no
