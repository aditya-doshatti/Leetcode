'''
408. Valid Word Abbreviation

Easy

A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.

For example, a string such as "substitution" could be abbreviated as (but not limited to):

"s10n" ("s ubstitutio n")
"sub4u4" ("sub stit u tion")
"12" ("substitution")
"su3i1u2on" ("su bst i t u ti on")
"substitution" (no substrings replaced)
The following are not valid abbreviations:

"s55n" ("s ubsti tutio n", the replaced substrings are adjacent)
"s010n" (has leading zeros)
"s0ubstitution" (replaces an empty substring)
Given a string word and an abbreviation abbr, return whether the string matches the given abbreviation.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: word = "internationalization", abbr = "i12iz4n"
Output: true
Explanation: The word "internationalization" can be abbreviated as "i12iz4n" ("i nternational iz atio n").

https://leetcode.com/problems/valid-word-abbreviation/description/
'''
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        if len(abbr) > len(word):
            return False
        wordPointer, abbrPointer, currNumStr = 0, 0, ""
        while abbrPointer < len(abbr) and wordPointer < len(word):
            if abbr[abbrPointer].isalpha():
                if word[wordPointer] != abbr[abbrPointer]:
                    return False
                wordPointer += 1
                abbrPointer += 1
            else:
                if abbr[abbrPointer] == '0':
                    return False
                num = 0
                while abbrPointer < len(abbr) and abbr[abbrPointer].isdigit():
                    num = num * 10 + int(abbr[abbrPointer])
                    abbrPointer += 1
                wordPointer += num
                if wordPointer > len(word):
                    return False
        return wordPointer == len(word) and abbrPointer == len(abbr)
