'''
859. Buddy Strings
Easy

Given two strings A and B of lowercase letters, return true if you can swap two letters in A so the result is equal to B, otherwise, return false.

Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at A[i] and A[j]. For example, swapping at indices 0 and 2 in "abcd" results in "cbad".

 

Example 1:

Input: A = "ab", B = "ba"
Output: true
Explanation: You can swap A[0] = 'a' and A[1] = 'b' to get "ba", which is equal to B.

https://leetcode.com/problems/buddy-strings/
'''
class Solution:
    def buddyStrings(self, A: str, B: str) -> bool:
        if len(A) != len(B):
            return False
        flag = False
        idx = -1
        for i in range(len(A)):
            if i != idx and A[i] != B[i]:
                if flag:
                    return False
                if A[i] not in B[i:]:
                    return False
                idx = B[i:].index(A[i])
                idx += i
                if A[idx] != B[i]:
                    return False
                flag = True
        if not flag:
            if A == B and len(set(A)) != len(A):
                flag = True
        return flag and True
