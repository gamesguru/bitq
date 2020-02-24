import base64
from hashlib import sha3_256 as sha3


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
