'''
506. Relative Ranks
Easy

Given scores of N athletes, find their relative ranks and the people with the top three highest scores, who will be awarded medals: "Gold Medal", "Silver Medal" and "Bronze Medal".

Example 1:
Input: [5, 4, 3, 2, 1]
Output: ["Gold Medal", "Silver Medal", "Bronze Medal", "4", "5"]
Explanation: The first three athletes got the top three highest scores, so they got "Gold Medal", "Silver Medal" and "Bronze Medal". 
For the left two athletes, you just need to output their relative ranks according to their scores.

https://leetcode.com/problems/relative-ranks/
'''
class Solution:
    def findRelativeRanks(self, nums: List[int]) -> List[str]:
        orig = nums[::]
        nums.sort(reverse = True)
        dic = {}
        if nums[0]:
            dic[nums[0]] = 'Gold Medal'
            if len(nums) > 1:
                dic[nums[1]] = 'Silver Medal'
                if len(nums) > 2:
                    dic[nums[2]] = 'Bronze Medal'
                    rank = 4
                    if len(nums) > 3:
                        for val in nums[3:]:
                            dic[val] = str(rank)
                            rank +=1 
        retVal = []
        for val in orig:
            retVal.append(dic[val])
        return retVal
