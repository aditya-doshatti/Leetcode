'''
139. Word Break
Medium

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".

https://leetcode.com/problems/word-break/
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if not s:
            return False
        found = [0]
        while (found):
            temp = found.pop(0)
            if temp == len(s):
                return True
            for word in wordDict:
                if s[temp:].startswith(word):
                    end = temp+len(word)
                    if end not in found:
                        found.append(end)
        return False
        # dp = [False for a in range(len(s)+1)]
        # dic = {}
        # for word in wordDict:
        #     dic[word] = len(word)
        # dp[0] = True
        # for i in range(1,len(s)+1):
        #     for word, l in dic.items():
        #         if s[i-l:i]==word and dp[i-l]:
        #             dp[i] = True
        # return dp[-1]
        # Time limit Exceeded
        # dic = {}
        # for word in wordDict:
        #     dic[word] = 1
        # found, i, dp = [0], 0, [False for a in range(len(s))]
        # while found:
        #     i = found.pop(0)
        #     prev = i
        #     while i <len(s):
        #         if s[prev:i+1] in dic:
        #             found.append(i+1)
        #             dp[i] = True
        #         i+=1
        # return dp[-1]
