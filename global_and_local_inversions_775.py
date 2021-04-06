'''
775. Global and Local Inversions
Medium

We have some permutation A of [0, 1, ..., N - 1], where N is the length of A.

The number of (global) inversions is the number of i < j with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i with 0 <= i < N and A[i] > A[i+1].

Return true if and only if the number of global inversions is equal to the number of local inversions.

Example 1:

Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.

https://leetcode.com/problems/global-and-local-inversions/
'''
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        minVal = float('-inf')
        for i in range(1,len(A)):
            if A[i] < minVal:
                return False
            else:
                minVal = max(minVal, A[i-1])
        return  True
        # i = 0
        # while i < len(A)-1:
        #     if A[i+1] < A[i]:
        #         if A[i] - A[i+1] == 1:
        #             i += 1
        #             continue
        #         else:
        #             return False
        #     i += 1
        # return True
        # gi, li, i = 0, 0, len(A)-1
        # minVal = A[-1]
        # while i >= 0 :
        #     if i != 0 and A[i] < A[i-1]:
        #         li += 1
        #     if A[i] > minVal:
        #         gi += 1
        #     minVal = min(A[i], minVal)
        #     i -= 1
        #     # print(li, gi, minVal)
        # return gi == li
