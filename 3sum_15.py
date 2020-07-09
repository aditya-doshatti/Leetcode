'''
15. 3Sum
Medium

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

https://leetcode.com/problems/3sum/
'''
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums, retVal, i = sorted(nums), [], 0
        while i < len(nums) - 2:
            if i == 0 or nums[i] != nums[i - 1]:
                j, k = i + 1, len(nums) - 1
                while j < k:
                    if nums[i] + nums[j] + nums[k] < 0:
                        j += 1
                    elif nums[i] + nums[j] + nums[k] > 0:
                        k -= 1
                    else:
                        retVal.append([nums[i], nums[j], nums[k]])
                        j, k = j + 1, k - 1
                        while j < k and nums[j] == nums[j - 1]:
                            j += 1
                        while j < k and nums[k] == nums[k + 1]:
                            k -= 1
            i += 1
        return retVal
        # nums.sort()
        # counts = collections.Counter(nums)
        # retVal = []
        # if counts[0] >=3:
        #     retVal.append([0,0,0])
        # dic = defaultdict(list)
        # for i in range(len(nums)):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     else:
        #         for j in range(i+1, len(nums)):
        #             if nums[j] == nums[j-1]:
        #                 continue
        #             dic[nums[i]+nums[j]].append([nums[i],nums[j]])
        # for i in range(len(nums)):
        #     if i > 0 and nums[i] == nums[i-1]:
        #         continue
        #     for ele in dic[0-nums[i]]:
        #         if nums[i] in ele and counts[nums[i]] <=1:
        #             continue
        #         k = sorted(ele + [nums[i]])
        #         if k not in retVal:
        #             retVal.append(k)
        # return retVal
                
