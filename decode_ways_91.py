'''
91. Decode Ways
Medium

A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

https://leetcode.com/problems/decode-ways/
'''
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s)+1)]
        dp [0] = 1
        dp[1] = 1 if '0' < s[0] <='9' else 0
        # print(dp)
        for i in range(2, len(s)+1):
            if '0' < s[i-1] <= '9':
                dp[i] += dp[i-1]
            if s[i-2] !='0'  and int(s[i-2:i]) < 27:
                dp[i] += dp[i-2]
            # print(dp)
        return dp[-1]
        # Non dp solution failed for 1212 not considering 12,12
        # i, retVal =0, 0
        # if len(s) == 1 and s[i] != '0':
        #     return 1            
        # while i < len(s)-1:
        #     if s[i] == '0' and s[i-1] > '2':
        #         return 0
        #     if int(s[i:i+2]) < 27:
        #         retVal +=1
        #     i+=1
        # return retVal+1 if retVal else 0
