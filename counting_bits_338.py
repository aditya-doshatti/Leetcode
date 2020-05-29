'''
338. Counting Bits
Medium

Given a non negative integer number num. For every numbers i in the range 0 ≤ i ≤ num calculate the number of 1's in their binary representation and return them as an array.

Example 1:

Input: 2
Output: [0,1,1]

https://leetcode.com/problems/counting-bits/
'''
class Solution:
    def countBits(self, num: int) -> List[int]:
        retVal = [0] * (num+1)
        for val in range(num+1):
            if val % 2:
                retVal[val] = retVal[val-1] + 1
            else:
                retVal[val] = retVal[val//2]
        return retVal
        # retVal = []
        # for val in range(num+1):
        #     k = str(bin(val))[2:]
        #     retVal.append(k.count('1'))
        # return retVal
