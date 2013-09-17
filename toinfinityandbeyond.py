#!/usr/bin/env python
import os

c = 0
while c < 100:
    with open('count.txt', 'r') as f:
        i = int(f.read())

    with open('count.txt', 'w') as f:
        i += 1
        f.write(str(i))

    os.system('git commit -a -m "to infinity!"')
    os.system('git push')

    c += 1
