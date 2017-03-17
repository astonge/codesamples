#!/usr/bin/env python
import sys
s = 0
MAX = 50

LIST1 = []
LIST2 = []
COMMON = []

for z in range(1,len(sys.argv)):
  if z == 1:
    LIST1.append(int(sys.argv[z]))
  if z == 2:
    LIST2.append(int(sys.argv[z]))
  v = s + int(sys.argv[z])
  for i in range(1, MAX):
    if z == 1:
        LIST1.append(v + int(sys.argv[z]))
    if z == 2:
        LIST2.append(v + int(sys.argv[z]))
    v = v + int(sys.argv[z])

print "LIST1: ",LIST1
print "LIST2: ",LIST2

i = 0
c = 0

for i in range(len(LIST1)):
    for c in range(len(LIST2)):
        if LIST1[i] == LIST2[c]:
            COMMON.append(LIST1[i])

print "COMMON: ",COMMON
