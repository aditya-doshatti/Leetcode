'''
524. Longest Word in Dictionary through Deleting
Medium

Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example 1:
Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output: 
"apple"

https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/
'''
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def match(x, y):
            if not y: 
                return True
            if not x: 
                return False
            if x[0]==y[0]: 
                return match(x[1:], y[1:])
            else:
                return match(x[1:], y)
        
        
        for elem in sorted(d, key = lambda x: (-len(x),x)):
            if match(s,elem):
                return elem
        return ''
        # Did not consider it needs to substring
        # d.sort(key=lambda x: (-len(x),x))
        # sCounter = Counter(s)
        # for elem in d:
        #     if len(elem) > len(s):
        #         continue
        #     else:
        #         flag = True
        #         temp = Counter(elem)
        #         for key in temp:
        #             if key not in sCounter or sCounter[key] < temp[key]:
        #                 #print(key, sCounter, temp)
        #                 flag = False
        #                 break
        #         if flag:
        #             return elem
        # return ""
