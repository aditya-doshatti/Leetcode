'''
954. Array of Doubled Pairs
Medium

Given an integer array of even length arr, return true if it is possible to reorder arr such that arr[2 * i + 1] = 2 * arr[2 * i] for every 0 <= i < len(arr) / 2, or false otherwise.

Example 1:

Input: arr = [3,1,3,6]
Output: false

https://leetcode.com/problems/array-of-doubled-pairs/
'''
class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        dic = Counter(arr)
        arr.sort()
        for val in arr:
            if val > 0:
                if dic[val] > 0:
                    if (val * 2) not in dic or dic[val*2] < dic[val]:
                        return False
                    dic[val*2] -= dic[val]
                    dic[val] = 0
            else:
                if dic[val] > 0:
                    if (val / 2) not in dic or dic[val/2] < dic[val]:
                        return False
                    dic[val/2] -= dic[val]
                    dic[val] = 0
        return True
