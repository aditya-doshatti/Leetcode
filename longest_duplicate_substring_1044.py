'''
1044. Longest Duplicate Substring
Hard

Given a string S, consider all duplicated substrings: (contiguous) substrings of S that occur 2 or more times.  (The occurrences may overlap.)

Return any duplicated substring that has the longest possible length.  (If S does not have a duplicated substring, the answer is "".)

 

Example 1:

Input: "banana"
Output: "ana"

https://leetcode.com/problems/longest-duplicate-substring/
'''
class Solution:
    def longestDupSubstring(self, S: str) -> str:
        beg, end = 0, len(S)
        q = (1<<31) - 1 
        Found = ""
        while beg + 1 < end:
            mid = (beg + end)//2
            isFound, candidate = self.RabinKarp(S, mid, q)
            if isFound:
                beg, Found = mid, candidate
            else:
                end = mid

        return Found
    # https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm
    def RabinKarp(self,text, M, q):
        if M == 0: return True
        h, t, d = (1<<(8*M-8))%q, 0, 256

        dic = defaultdict(list)

        for i in range(M): 
            t = (d * t + ord(text[i]))% q

        dic[t].append(i-M+1)

        for i in range(len(text) - M):
            t = (d*(t-ord(text[i])*h) + ord(text[i + M]))% q
            for j in dic[t]:
                if text[i+1:i+M+1] == text[j:j+M]:
                    return (True, text[j:j+M])
            dic[t].append(i+1)
        return (False, "")
        
