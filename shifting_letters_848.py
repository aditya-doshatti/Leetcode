'''
848. Shifting Letters
Medium
You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.
Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.

 

Example 1:

Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.

https://leetcode.com/problems/shifting-letters/
'''
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s, shifts =  s[::-1], shifts[::-1] #Not the most optimum solution
        retVal = []
        for i,char in enumerate(s):
            curr = chr(ord(char) + sum(shifts[:i+1])%26)
            # print(ord(curr), ord('z'))
            if curr > 'z':
                curr = chr((ord(curr)-ord('z')) + ord('a')-1)
            retVal.append(curr)
        retVal = retVal[::-1]
        return ''.join(retVal)
