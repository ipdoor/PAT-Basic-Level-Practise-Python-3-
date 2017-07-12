#! /uer/bin/env python3
# -*- coding:utf-8 -*-
import re
re_match=re.compile(r'[A]*PA+T*');
number=int(input())
L=[]
while number>0:
      n=input()
      st=re.search('T',n)
      sp=re.search('P',n)
      if re.search(re_match,n) \
      and not re.findall(r'[^PAT]',n) \
      and st \
      and sp \
      and (len(n)-1- st.start()) == sp.start()*(st.start()-sp.start()-1):
       L.append('YES')
      else: 
       L.append('NO')
      number -=1
print('\n'.join(L))

