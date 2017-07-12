#! /usr/bin/env python3
# -*- coding:utf-8 -*-
count=0
n=input()
n=int(n)
while n>1:
    if n%2==0:
        n=n//2  
        count=count+1
    else:
        n=(3*n+1)//2
        count=count+1
print(count)
