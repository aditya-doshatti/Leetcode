'''
1658. Minimum Operations to Reduce X to Zero
Medium

You are given an integer array nums and an integer x. In one operation, you can either remove the leftmost or the rightmost element from the array nums and subtract its value from x. Note that this modifies the array for future operations.

Return the minimum number of operations to reduce x to exactly 0 if it's possible, otherwise, return -1.

 

Example 1:

Input: nums = [1,1,4,2,3], x = 5
Output: 2
Explanation: The optimal solution is to remove the last two elements to reduce x to zero.

https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
'''
class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total=sum(nums)
        if total<x:
            return -1
        if total==x:
            return len(nums)
        target=total-x
        curr=0
        retVal=-1
        i=j=0
        for a in nums:
            curr+=a
            j+=1
            while curr>target:
                curr-=nums[i]
                i+=1
                j-=1
            if curr==target and j>retVal:
                retVal=j
        return -1 if retVal==-1 else len(nums)-retVal
        # b, e, abadB, abadE, retVal = 0 , len(nums) -1, False, False, 0
        # while x > 0:
        #     print(b, e, abadB, abadE, retVal, x)
        #     if not abadB:
        #         if e >= b:
        #             if nums[b] >= nums[e] or abadE:
        #                 if x-nums[b] >= 0:
        #                     x = x-nums[b]
        #                     retVal += 1
        #                     b += 1
        #                 else:
        #                     abadB = True
        #         else:
        #             abadB = True
        #     if not abadE:
        #         if b <= e:
        #             if nums[e] >= nums[b] or abadB:
        #                 if x - nums[e] >= 0:
        #                     x = x- nums[e]
        #                     retVal += 1
        #                     e -= 1
        #                 else:
        #                     abadE = True
        #         else:
        #             abadE = True
        #     if abadE and abadB:
        #         return -1
        # return retVal
