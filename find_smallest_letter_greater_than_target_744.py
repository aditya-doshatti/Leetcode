'''
744. Find Smallest Letter Greater Than Target
Easy

Given a list of sorted characters letters containing only lowercase letters, and given a target letter target, find the smallest element in the list that is larger than the given target.

Letters also wrap around. For example, if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.

Examples:
Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

https://leetcode.com/problems/find-smallest-letter-greater-than-target/
'''
from collections import Counter
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        ac_orig = ord(target)
        if ac_orig == 122:
            ac = 97
        else:
            ac =ac_orig + 1
        di = Counter(letters)
        while True:
            if ac == ac_orig:
                break
            if chr(ac) in di:
                return chr(ac)
            if ac == 122:
                ac = 97
            else:
                ac+=1
