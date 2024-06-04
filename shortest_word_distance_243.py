'''
243. Shortest Word Distance

Easy

Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

 

Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3

https://leetcode.com/problems/shortest-word-distance/description/
'''
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        x, y, retVal = -1, -1, len(wordsDict)
        for i,word in enumerate(wordsDict):
            if word == word1:
                x = i
            if  word == word2:
                y = i
            if x!=-1 and y!=-1:
                retVal = min(retVal, abs(x - y))
        return retVal
