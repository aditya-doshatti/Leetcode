'''
140. Word Break II
Hard

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

https://leetcode.com/problems/word-break-ii/
'''
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordLets = set(''.join(wordDict))
        wordDict = set(wordDict) #Fast lookup
        stringLets = set(s)
        if stringLets - wordLets:
            return []
        retVal = []
        n = len(s)
        def dfs(temp = [], index = 0):
            if index == n:
                retVal.append(' '.join(temp))
                return
            for i in range(index, n+1):
                if s[index:i] in wordDict:
                    dfs(temp+[s[index:i]], i)
        dfs()
        return retVal
