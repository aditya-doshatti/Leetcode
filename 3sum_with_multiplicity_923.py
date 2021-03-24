'''
923. 3Sum With Multiplicity
Medium

Given an integer array arr, and an integer target, return the number of tuples i, j, k such that i < j < k and arr[i] + arr[j] + arr[k] == target.

As the answer can be very large, return it modulo 109 + 7.

 

Example 1:

Input: arr = [1,1,2,2,3,3,4,4,5,5], target = 8
Output: 20
Explanation: 
Enumerating by the values (arr[i], arr[j], arr[k]):
(1, 2, 5) occurs 8 times;
(1, 3, 4) occurs 8 times;
(2, 2, 4) occurs 2 times;
(2, 3, 3) occurs 2 times.

https://leetcode.com/problems/3sum-with-multiplicity/
'''
class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        retVal = 0
        l2 = collections.defaultdict(int)
        for i in range(2, len(arr)):
            #print(l2)
            for j in range(i-1):
                l2[arr[j] + arr[i-1]] += 1
            retVal = retVal + l2[target - arr[i]]
            retVal = retVal % (10**9 + 7)
        return retVal
