'''
1002. Find Common Characters

Easy

Given a string array words, return an array of all characters that show up in all strings within the words (including duplicates). You may return the answer in any order.

Example 1:

Input: words = ["bella","label","roller"]
Output: ["e","l","l"]

https://leetcode.com/problems/find-common-characters/description
'''
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        common_chars = []
        for char in words[0]:
            common_chars.append(char)
        for word in words[1:]:
            to_be_removed = []
            for char in common_chars:
                if char in word:
                    word = word.replace(char, "", 1)
                    continue
                else:
                    to_be_removed.append(char)
            for char in to_be_removed:
                common_chars.remove(char)
        return common_chars
