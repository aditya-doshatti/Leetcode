'''
179. Largest Number
Medium

Given a list of non negative integers, arrange them such that they form the largest number.

Example 1:

Input: [10,2]
Output: "210"

https://leetcode.com/problems/largest-number/
'''
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        strList = []
        for i in nums:
            strList.append(str(i))
        retVal = ''.join(sorted(strList, key=cmp_to_key(lambda x,y : 1 if x+y<y+x else -1)))
        if retVal[0] != "0":
            return retVal
        return "0"
