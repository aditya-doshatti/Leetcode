'''
1189. Maximum Number of Balloons
Easy

Given a string text, you want to use the characters of text to form as many instances of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of instances that can be formed.

 

Example 1:



Input: text = "nlaebolko"
Output: 1

https://leetcode.com/problems/maximum-number-of-balloons/
'''
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        dic = {'b':0, 'a':0, 'l':0, 'o':0, 'n':0}
        for char in text:
            if char in dic:
                dic[char] += 1 if char in ('l', 'o') else 2
        return min(dic.values()) // 2
        dic ={'b':1, 'a':1,'l':2,'o':2,'n':1}
        counter = Counter(text)
        retVal = float('inf')
        for key in dic.keys():
            if key not in counter:
                return 0
            retVal = min(retVal, counter[key]//dic[key])
        return retVal
