'''
47. Permutations II
Medium

Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations in any order.

 

Example 1:

Input: nums = [1,1,2]
Output:
[[1,1,2],
 [1,2,1],
 [2,1,1]]

https://leetcode.com/problems/permutations-ii/
'''
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        retVal = []
        def helper(curr, dic):
            if len(curr) == len(nums):
                retVal.append(list(curr))
                return
            for num in dic:
                if dic[num] > 0:
                    curr.append(num)
                    dic[num] -= 1
                    helper(curr, dic)
                    curr.pop()
                    dic[num] += 1
        helper([], Counter(nums))
        return retVal
