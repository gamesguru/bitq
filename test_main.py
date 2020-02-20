import os

import pyspx.shake256_128s as sphincs
import pytest

from qc.utils import ip, pk, sk
from qc.utils.clstructs import Block, Transaction


def test_gen_wallet():
    seed = os.urandom(sphincs.crypto_sign_SEEDBYTES)
    pk, sk = sphincs.generate_keypair(seed)
    print()
    print("pk: " + pk.hex())
    print("sk: " + sk.hex())


def test_sign_verify():
    message = "Hi there coin user".encode()

    sig = sphincs.sign(message, bytes.fromhex(sk))
    assert sphincs.verify(message, sig, bytes.fromhex(pk))

    fake_sk = "90999d256748e4f194b1a7698c1bd8ac0e7574aa776c5822bfce5118b257683789279d7a3853770cc41f4110b08908f1c11879f943461954dd0557f894e34aca"
    fake_sig = sphincs.sign(message, bytes.fromhex(fake_sk))
    assert not sphincs.verify(message, fake_sig, bytes.fromhex(pk))


def test_genesis():
    receiver = "test2"
    amount = 0.001

    tx = []
    tx.append(Transaction(pk, receiver, amount, sk))

    block = Block(tx=tx)
