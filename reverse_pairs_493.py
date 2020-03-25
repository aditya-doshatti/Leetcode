'''
493. Reverse Pairs
Hard

Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2

https://leetcode.com/problems/reverse-pairs/
'''
class Solution:
    def __init__(self):
        self.retVal = 0 

    def reversePairs(self, nums: List[int]) -> int:
        self.helper(nums)
        return self.retVal
        
    def helper(self, lst):
        if len(lst) <= 1:
            return lst
        else:
            return self.merge(self.helper(lst[:int(len(lst)/2)]), self.helper(lst[int(len(lst)/2):]))
        
    def merge(self, left, right):
        l, r = 0, 0
        while l < len(left) and r < len(right):
            if left[l] <= 2*right[r]:
                l += 1
            else:
                self.retVal += len(left)-l
                r +=1 
        return sorted(left+right)
    
        # Time limit Exceeded
        # n, retVal = len(nums)-1, 0
        # dic = {}
        # for i in range(len(nums)):
        #     #print(dic)
        #     for key in sorted(dic.keys()):
        #         if key >= 2*nums[i]:
        #             retVal += dic[key]
        #             break
        #     temp = nums[i] - 1
        #     for key in sorted(dic.keys()):
        #         if key < temp:
        #             dic[key] += 1
        #         if key > temp:
        #             dic[temp] = dic.get(temp, 0) + 1
        #     dic[temp] = dic.get(temp, 0) + 1
        # return retVal
