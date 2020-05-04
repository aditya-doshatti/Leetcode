'''
383. Ransom Note
Easy

Given an arbitrary ransom note string and another string containing letters from all the magazines, write a function that will return true if the ransom note can be constructed from the magazines ; otherwise, it will return false.

Each letter in the magazine string can only be used once in your ransom note.

Note:
You may assume that both strings contain only lowercase letters.

canConstruct("a", "b") -> false
canConstruct("aa", "ab") -> false
canConstruct("aa", "aab") -> true

https://leetcode.com/problems/ransom-note/
'''
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        count = Counter(ransomNote)
        for key in count:
            if magazine.count(key) < count[key]:
                return False
        return True
        # count = Counter(magazine)
        # for char in ransomNote:
        #     if char in count and count[char] > 0:
        #         count[char]-=1
        #     else:
        #         return False
        # return True
