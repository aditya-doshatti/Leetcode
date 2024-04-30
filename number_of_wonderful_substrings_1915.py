'''
1915. Number of Wonderful Substrings
Solved
Medium
Topics
Companies
Hint
A wonderful string is a string where at most one letter appears an odd number of times.

For example, "ccjjc" and "abab" are wonderful, but "ab" is not.
Given a string word that consists of the first ten lowercase English letters ('a' through 'j'), return the number of wonderful non-empty substrings in word. If the same substring appears multiple times in word, then count each occurrence separately.

A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: word = "aba"
Output: 4
Explanation: The four wonderful substrings are underlined below:
- "aba" -> "a"
- "aba" -> "b"
- "aba" -> "a"
- "aba" -> "aba"

https://leetcode.com/problems/number-of-wonderful-substrings/description/
'''
class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        ans = 0
        prefix = 0  
        count = [0] * 1024  
        count[0] = 1  

        for c in word:
            prefix ^= 1 << ord(c) - ord('a')
            ans += count[prefix]
            ans += sum(count[prefix ^ 1 << i] for i in range(10))
            count[prefix] += 1

        return ans
        '''
        TLE 57/88
        retVal = 0
        list_of_counts = []
        i = 0
        for j in range(i, len(word)):
            count = [0] * 10
            # print(word[i:j + 1])
            for char in word[i:j + 1]:
                count[ord(char) - ord('a')] += 1
            odd = 0
            for num in count:
                odd += (num % 2)
            if odd <= 1:
                retVal += 1
            list_of_counts.append(count)
        for i,char in enumerate(word):
            print(i,char)
            for counts in list_of_counts[i:]:
                if counts[ord(char) - ord('a')] > 0:
                    counts[ord(char) - ord('a')] -= 1
                odd = 0
                if any(counts):
                    for num in counts:
                        odd += (num % 2)
                    if odd <= 1:
                        retVal += 1
        return retVal
        TLE 43/87
        retVal = 0
        for i in range(len(word)):
            for j in range(i, len(word)):
                count = [0] * 10
                # print(word[i:j + 1])
                for char in word[i:j + 1]:
                    count[ord(char) - ord('a')] += 1
                odd = 0
                # print(count)
                for num in count:
                    odd += (num % 2)
                # print(odd)
                if odd <= 1:
                    retVal += 1
        return retVal
        '''
