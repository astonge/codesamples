#!/usr/bin/env python

for num in range(2,3000+1):
  for i in range(2, num):
    if (num % i) == 0:
      break
  else:
    print num,
