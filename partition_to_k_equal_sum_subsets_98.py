'''
98. Partition to K Equal Sum Subsets
Medium

Given an array of integers nums and a positive integer k, find whether it's possible to divide this array into k non-empty subsets whose sums are all equal.

 

Example 1:

Input: nums = [4, 3, 2, 3, 5, 2, 1], k = 4
Output: True
Explanation: It's possible to divide it into 4 subsets (5), (1, 4), (2,3), (2,3) with equal sums.

https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
'''
class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total%k:
            return False
        target = total/k
        def search(sumList, sets):
            #print(groups, sets)
            if not nums: return True
            v = nums.pop()
            for i, sumVal in enumerate(sumList):
                if sumVal + v <= target:
                    sumList[i] += v
                    if len(sets) > i:
                        sets[i].add(v)
                    else:
                        sets.append(set({v}))
                    if search(sumList, sets): 
                        return True
                    sumList[i] -= v
                if not sumVal: 
                    break
            nums.append(v)
            return False

        nums.sort()
        if nums[-1] > target: return False
        while nums and nums[-1] == target:
            nums.pop()
            k -= 1
        sets = []
        return search([0] * k, sets)
#         sumVal = sum(arr)
#         if sumVal % k:
#             return False
#         sumEach = sumVal/k
#         retVal = []
#         for i in range(len(arr)):
#             tempSet = set()
#             tempSum = 0 
#             tempSet.add(arr[i])
#             tempSum += arr[i]
#             for j in range(i+1, len(arr)):
#                 print(tempSet)
#                 tempSet, tempSum = self.helper(j, arr, tempSet, tempSum, sumEach, retVal)
#                 if tempSum == sumEach:
#                     retVal.append(tempSet)
#                     break
#         print(retVal)
#         return retVal
    
#     def helper(self, i, arr, tempSet, tempSum, sumEach, retVal):
#         print(tempSet, retVal, sumEach, tempSum)
#         for j in range(i,len(arr)):
#             for k in retVal:
#                 if arr[j] in k:
#                     continue
#             if arr[j] not in tempSet:
#                 if arr[j] + tempSum <= sumEach:
#                     tempSet.add(arr[j])
#                     return tempSet, tempSum
#         return tempSet, tempSum
