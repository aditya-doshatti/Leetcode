'''
394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].

 

Example 1:

Input: s = "3[a]2[bc]"
Output: "aaabcbc"

https://leetcode.com/problems/decode-string/
'''
class Solution:
    def decodeString(self, s: str) -> str:
        retVal,val, temp, i = '', [], [], 0
        while i < len(s):
            char = s[i]
            if '0' < char <= '9':
                tempVal = ''
                while '0' <= s[i] <= '9':
                    tempVal += s[i]
                    i += 1
                val.append(int(tempVal))
                temp.append('')
            elif char == ']':
                if len(temp) > 1:
                    temp[-2] += temp[-1]*val[-1]
                else:
                    retVal += temp[-1]*val[-1]
                val.pop()
                temp.pop()
            elif char == '[':
                i += 1
                continue
            elif len(val) > 0:
                temp[-1] += char
            else:
                retVal += char
            i += 1
        return retVal
