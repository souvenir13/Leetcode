# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 22:49:07 2017

@author: bowen

Kewords：时间复杂度,Hash Map
"""

class Solution1(object):
    '''
    简单粗暴法
    O(n2)
    '''
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<=1:
            return 0
        for i in range(len(nums)):
            ind1 = i
            left = target - nums[i]
            for j in range(i+1,len(nums)):
                if nums[j]==left:
                    ind2 = j
                    return [ind1,ind2]
                else:
                    continue
        return 0

class Solution2(object):
    '''
    一次哈希法
    O(n)
    '''
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums)<=1:
            return 0
        num_ind_dict = {}
        for i in range(len(nums)):
            if nums[i] in num_ind_dict:
                return [num_ind_dict[nums[i]],i]
            else :
                num_ind_dict[target-nums[i]] = i
        return 0
s1 = Solution1()
s2 = Solution2()
print (s2.twoSum([-1,-2,-4,-5],-9))