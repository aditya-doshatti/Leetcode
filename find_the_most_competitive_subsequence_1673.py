'''
1673. Find the Most Competitive Subsequence
Medium

Given an integer array nums and a positive integer k, return the most competitive subsequence of nums of size k.

An array's subsequence is a resulting sequence obtained by erasing some (possibly zero) elements from the array.

We define that a subsequence a is more competitive than a subsequence b (of the same length) if in the first position where a and b differ, subsequence a has a number less than the corresponding number in b. For example, [1,3,4] is more competitive than [1,3,5] because the first position they differ is at the final number, and 4 is less than 5.

 

Example 1:

Input: nums = [3,5,2,6], k = 2
Output: [2,6]
Explanation: Among the set of every possible subsequence: {[3,5], [3,2], [3,6], [5,2], [5,6], [2,6]}, [2,6] is the most competitive.

https://leetcode.com/problems/find-the-most-competitive-subsequence/
'''
class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        skip = len(nums) - k
        stack = []
        for i in range(len(nums)):
            while stack and nums[i] < stack[-1] and skip > 0:
                stack.pop()
                skip -= 1
            if skip == 0:
                stack += nums[i:]
                break
            stack.append(nums[i])
        return stack[:k]
        # retVal = []
        # dic = defaultdict(list)
        # for i in range(len(nums)):
        #     dic[nums[i]].append(i)
        # for key in sorted(dic.keys()):
        #     for j in range(len(dic[key])-1, -1, -1):
        #         if dic[key][j] - k > 0:
        #             retVal.append(key)
        # print(dic, retVal)
        # return []
