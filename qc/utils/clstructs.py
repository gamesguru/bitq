import time
from decimal import Decimal
from hashlib import sha3_256 as sha3

import pyrx
import pyspx.shake256_128s as sphincs

from .. import __version__
from . import ip


class Block:
    def __init__(self, tx, nonce, seed_hash):
        self.ver = __version__
        self.time = int(time.time() * 1000)
        self.relayer = ip

        self.tx = tx
        tx_hashes = [t.hash for t in self.tx]

        self.nonce = nonce

        # Hash
        uuid = ";".join(
            [self.ver, str(self.time), self.relayer, str(self.nonce), *tx_hashes]
        )
        bh = pyrx.get_rx_hash(uuid, seed_hash, nonce)
        hh = binascii.hexlify(bh).decode()

        self.hash = sha3(
            ";".join(
                [self.ver, str(self.time), self.relayer, str(self.nonce), *tx_hashes]
            ).encode()
        ).hexdigest()
        print(self.hash)


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
            ";".join(
                [
                    self.ver,
                    str(self.time),
                    self.relayer,
                    self.sender,
                    self.receiver,
                    str(self.amount),
                ]
            ).encode()
        ).hexdigest()
        self.sig = sphincs.sign(self.hash.encode(), bytes.fromhex(sk)).hex()
