import getpass
import json
import os
import random
import sys

import pyspx.shake256_128s as sphincs
import pytest

from qc.crypt import v1_address
from qc.utils import ip, pk, sk
from qc.utils.clstructs import Block, Transaction


def test_gen_wallet():
    # Choose 9 random words from about 58,000
    # words = []
    # for word in open("resources/corncob_lowercase.txt").readlines():
    #     words.append(word.rstrip())
    # seed_phrase = " ".join(random.choice(words) for i in range(9))

    # Use known seed
    seed_phrase = "tablespoonfuls anthropomorphism effortless deceives colostomy factually elections doggerel inconspicuousness"
    print("\nseed_phrase: %s" % seed_phrase)

    # password = getpass.getpass("password: ")
    # confirm_password = getpass.getpass("confirm:  ")
    # password = "secret"
    # confirm_password = "secret"
    # if password != confirm_password:
    #     assert False

    # Create bytes-seed
    random.seed(seed_phrase)
    r = random.getrandbits(384)
    seed = r.to_bytes(48, sys.byteorder)

    pk, sk = sphincs.generate_keypair(seed)
    address = v1_address(pk, n_id=0x00)
    assert (
        pk.hex() == "fc02a0ac80b9dae15e113db753f1a90705153a9f58a6609969e0952102238b2f"
    )
    assert (
        sk.hex()
        == "dd9d4f0a24cc017956ec173708023729aeb6d53d4b173e9df3f3618bb13af8e4fc02a0ac80b9dae15e113db753f1a90705153a9f58a6609969e0952102238b2f"
    )
    assert address == "035{>1T<6+iryZLjuAAo$#kS&`~J#+BKo<)j>FYbFz46RzW"
    print(json.dumps({"pk": pk.hex(), "sk": sk.hex(), "address": address}, indent=2))


def test_sign_verify():
    message = "Hi there coin user".encode()

    sig = sphincs.sign(message, bytes.fromhex(sk))
    assert sphincs.verify(message, sig, bytes.fromhex(pk))

    fake_sk = "90999d256748e4f194b1a7698c1bd8ac0e7574aa776c5822bfce5118b257683789279d7a3853770cc41f4110b08908f1c11879f943461954dd0557f894e34aca"
    fake_sig = sphincs.sign(message, bytes.fromhex(fake_sk))
    assert not sphincs.verify(message, fake_sig, bytes.fromhex(pk))


def test_genesis():
    seed_hash = bytes.fromhex(
        "63eceef7919087068ac5d1b7faffa23fc90a58ad0ca89ecb224a2ef7ba282d48"
    )
    receiver = "test2"
    amount = 0.001

    tx = []
    tx.append(Transaction(pk, receiver, amount, sk))

    block = Block(tx=tx, seed_hash=seed_hash, nonce=0)


def test_create_teardown_db():
    from qc.sql import sql

    r = sql("SELECT * FROM qubit")
    print(r)
