'''
884. Uncommon Words from Two Sentences
Solved
Easy
Topics
Companies
A sentence is a string of single-space separated words where each word consists only of lowercase letters.

A word is uncommon if it appears exactly once in one of the sentences, and does not appear in the other sentence.

Given two sentences s1 and s2, return a list of all the uncommon words. You may return the answer in any order.

 

Example 1:

Input: s1 = "this apple is sweet", s2 = "this apple is sour"
Output: ["sweet","sour"]
https://leetcode.com/problems/uncommon-words-from-two-sentences/description/
'''
from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        retVal = []
        s = s1 + " " + s2
        counter_s = Counter(s.split(" "))
        for word, count in counter_s.items():
            if count == 1:
                retVal.append(word)
        return retVal
        '''
        counter_s1 = Counter(s1.split(" "))
        counter_s2 = Counter(s2.split(" "))
        retVal = []
        for word, count in counter_s1.items():
            if count == 1:
                if word not in counter_s2.keys():
                    retVal.append(word)
        for word, count in counter_s2.items():
            if count == 1:
                if word not in counter_s1.keys():
                    retVal.append(word)
        return retVal
        '''
