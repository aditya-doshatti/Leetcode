'''
60. Permutation Sequence
Medium

Share
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

Note:

Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.
Example 1:

Input: n = 3, k = 3
Output: "213"

https://leetcode.com/problems/permutation-sequence/
'''
class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        sortedList = list(range(1,n+1))
        retVal = ""
        for i in range(n,0,-1):
            q = (k-1)//factorial(i-1)
            k -= q*factorial(i-1)
            retVal += str(sortedList[q])
            sortedList.remove(sortedList[q])
        return retVal
