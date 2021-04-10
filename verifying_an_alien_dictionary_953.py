'''
953. Verifying an Alien Dictionary
Easy

In an alien language, surprisingly they also use english lowercase letters, but possibly in a different order. The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language, and the order of the alphabet, return true if and only if the given words are sorted lexicographicaly in this alien language.

 

Example 1:

Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language, then the sequence is sorted.

https://leetcode.com/problems/verifying-an-alien-dictionary/
'''
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for index, val in enumerate(order):
            dic[val] = index
        for i in range(len(words) - 1):
            for j in range(len(words[i])):
                if j >= len(words[i + 1]):
                    return False
                if words[i][j] != words[i + 1][j]:
                    if dic[words[i][j]] > dic[words[i + 1][j]]:
                        return False
                    break
        return True
