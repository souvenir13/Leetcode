# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 15:48:04 2017

@author: bowen

面试题
input:一串数组
output:重新排序的等差数列，未能成为等差数列的返回-1
"""

def checkArray(count,lists):
    '''
    count:length of lists
    lists:[array]
    思路：冒泡排序，每遍历获得最大值，加入一个新数组，
          加入前先进行判断，是否能使数列成为等差数列
    '''
    list_esort = []
    for i in range(0, count):
        for j in range(0, count-i-1):
            if lists[j]>lists[j+1]:  
                temp = lists[j]  
                lists[j] = lists[j+1]  
                lists[j+1] = temp 
        if len(list_esort)<2:
            list_esort.append(lists[count-i-1])
        else:
            if lists[count-i-1]-list_esort[-1]==list_esort[-1]-list_esort[-2]:
                list_esort.append(lists[count-i-1])
            else:
                return -1
    return lists

if __name__ == "__main__":
    print(checkArray(4,[5,7,3,9]))