'''
2047. Number of Valid Words in a Sentence
Easy

A sentence consists of lowercase letters ('a' to 'z'), digits ('0' to '9'), hyphens ('-'), punctuation marks ('!', '.', and ','), and spaces (' ') only. Each sentence can be broken down into one or more tokens separated by one or more spaces ' '.

A token is a valid word if all three of the following are true:

It only contains lowercase letters, hyphens, and/or punctuation (no digits).
There is at most one hyphen '-'. If present, it must be surrounded by lowercase characters ("a-b" is valid, but "-ab" and "ab-" are not valid).
There is at most one punctuation mark. If present, it must be at the end of the token ("ab,", "cd!", and "." are valid, but "a!b" and "c.," are not valid).
Examples of valid words include "a-b.", "afad", "ba-c", "a!", and "!".

Given a string sentence, return the number of valid words in sentence.

 

Example 1:

Input: sentence = "cat and  dog"
Output: 3
Explanation: The valid words in the sentence are "cat", "and", and "dog".

https://leetcode.com/problems/number-of-valid-words-in-a-sentence/
'''
class Solution:
    def countValidWords(self, sentence: str) -> int:
        retVal = 0
        split = sentence.split(" ")
        def is_lower(c):
            if ord('a')<=ord(c)<= ord('z'):
                return True
            return False
        def valid(w):
            count = 0
            for i, c in enumerate(w):
                if c.isdigit():
                    return False
                if c == '-':
                    if i == 0 or i == len(w)-1:
                        return False
                    if not is_lower(w[i-1]) or not is_lower(w[i+1]):
                        return False
                    if count != 0:
                        return False
                    count += 1
                if c in '!.,' and not i == len(w)-1:
                    return False
            return True
        for word in split:
            if word and valid(word):
                retVal += 1
        return retVal
