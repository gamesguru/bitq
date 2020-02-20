import time
from decimal import Decimal
from hashlib import sha3_256 as sha3

import pyspx.shake256_128s as sphincs

from .. import __version__
from . import ip


class Block:
    def __init__(self, tx=[]):
        self.ver = __version__
        self.time = int(time.time() * 1000)
        self.relayer = ip

        self.tx = tx

        self.nonce = None


class Transaction:
    def __init__(self, sender, receiver, amount, sk):
        self.ver = __version__
        self.time = int(time.time() * 1000)
        self.relayer = ip

        self.sender = sender
        self.receiver = receiver
        self.amount = Decimal(amount)

        # Create hash, and signature
        self.hash = sha3(
            ",".join([self.sender, self.receiver, str(self.amount)]).encode()
        ).hexdigest()
        self.signature = sphincs.sign(self.hash.encode(), bytes.fromhex(sk)).hex()
