'''
922. Sort Array By Parity II
Easy

Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.

Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.

https://leetcode.com/problems/sort-array-by-parity-ii/
'''
class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        odd = 1
        for even in range(0, len(A), 2):
            if A[even] % 2:
                while A[odd] % 2:
                    odd += 2
                A[even], A[odd] = A[odd], A[even]
        return A
        
        # Wrong logic
        # carry = []
        # for i in range(len(A)):
        #     if i % 2 == A[i] % 2:
        #         continue
        #     if carry:
        #         a,b = carry.pop()
        #         temp = A[i]
        #         A[a] = temp
        #         A[i] = b
        #     else:
        #         carry.append((i, A[i]))
        # return A
