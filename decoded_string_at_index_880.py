'''
880. Decoded String at Index
Medium

An encoded string S is given.  To find and write the decoded string to a tape, the encoded string is read one character at a time and the following steps are taken:

If the character read is a letter, that letter is written onto the tape.
If the character read is a digit (say d), the entire current tape is repeatedly written d-1 more times in total.
Now for some encoded string S, and an index K, find and return the K-th letter (1 indexed) in the decoded string.

 

Example 1:

Input: S = "leet2code3", K = 10
Output: "o"
Explanation: 
The decoded string is "leetleetcodeleetleetcodeleetleetcode".
The 10th letter in the string is "o".

https://leetcode.com/problems/decoded-string-at-index/
'''
class Solution:
    def decodeAtIndex(self, S: str, K: int) -> str:
        size = 0
        for char in S:
            if '1' < char <='9':
                size *= int(char)
            else:
                size += 1

        for char in reversed(S):
            K %= size
            if K == 0 and char.isalpha():
                return char

            if '1' < char <='9':
                size /= int(char)
            else:
                size -= 1
        # T L E
        # i, tmp,cnt  = 0, '', 0
        # while i <= K and i <len(S):
        #     print(tmp, S, i)
        #     if '1' < S[i] <='9':
        #         tmp = tmp * int(S[i])
        #         S = tmp + S[i+1:]
        #         i = len(tmp)-1
        #     else:
        #         tmp += S[i]
        #     i += 1
        # print(S)
        # return S[K-1]
