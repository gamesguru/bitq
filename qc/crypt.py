import base64
import random
import sys
from hashlib import sha3_256 as sha3

import pyspx.shake256_128s as sphincs


def generate_keypair(seed_words, password, offset=0):

    print("\nseed_phrase: %s" % " ".join(seed_words))
    if password:
        print("password:    yes")
        seed_words.append(password)

    # Create bytes-seed
    random.seed(" ".join(seed_words))
    r = random.getrandbits(384)
    r += offset
    seed = r.to_bytes(48, sys.byteorder)

    pk, sk = sphincs.generate_keypair(seed)

    return pk, sk


def pk2address(pk, version, n_id=0x00):

    # Meta data
    header = "v%i" % (version)

    # PK hash
    pk_hash = sha3(pk).hexdigest()

    # Address
    address = "_".join([header, pk_hash])

    # Checksum
    checksum = sha3(address.encode()).digest()[:4]
    address = "_".join([address, checksum.hex()])

    print("address: %s" % address)
    return address


def verify_address(address):
    parts = address.split("_")
    meta = parts[0]
    data = parts[1]
    checksum = parts[2]

    def verify_checksum(stub, checksum):
        return sha3(stub.encode()).digest()[:4].hex() == checksum

    if meta == "v1":
        stub = "_".join([meta, data])
        if not verify_checksum(stub, checksum):
            return False, "checksum failure, check address"
        return True, None
    else:
        return False, "unknown address type"
