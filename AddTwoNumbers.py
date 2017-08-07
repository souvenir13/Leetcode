# -*- coding: utf-8 -*-
"""
Created on Sat Aug  5 17:34:17 2017

@author: bowen
"""

'''
Keywords: 链表LinkList,结点Node,leetcode_Add_Two_Numbers 
Reference: 
    http://www.cnblogs.com/yupeng/p/3413763.html
    http://zhaochj.github.io/2016/05/12/2016-05-12-%E6%95%B0%E6%8D%AE%E7%BB%93%E6%9E%84-%E9%93%BE%E8%A1%A8/
'''

# Definition for singly-linked list.
class Node:
    def __init__(self, x):
        self.val = x
        self.next = None
        
class LinkList(object):
    def __init__(self,x):
        self.head = Node(x)
    
    def append(self,item):
        q = Node(item)
        if self.head == None:
            self.head = q
        else:
            p = self.head
            while p.next!=None:
                p = p.next
            p.next = q
        
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        root = n = Node(0)
        carry = 0
        while l1 or l2 or carry:
            v1=v2=0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry,val = divmod(v1+v2+carry,10)
            n.next = Node(val)
            n = n.next
        return root.next

if __name__ == '__main__':
    #新建链表list1:7->8->2
    list1 = LinkList(7)
    list1.append(8)
    list1.append(2)
    #新建链表list1:3->2->1
    list2 = LinkList(3)
    list2.append(2)
    list2.append(1)
    sumOfTwoNum = Solution()
    #2 8 7 + 1 2 3 = 4 1 0, 返回 0->1->4
    result = sumOfTwoNum.addTwoNumbers(list1.head,list2.head)

    n = m = Node(0)# n 和 m 都指向同一个地址，改地址存放一个Node实例
    a = Node(1)
    b = a # b 和 a 都指向同一个地址



