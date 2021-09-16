'''
978. Longest Turbulent Subarray
Medium

Given an integer array arr, return the length of a maximum size turbulent subarray of arr.

A subarray is turbulent if the comparison sign flips between each adjacent pair of elements in the subarray.

More formally, a subarray [arr[i], arr[i + 1], ..., arr[j]] of arr is said to be turbulent if and only if:

For i <= k < j:
arr[k] > arr[k + 1] when k is odd, and
arr[k] < arr[k + 1] when k is even.
Or, for i <= k < j:
arr[k] > arr[k + 1] when k is even, and
arr[k] < arr[k + 1] when k is odd.
 

Example 1:

Input: arr = [9,4,2,10,7,8,8,1,9]
Output: 5
Explanation: arr[1] > arr[2] < arr[3] > arr[4] < arr[5]

https://leetcode.com/problems/longest-turbulent-subarray/
'''
class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) <= 1:
            return len(arr)
        if len(set(arr)) <= 1:
            return len(set(arr)) 
        gt = arr[0] > arr[1]
        retVal, j, curr = 2, 1, 2
        while j < len(arr)-1:
            #print(retVal, curr, j)
            if gt and arr[j] < arr[j+1]:
                gt = False
                curr += 1
            elif not gt and arr[j] > arr[j+1]:
                gt = True
                curr += 1
            else:
                retVal = max(retVal, curr)
                curr = 2
                while j < len(arr)-1 and arr[j] == arr[j+1]:
                    j += 1
                if j < len(arr)-1:
                    gt = arr[j] > arr[j+1]
            j += 1
        retVal = max(retVal, curr)
        return retVal
