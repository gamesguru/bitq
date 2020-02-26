import json

import pyspx.shake256_128s as sphincs
import pytest

from qc.crypt import generate_keypair, pk2address, verify_address
from qc.utils import ip, pk, sk
from qc.utils.clstructs import Block, Transaction


def test_gen_wallet():
    # Use known seed (9 random words from about 58,000)
    seed_words = [
        "tablespoonfuls",
        "anthropomorphism",
        "effortless",
        "deceives",
        "colostomy",
        "factually",
        "elections",
        "doggerel",
        "inconspicuousness",
    ]
    password = "B0Ymz0yC"

    pk, sk = generate_keypair(seed_words, password)
    print(json.dumps({"pk": pk.hex(), "sk": sk.hex()}, indent=2))
    address = pk2address(pk, version=0x01)

    # Checks
    assert verify_address(address)[0]
    assert (
        pk.hex() == "9eae33ee33a98225f253416339d49b16f02e6ed2c87a8c6b82b46d21e9d57f33"
    )
    assert (
        sk.hex()
        == "1fd378132ea92f67e129c05d3e8fca3bdc442c9aef2cc2efb3a7b985a95b32429eae33ee33a98225f253416339d49b16f02e6ed2c87a8c6b82b46d21e9d57f33"
    )
    assert (
        address
        == "v1_1fdae0bd63796e3dd78a2c223ee569a40c0f34c777a3656d3a7cbca79ee1b7ea_234f6c97"
    )


def test_sign_verify():
    message = "Hi there coin user".encode()

    sig = sphincs.sign(message, bytes.fromhex(sk))
    assert sphincs.verify(message, sig, bytes.fromhex(pk))

    fake_sk = "90999d256748e4f194b1a7698c1bd8ac0e7574aa776c5822bfce5118b257683789279d7a3853770cc41f4110b08908f1c11879f943461954dd0557f894e34aca"
    fake_sig = sphincs.sign(message, bytes.fromhex(fake_sk))
    assert not sphincs.verify(message, fake_sig, bytes.fromhex(pk))


def test_server():
    pass


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
