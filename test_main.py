import json

import pyspx.shake256_128s as sphincs
import pytest

from qc.crypt import generate_keypair, v1_address
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
    password = "sEc/Re_t"

    pk, sk = generate_keypair(seed_words, password)
    print(json.dumps({"pk": pk.hex(), "sk": sk.hex()}, indent=2))
    address = v1_address(pk, n_id=0x00)

    assert (
        pk.hex() == "9c2c1c48b6b1d3925415fae598dbcd7c01b9dba503319399398c8b9b5b7da7c6"
    )
    assert (
        sk.hex()
        == "a869b534aa9dbce884f8c077b09b9e6b075d4ed4ee7cedf64e9492d4dc55369f9c2c1c48b6b1d3925415fae598dbcd7c01b9dba503319399398c8b9b5b7da7c6"
    )
    assert address == "0K_I$DvCl%&Ud4U(VhmJ5U`X1U~Wud!W=$H3i!3g*S7v9-T"


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
