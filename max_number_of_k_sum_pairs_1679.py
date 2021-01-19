'''
1679. Max Number of K-Sum Pairs
Medium

You are given an integer array nums and an integer k.

In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.

Return the maximum number of operations you can perform on the array.

 

Example 1:

Input: nums = [1,2,3,4], k = 5
Output: 2
Explanation: Starting with nums = [1,2,3,4]:
- Remove numbers 1 and 4, then nums = [2,3]
- Remove numbers 2 and 3, then nums = []
There are no more pairs that sum up to 5, hence a total of 2 operations.

https://leetcode.com/problems/max-number-of-k-sum-pairs/
'''
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        c, retVal = Counter(nums), 0
        for key,val in c.items():
            if key * 2 == k:
                retVal += math.floor(c[key]/2)
            elif key <= k/2:
                if k - key in c:
                    retVal += min(c[key],c[k-key])
            # while c[key] > 0:
            #     if k-key in c:
            #         if c[key] > 0:
            #             c[key] -= 1
            #         else:
            #             break
            #         if c[k-key] > 0:
            #             c[k-key] -= 1
            #         else:
            #             break
            #         retVal += 1
            #     else:
            #         break
        return retVal
