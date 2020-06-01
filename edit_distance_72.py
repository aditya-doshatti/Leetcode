'''
72. Edit Distance
Hard

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character
Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

https://leetcode.com/problems/edit-distance/

https://en.wikipedia.org/wiki/Edit_distance
'''
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        word1, word2 = "!" + word1, "!" + word2
        len1, len2 = len(word1), len(word2)
        dp = [[0] * len2 for _ in range(len1)]

        for i in range(len1): dp[i][0] = i
        for i in range(len2): dp[0][i] = i

        for i in range(1, len1):
            for j in range(1,len2):
                diff = (word1[i] != word2[j])
                dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + diff)

        return int(dp[-1][-1])
