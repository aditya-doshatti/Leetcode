'''
2515. Shortest Distance to Target String in a Circular Array

Easy

You are given a 0-indexed circular string array words and a string target. A circular array means that the array's end connects to the array's beginning.

Formally, the next element of words[i] is words[(i + 1) % n] and the previous element of words[i] is words[(i - 1 + n) % n], where n is the length of words.
Starting from startIndex, you can move to either the next word or the previous word with 1 step at a time.

Return the shortest distance needed to reach the string target. If the string target does not exist in words, return -1.

 

Example 1:

Input: words = ["hello","i","am","leetcode","hello"], target = "hello", startIndex = 1
Output: 1
Explanation: We start from index 1 and can reach "hello" by
- moving 3 units to the right to reach index 4.
- moving 2 units to the left to reach index 4.
- moving 4 units to the right to reach index 0.
- moving 1 unit to the left to reach index 0.
The shortest distance to reach "hello" is 1.

https://leetcode.com/problems/shortest-distance-to-target-string-in-a-circular-array/description/
'''
class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:        
        if words[startIndex] == target:
            return 0
        res, n = 0, len(words)
        i = 0
        while i<len(words):
            if words[(startIndex+i)%n]==target or words[(startIndex-i+n)%n]==target:
                return res
            res+=1
            i+=1
        return -1
        '''
        if words[startIndex] == target:
            return 0
        step = 1
        N = len(words)
        i,j = startIndex - step, startIndex + step
        if i == -1:
            i = N -1
        if j > N -1:
            j = 0
        while i != j:
            if words[i] == target or words[j] == target:
                return step
            step += 1
            i -= 1
            j += 1
            if i == -1:
                i = N -1
            if j > N -1:
                j = 0
        if words[i] == target:
            return step
        return -1
        '''
