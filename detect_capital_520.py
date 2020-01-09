'''
520. Detect Capital
Easy

Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
 

Example 1:

Input: "USA"
Output: True

https://leetcode.com/problems/detect-capital/
'''
class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        if len(word) > 1:
            i =2
            cap = False
            if 64 < ord(word[0]) < 91:
                cap = True
            if 64 < ord(word[1]) < 91 and not cap:
                return False
            elif 96 < ord(word[1]) < 123:
                cap = False
            while i < len(word):
                if cap:
                    if 64 > ord(word[i]) or ord(word[i]) > 91:
                        return False
                elif not cap:
                    if 96 > ord(word[i]) or ord(word[i]) > 123:
                        return False
                i+=1
        return True
            
