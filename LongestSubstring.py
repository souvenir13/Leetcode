# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 16:48:20 2017

@author: bowen

Problem:
    寻找最长无重复子串
Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without 
repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence
and not a substring.

Keywords: Hashmap

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        
        idea:Sliding Window
        一格一格地移动开始位置
        """
        substrArray = []
        slen = len(s)
        start = 0 
        end = 0
        maxlen = 0
        while (start < slen) and (end < slen):
            if not s[end] in substrArray:
                substrArray.append(s[end])
                end = end + 1
                maxlen = max(maxlen,end-start)
            else:
                substrArray.remove(s[start])
                start = start + 1

        return maxlen
        
    def method2(self,s):
        """
        :type s: str
        :rtype: int
        
        idea:Hash Map
        直接移动至所在索引的下一个位置
        """
        substrDict = {}
        slen = len(s)
        maxlen = 0
        start = 0
        for j in range(slen):
            if s[j] in substrDict:
                start = max(substrDict[s[j]],start)
            maxlen = max(maxlen,j-start+1)
            substrDict[s[j]] = j+1
        return maxlen
        
        
        
s1 = Solution()
print(s1.method2("jbpnbwwd"))

















