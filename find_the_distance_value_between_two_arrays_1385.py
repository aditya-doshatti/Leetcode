'''
1385. Find the Distance Value Between Two Arrays
Easy

Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.

The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

 

Example 1:

Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
Output: 2
Explanation: 
For arr1[0]=4 we have: 
|4-10|=6 > d=2 
|4-9|=5 > d=2 
|4-1|=3 > d=2 
|4-8|=4 > d=2 
For arr1[1]=5 we have: 
|5-10|=5 > d=2 
|5-9|=4 > d=2 
|5-1|=4 > d=2 
|5-8|=3 > d=2
For arr1[2]=8 we have:
|8-10|=2 <= d=2
|8-9|=1 <= d=2
|8-1|=7 > d=2
|8-8|=0 <= d=2

https://leetcode.com/problems/find-the-distance-value-between-two-arrays/
'''
class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        arr2.sort()
        retVal = 0
        for val in arr1:
            l, r, found = 0, len(arr2), False
            while l < r:
                mid = (l+r)//2
                if abs(arr2[mid] -val) <= d:
                    found = True
                    break
                elif arr2[mid] < val:
                    l = mid + 1
                else:
                    r = mid
            if not found:
                retVal += 1
        return retVal
