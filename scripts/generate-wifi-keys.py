#!/usr/bin/env python3

import random
import string
import sys

LENGTH = 10
CHARACTERS = (string.ascii_letters + string.digits) * 5 + string.punctuation.replace('"', '')

print("Input TLAs (then press Ctrl+D for end)", file=sys.stderr)

for line in sys.stdin.readlines():
    tla = line.strip().upper()
    if not tla:
        break
    password = "".join(random.choice(CHARACTERS) for _ in range(LENGTH))
    print('{}: "{}"'.format(tla, password))
