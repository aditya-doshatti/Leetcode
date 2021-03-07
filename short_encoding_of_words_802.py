'''
820. Short Encoding of Words
Medium

A valid encoding of an array of words is any reference string s and array of indices indices such that:

words.length == indices.length
The reference string s ends with the '#' character.
For each index indices[i], the substring of s starting from indices[i] and up to (but not including) the next '#' character is equal to words[i].
Given an array of words, return the length of the shortest reference string s possible of any valid encoding of words.

 

Example 1:

Input: words = ["time", "me", "bell"]
Output: 10
Explanation: A valid encoding would be s = "time#bell#" and indices = [0, 2, 5].
words[0] = "time", the substring of s starting from indices[0] = 0 to the next '#' is underlined in "time#bell#"
words[1] = "me", the substring of s starting from indices[1] = 2 to the next '#' is underlined in "time#bell#"
words[2] = "bell", the substring of s starting from indices[2] = 5 to the next '#' is underlined in "time#bell#"

https://leetcode.com/problems/short-encoding-of-words/
'''
class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        retVal=0
        n=len(words)
        revWords=[word[::-1] for word in words]
        revWords.sort()
        for i in range(n):
            if i+1<n and revWords[i+1].startswith(revWords[i]):
                pass
            else:
                retVal+=len(revWords[i])+1
        return retVal
        # Wrong as sequence doesn't matter
        # n = 0
        # retVal = ""
        # setW = set()
        # while n < len(words):
        #     if words[n] in setW:
        #         n +=1 
        #         continue
        #     setW.add(words[n])
        #     if n !=0 and len(words[n-1]) >= len(words[n]):
        #         if words[n-1][len(words[n-1])-len(words[n]):] == words[n]:
        #             n += 1
        #             continue
        #     elif n != 0 and len(words[n]) >= len(words[n-1]):
        #         if words[n][len(words[n])-len(words[n-1]):] == words[n-1]:
        #             retVal = words[n][:len(words[n])-len(words[n-1])] + retVal
        #             n += 1
        #             continue
        #     retVal =  retVal + words[n] + "#"
        #     n += 1
        # return len(retVal)
