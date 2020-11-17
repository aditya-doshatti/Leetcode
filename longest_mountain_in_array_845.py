'''
845. Longest Mountain in Array
Medium

Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.

https://leetcode.com/problems/longest-mountain-in-array/
'''
class Solution:
    def longestMountain(self, A: List[int]) -> int:
        retVal = temp = 0
        while temp < len(A):
            end = temp
            if end +1 < len(A) and A[end] < A[end + 1]:
                while end + 1 < len(A) and A[end] < A[end+1]:
                    end += 1
                if end + 1 < len(A) and A[end] > A[end+1]:
                    while end + 1 < len(A) and A[end] > A[end+1]:
                        end += 1
                    retVal = max(retVal, end-temp + 1)
            temp = max(end, temp +1)
        return retVal
