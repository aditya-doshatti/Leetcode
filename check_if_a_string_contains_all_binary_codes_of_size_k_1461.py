'''
1461. Check If a String Contains All Binary Codes of Size K
Medium

Given a binary string s and an integer k.

Return True if every binary code of length k is a substring of s. Otherwise, return False.

 

Example 1:

Input: s = "00110110", k = 2
Output: true
Explanation: The binary codes of length 2 are "00", "01", "10" and "11". They can be all found as substrings at indicies 0, 1, 3 and 2 respectively.

https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/
'''
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        required = 2 ** k
        done = set()
        for i in range(k, len(s)+1):
            temp = s[i-k:i]
            if temp not in done:
                done.add(temp)
                required -=1 
                if required == 0:
                    return True
        return False
        # if len(s) < k:
        #     return False
        # for i in range(2 **k):
        #     binary = str(bin(i)[2:])
        #     checkVal = '0'*(k-len(binary)) + binary
        #     if checkVal in s:
        #         continue
        #     else:
        #         return False
        # return True
