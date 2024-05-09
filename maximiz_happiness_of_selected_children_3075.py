'''
3075. Maximize Happiness of Selected Children

Medium

You are given an array happiness of length n, and a positive integer k.

There are n children standing in a queue, where the ith child has happiness value happiness[i]. You want to select k children from these n children in k turns.

In each turn, when you select a child, the happiness value of all the children that have not been selected till now decreases by 1. Note that the happiness value cannot become negative and gets decremented only if it is positive.

Return the maximum sum of the happiness values of the selected children you can achieve by selecting k children.

 

Example 1:

Input: happiness = [1,2,3], k = 2
Output: 4
Explanation: We can pick 2 children in the following way:
- Pick the child with the happiness value == 3. The happiness value of the remaining children becomes [0,1].
- Pick the child with the happiness value == 1. The happiness value of the remaining child becomes [0]. Note that the happiness value cannot become less than 0.
The sum of the happiness values of the selected children is 3 + 1 = 4.

https://leetcode.com/problems/maximize-happiness-of-selected-children/description/
'''
import heapq
class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        sortedArr = sorted(happiness, reverse=True)
        if sortedArr[k-1] >= k-1:
            return sum(sortedArr[:k]) - ((0 + k-1) * k // 2)
        retVal = 0
        for i, val in enumerate(sortedArr[:k]):
            if val - i <= 0:
                break
            retVal += val - i
        return retVal
        '''
        maxHeap = [-val for val in happiness]
        heapq.heapify(maxHeap)
        step, retVal = 0, 0
        while k:
            currVal = -heapq.heappop(maxHeap)
            if currVal - step > 0:
                retVal += (currVal - step)
            step += 1
            k -= 1
        return retVal
        '''
