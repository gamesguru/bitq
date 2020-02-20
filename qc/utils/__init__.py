import json
import os
import requests
from decimal import getcontext

ip = requests.get("https://api.ipify.org").text

getcontext().prec = 100

# Signing key
config = json.load(open(os.path.join(os.path.expanduser("~"), ".qcconfig")))
pk = config["pk"]
sk = config["sk"]
