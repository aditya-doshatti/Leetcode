'''
1365. How Many Numbers Are Smaller Than the Current Number
Easy

Given the array nums, for each nums[i] find out how many numbers in the array are smaller than it. That is, for each nums[i] you have to count the number of valid j's such that j != i and nums[j] < nums[i].

Return the answer in an array.

 

Example 1:

Input: nums = [8,1,2,2,3]
Output: [4,0,1,1,3]
Explanation: 
For nums[0]=8 there exist four smaller numbers than it (1, 2, 2 and 3). 
For nums[1]=1 does not exist any smaller number than it.
For nums[2]=2 there exist one smaller number than it (1). 
For nums[3]=2 there exist one smaller number than it (1). 
For nums[4]=3 there exist three smaller numbers than it (1, 2 and 2).

https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
'''
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_list = nums[::]
        sorted_list.sort()
        dic, k = {}, 0
        for i in range(0,len(sorted_list)):
            if i == 0:
                dic[sorted_list[i]] = 0
            elif sorted_list[i-1] != sorted_list[i]:
                dic[sorted_list[i]] = k
            k += 1
        retVal = []
        for num in nums:
            retVal.append(dic[num])
        return retVal
