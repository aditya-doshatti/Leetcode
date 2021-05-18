'''
1048. Longest String Chain
Medium

Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it equal to word2. For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2, word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.

 

Example 1:

Input: words = ["a","b","ba","bca","bda","bdca"]
Output: 4
Explanation: One of the longest word chain is "a","ba","bda","bdca".

https://leetcode.com/problems/longest-string-chain/
'''
class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        cache = {}
        retVal = 1
        words.sort(key=len)
        for word in words:
            cache[word] = 1
            for i in range(len(word)):
                word_ = word[:i] + word[i+1:]
                if word_ in cache:
                    cache[word] = max(cache[word], cache[word_] + 1)
                    retVal = max(retVal, cache[word])
        return retVal
