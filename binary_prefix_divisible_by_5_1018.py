'''
1018. Binary Prefix Divisible By 5
Easy

Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number (from most-significant-bit to least-significant-bit.)

Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.

Example 1:

Input: [0,1,1]
Output: [true,false,false]
Explanation: 
The input numbers in binary are 0, 01, 011; which are 0, 1, and 3 in base-10.  Only the first number is divisible by 5, so answer[0] is true.

https://leetcode.com/problems/binary-prefix-divisible-by-5/
'''
class Solution(object):
    def prefixesDivBy5(self, A):
        """
        :type A: List[int]
        :rtype: List[bool]
        """
        retVal = []
        tempVal, i = 0, 0
        for val in A:
            tempVal = (tempVal << 1)
            if val:
                 tempVal += 1
            if tempVal % 5:
                retVal.append(False)
            else:
                retVal.append(True)
        return retVal
        # retVal = []
        # tempVal, i = 0, 0
        # for val in A:
        #     tempVal = 2*tempVal +val
        #     if tempVal % 5:
        #         retVal.append(False)
        #     else:
        #         retVal.append(True)
        # return retVal
        # retVal = []
        # i, tempVal, tempStr = 0, 0, ''
        # for val in A:
        #     tempStr += str(val)
        #     tempVal = int(tempStr, 2)
        #     if tempVal % 5:
        #         retVal.append(False)
        #     else:
        #         retVal.append(True)
        #     i += 1
        # return retVal
