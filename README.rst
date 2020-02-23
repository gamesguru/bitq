******
 bitq
******

A bitcoin gen3 protocol written in python.

Our features

- SHA-3 proof of work algorithm

- shake_256 tx and block signatures

- SHA-3 tx and block hashes

- 4 MB blocks and 2 minute windows

- Segwit and bech32 compatibility

Config and KeyGen
#################

Generate a key with a call such as

.. code-block :: python3

    import json
    import os
    import pyspx.shake256_128s as sphincs
    seed = os.urandom(sphincs.crypto_sign_SEEDBYTES)
    pk, sk = sphincs.generate_keypair(seed)
    print(json.dumps({"pk": pk.hex(), "sk": sk.hex()}, indent=2))


This can be accomplished with the ``test_gen_wallet`` test.

Save a ``.qcconfig`` file in your user folder.

.. code-block :: json

    {
        "pk": "7e6c5d688fc87f7244e93bd832baae4cb77f1d6673de1e4d7a5e02b5187d054a",
        "sk": "1dc1919a60100dfe494c0938f0f4c9d3263a1e17487dc6b1695022b2abffd4807e6c5d688fc87f7244e93bd832baae4cb77f1d6673de1e4d7a5e02b5187d054a"
    }

You will use these keys to access your wallet in early versions.

The user folder can be found at,

.. code-block ::

    C:\Users\Shane     [Windows]
    /Users/shane       [macOS]
    /home/shane        [Linux]

Sending Payments
################

The command for sending is

``qc send fa547cafff6351e1ff5bdcaa209c116a6d12be439de47350b86d6b75513a6bca 0.0001``

You will be asked to confirm and unlock your secret key.

Mining
######

The command line is currently designed for single user.

RandomX favors consumer CPUs.
We may test GPU-specific algos also.

To set your machine to mine, simply run

``qc mine``

If it has any issue connecting or finding peers,
you will be alerted within seconds.

Once peers are established payments can be processed,
and blocks can be mined, appended, and broadcast.

Peers DB
########

Can be manually managed or inspected through postgres.

TODO: this
