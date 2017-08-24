# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 16:48:20 2017

@author: bowen

Problem:
Longest Substring Without Repeating Characters

Given a string, find the length of the longest substring without 
repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. 
Note that the answer must be a substring, "pwke" is a subsequence
and not a substring.

"""

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        
        idea:Sliding Window
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
        
s1 = Solution()
print(s1.lengthOfLongestSubstring("jbpnbwwd"))

















