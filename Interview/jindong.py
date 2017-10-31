# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 19:52:36 2017

@author: bowen
"""
import math

def method(n):
#    if n<1 or n>pow(10,18):
#        return -1
#    n = int(sys.stdin.readline().strip())
    if n<1 or n>1000000000000000000:
        print(0)
    ans = int(math.sqrt(2*n))
    while ( ans*ans + ans - 2*n < 0):
        ans += 1
    print(ans)
    return ans


def method2(n):
#    if n<1 or n>pow(10,18):
#        return -1
#    n = int(sys.stdin.readline().strip())
    if n<1 or n>1000000000000000000:
        print(0)
    ans = int(math.sqrt(2*n))
    while ( ans*ans + ans - 2*n < 0):
        ans += 1
    print(ans)
    return ans


def method3(n):
    if n == 1:
        print (1)
    a = []
    a.append(1)
    w2=0
    w3=0
    w5=0
    for i in range(n):
        t = min(a[w2]*2,min(a[w3]*3,a[w5]*5))
        if t == a[w2]*2:
            w2 += 1
        if t == a[w3]*3:
            w3 += 1
        if t == a[w5]*5:
            w5 += 1
        a.append(t)
    print (a[n-1])
    
method3(6)
    