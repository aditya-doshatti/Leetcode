'''
777. Swap Adjacent in LR String
Medium

In a string composed of 'L', 'R', and 'X' characters, like "RXXLRXRXL", a move consists of either replacing one occurrence of "XL" with "LX", or replacing one occurrence of "RX" with "XR". Given the starting string start and the ending string end, return True if and only if there exists a sequence of moves to transform one string to the other.

Example:

Input: start = "RXXLRXRXL", end = "XRLXXRRLX"
Output: True
Explanation:
We can transform start to end following these steps:
RXXLRXRXL ->
XRXLRXRXL ->
XRLXRXRXL ->
XRLXXRRXL ->
XRLXXRRLX

https://leetcode.com/problems/swap-adjacent-in-lr-string/
'''
class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        if len(start) != len(end):
            return False
        if start == end:
            return True
        i  = 0
        a, b = "", ""
        f = {"L":[], "R":[]}
        s = {"L":[], "R":[]}
        while i < len(start):
            if start[i] != 'X':
                a += start[i]
                f[start[i]].append(i)
            if end[i] != 'X':
                b += end[i]
                s[end[i]].append(i)
            i+=1
        if a == b:
            for i in range(len(f['L'])):
                if s['L'][i] > f['L'][i]:
                    return False
            for i in range(len(f['R'])):
                if s['R'][i] < f['R'][i]:
                    return False
            return True
        else:
            return False
