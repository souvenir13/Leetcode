# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 18:32:01 2017

@author: bowen

Q:
    寻找最长回文子串
    Given a string s, find the longest palindromic substring in s.
    You may assume that the maximum length of s is 1000.

Eg:
    Input: "babad"

    Output: "bab"

    Note: "aba" is also a valid answer.
    ------------------------------------------    
    Input: "cbbd"

    Output: "bb"
    
Keywords:
    Dynamic Programming
"""

    
class Solution(object):

    def checkPaliStr(self,start,end,s):
        if (start==end):
            return True
        elif (end==start+1 and s[start]==s[end]):
            return True
        elif (s[start]==s[end] and self.checkPaliStr(start+1,end-1,s)==True):
            return True
        else:
            return False

    def longestPalindrome(self,ss):
        slen = len(ss)
        ansSS = ""
        for i in range(slen):
            for j in range(i,slen):
                if self.checkPaliStr(i,j,ss) == True :
                    if j-i+1>len(ansSS):
                        ansSS = ss[i:j+1]
        return ansSS

    def fib(self,n):
        if n == 0:
            return 0
        if n == 1:
            return 1
        else :
            return self.fib(n-1)+self.fib(n-2)
        
        
ans1 = Solution().longestPalindrome("ababababababab")
ss = "abcde"
#print (ans1.checkPaliStr("babad"))
print (ans1)