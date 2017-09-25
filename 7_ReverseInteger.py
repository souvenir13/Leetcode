# -*- coding: utf-8 -*-
"""
Created on Mon Aug 28 12:45:38 2017

@author: bowen

Q:
    颠倒数字
    Reverse digits of an integer.

Eg：
    Example1: x = 123, return 321
    Example2: x = -123, return -321
    Example3: x = 901000, return 109
Note:
    以0为结尾的数字。
    规定输入不能超过32位int：32位整数-2^31~2^31-1,即-2147483648到2147 483 647
"""

class Solution(object):
    
    def reverse(self, x):
        if x>=0:
            sign = 1
        else:
            sign = -1
            x = -x
        xs = str(x)
        ans = int(xs[::-1])
        return sign * ans * (ans<pow(2,31))
    
ans = Solution().reverse(-153469)
print(ans)