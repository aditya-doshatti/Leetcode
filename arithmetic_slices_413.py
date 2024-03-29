'''
413. Arithmetic Slices
Medium

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:

1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
The following sequence is not arithmetic.

1, 1, 2, 5, 7
 
A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of the array A is called arithmetic if the sequence:
A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.

 
Example:

A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.

https://leetcode.com/problems/arithmetic-slices/
'''
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if not A or len(A) < 3:
            return 0
        retVal = 0
        count, diff = 2, A[1] - A[0]
        for i in range(2, len(A)):
            if A[i] - A[i-1] == diff:
                count += 1
            else:
                if count > 2: 
                    retVal += ((count-1)*(count-2))//2
                count, diff = 2, A[i] - A[i-1]
        if count > 2: 
            retVal += ((count-1)*(count-2))//2
        return retVal
