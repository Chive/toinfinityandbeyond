#!/usr/bin/env python
import os

c = 0
while c < 10000:
    with open('count.txt', 'r') as f:
        i = int(f.read())

    with open('count.txt', 'w') as f:
        i += 1
        f.write(str(i))

    os.system('git commit -a -m "to infinity!"')

    c += 1

os.system('git push')