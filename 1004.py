#! /usr/bin/env python3
# -*- coding: utf-8 -*-
import re
L=[]
standard=re.compile(r'([\w]+)[\s]+([\w]+)[\s]+([0-9]+)')
num=int(input())
while num>0:
   L.append(re.search(standard,input()).groups())
   num=num-1
L=sorted(L,key=lambda t: int(t[2]),reverse=True)
print(L[0][0],L[0][1])
print(L[-1][0],L[-1][1])
