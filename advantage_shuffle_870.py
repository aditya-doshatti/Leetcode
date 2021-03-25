'''
870. Advantage Shuffle
Medium

Given two arrays A and B of equal size, the advantage of A with respect to B is the number of indices i for which A[i] > B[i].

Return any permutation of A that maximizes its advantage with respect to B.

 

Example 1:

Input: A = [2,7,11,15], B = [1,10,4,11]
Output: [2,11,7,15]

https://leetcode.com/problems/advantage-shuffle/
'''
class Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        A.sort()
        retVal = []
        for i in range(len(B)):
            low, high = 0, len(A)
            while low < high:
                mid = (low+high)//2
                if A[mid] < B[i]:
                    low = mid + 1
                else:
                    high = mid
            if low < len(A) and A[low] == B[i]:
                while low < len(A) and A[low] == B[i]:
                    low += 1
            if low == len(A):
                low = 0
            retVal.append(A.pop(low))
        return retVal
