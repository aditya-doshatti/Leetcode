'''
1004. Max Consecutive Ones III
Medium

Given an array A of 0s and 1s, we may change up to K values from 0 to 1.

Return the length of the longest (contiguous) subarray that contains only 1s. 

 

Example 1:

Input: A = [1,1,1,0,0,0,1,1,1,1,0], K = 2
Output: 6
Explanation: 
[1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1.  The longest subarray is underlined.

https://leetcode.com/problems/max-consecutive-ones-iii/
'''
class Solution(object):
    def longestOnes(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        i, j = 0, 0
        while j < len(A):
            if A[j] == 0:
                K -=1
            if K < 0:
                if A[i] == 0:
                    K +=1
                i +=1
            j+=1
        return len(A)-i
        # TLE Solution
        # i, retVal = 0, 0
        # while i < len(A):
        #     curr = K
        #     j = i
        #     first, zero = True, i
        #     while j < len(A):
        #         if A[j] == 1:
        #             j += 1
        #         elif curr > 0:
        #             if first:
        #                 zero = j
        #                 first = False
        #             j += 1
        #             curr -= 1
        #         else:
        #             break
        #     retVal = max(retVal, j-i)
        #     # print(retVal, i, j, zero, first)
        #     if zero == i:
        #         i += 1
        #     else:
        #         i = zero
        # return retVal
