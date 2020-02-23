import json
import os
import requests
from decimal import getcontext

ip = requests.get("https://api.ipify.org").text

getcontext().prec = 100

# Signing key
try:
    config = json.load(open(os.path.join(os.path.expanduser("~"), ".qcconfig")))
    pk = config["pk"]
    sk = config["sk"]
except:
    print('warn: no file "~/.qcconfig"')
    pk = os.environ["QCWALLET_PUBLIC_KEY"]
    sk = os.environ["QCWALLET_SECRET_KEY"]
