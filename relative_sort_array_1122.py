'''
1122. Relative Sort Array

Easy

Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.


Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]

https://leetcode.com/problems/relative-sort-array/description/
'''
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ca1 = Counter(arr1)
        retVal = []
        for i in range(len(arr2)):
            if arr2[i] in ca1.keys():
                retVal += [arr2[i]] * ca1[arr2[i]]
                del(ca1[arr2[i]])
        for k in sorted(ca1.keys()):
            retVal += [k] * ca1[k]
        return retVal
