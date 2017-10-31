# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 20:18:02 2017

@author: bowen
"""

def findNum(a,n):
    b = sorted(a)
    flag = 1
    res = []
    for i in range(n):
        for j in range(i+1,n):
            if b[j]%b[i] == 0:
                flag = 0
        if flag == 1:
            res.append(b[i])
            print (b[i])
    if flag == 1:
        return sorted(res)
    else:
        return -1

if __name__ == '__main__':
    num = int(input("n input:"))
    line = input("l input:")
    array = list(map(int,line.split()))
    ans = findNum(array,num)
    print (ans)
