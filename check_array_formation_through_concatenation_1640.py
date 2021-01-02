'''
1640. Check Array Formation Through Concatenation
Easy

You are given an array of distinct integers arr and an array of integer arrays pieces, where the integers in pieces are distinct. Your goal is to form arr by concatenating the arrays in pieces in any order. However, you are not allowed to reorder the integers in each array pieces[i].

Return true if it is possible to form the array arr from pieces. Otherwise, return false.

 

Example 1:

Input: arr = [85], pieces = [[85]]
Output: true

https://leetcode.com/problems/check-array-formation-through-concatenation/
'''
class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:
        dic = {}
        for i, val in enumerate(arr):
            dic[val] = i
        for piece in pieces:
            if not piece[0] in dic:
                return False
            k = dic[piece[0]]
            for i in range(len(piece)):
                if k+i >= len(arr) or arr[k+i] != piece[i]:
                    return False
        return True
