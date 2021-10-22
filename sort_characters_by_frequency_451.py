'''
451. Sort Characters By Frequency
Medium

Given a string, sort it in decreasing order based on the frequency of characters.

Example 1:

Input:
"tree"

Output:
"eert"

Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid answer.

https://leetcode.com/problems/sort-characters-by-frequency/
'''
class Solution:
    def frequencySort(self, s: str) -> str:
        counter = Counter(s)
        retVal = ""
        for val in sorted(counter.items(), key=lambda a:a[1], reverse=True):
            retVal += val[0]*val[1]
        return retVal
'''
from collections import Counter
class Solution:
    def frequencySort(self, s: str) -> str:
        dic = Counter(s)
        k = []
        for key in dic:
            heapq.heappush(k, (-1*dic[key], key))
        retVal = ''
        while k:
            val, char = heapq.heappop(k)
            retVal += ((-1*val)*char)
        return retVal
'''
