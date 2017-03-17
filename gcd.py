#!/usr/bin/env python

import sys

def gcd(x,y):
  while(y):
    x,y = y,x % y
  return int(x)

a = int(sys.argv[1])
b = int(sys.argv[2])

print "GCD: ",gcd(a,b)
print "LCM: ",(a*b)/gcd(a,b)
