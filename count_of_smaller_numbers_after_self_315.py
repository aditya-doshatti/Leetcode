'''
315. Count of Smaller Numbers After Self
Hard

You are given an integer array nums and you have to return a new counts array. The counts array has the property where counts[i] is the number of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0] 
Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.

https://leetcode.com/problems/count-of-smaller-numbers-after-self/
'''
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
	'''
        This solution is TLE for 1 test case have a solution of traversing reverse in mind might work better
	'''
        retVal, count = [], 0
        for i in range(len(nums)):
            count = 0
            for j in range(i+1,len(nums)):
                if nums[i] > nums[j]:
                    count += 1
            retVal.append(count)
        return retVal
        # retVal, count = [], 0
        # for i in range(1,len(nums)):
        #     if nums[i]<nums[0]:
        #         count+=1
        # retVal.append(count)
        # for i in range(1, len(nums)):
        #     if nums[i] > nums[0]:
        #         retVal.append(retVal[0]-i)
        #     else:
        #         currCount = 0
        #         for j in range(i,len(nums)):
        #             if nums[j] < nums[i]:
        #                 currCount +=1
        #         retVal.append(currCount)
        # return retVal
