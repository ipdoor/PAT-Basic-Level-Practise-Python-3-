#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = input()
d = {'0': 'ling',
     '1': 'yi',
     '2': 'er',
     '3': 'san',
     '4': 'si',
     '5': 'wu',
     '6': 'liu',
     '7': 'qi',
     '8': 'ba',
     '9': 'jiu'}
total = sum([int(i) for i in n])
print(' '.join([d[i] for i in str(total)]))
