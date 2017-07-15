#! /usr/bin/env python3
# -*- coding:utf-8 -*-
def get_number(num):
    if num%2==0:
       return num /2
    else:
       return (3*num+1)/2

num=int(input())
L=[int(i) for i in input().split()]
data=L[:]
for i in data:
    while not i==1:
       i=get_number(i)
       if i in L:
          L.remove(i)
L.sort(reverse=True) 
print(" ".join(str(i) for i in L))   
