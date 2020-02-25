import base64
import random
import sys
from hashlib import sha3_256 as sha3

import pyspx.shake256_128s as sphincs


def generate_keypair(seed_words, password):

    print("\nseed_phrase: %s" % " ".join(seed_words))
    password = "secret"
    if password:
        seed_words.append(password)

    # Create bytes-seed
    random.seed(" ".join(seed_words))
    r = random.getrandbits(384)
    seed = r.to_bytes(48, sys.byteorder)

    pk, sk = sphincs.generate_keypair(seed)

    return pk, sk


def v1_address(pk, n_id):

    # Double hash
    pk_hash = sha3(pk).digest()
    pk_hash = bytearray(sha3(pk_hash).digest())

    # Network ID byte header
    pk_hash.insert(0, n_id)

    # Checksum footer
    checksum = sha3(pk_hash).digest()
    checksum = bytearray(sha3(pk_hash).digest())[:4]
    pk_hash.extend(checksum)

    address = base64.b85encode(pk_hash).decode()
    print("address: %s" % address)
    return address
