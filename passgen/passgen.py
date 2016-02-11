#!/usr/bin/python
from random import randint
import sys

# generate a 16 char password.

for x in range(16):
	sys.stdout.write(chr(randint(33,126)))
print " "
