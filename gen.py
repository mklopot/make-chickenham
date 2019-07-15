#!/usr/bin/python3.6

import math
import sys
import secrets
import pycoin
import itertools
import reedsolo
import split
import combine
from pycoin.symbols.btc import network

threshold = int(sys.argv[1])
number = int(sys.argv[2])

seed = '0'
while int(seed, 16) < 1 or int(seed, 16) >  0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364140:
    seed = secrets.token_hex(32)

splitter = split.Splitter(threshold, number)
shares = splitter(seed)

combos = itertools.combinations(shares, threshold)
combiner = combine.Combiner(threshold)
i = 0
num_combos = int(math.factorial(number) / (math.factorial(threshold) * math.factorial(number - threshold)))
for combo in combos:
    i += 1
    print("{}Validating {} of {}".format("\b"*50, i, num_combos), end="", flush=True)
    if combiner(combo) != seed:
        raise ValueError("Failed validating split shares")

addr = network.keys.private(secret_exponent=int(seed, 16)).address()
del seed

print("\n\n")

rs = reedsolo.RSCodec(10)
for share in shares:
    if not len(share) % 2:
        share = "0" + share
    pos = share.index("-")
    share = share.replace('-', "")
    encoded = rs.encode(bytes.fromhex(share)).hex()
    with_dash = encoded[:pos] + "-" + encoded[pos:]
    print(with_dash.upper())
print("\nAddress:")
print(addr)
