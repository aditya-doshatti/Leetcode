'''
605. Can Place Flowers
Easy

Suppose you have a long flowerbed in which some of the plots are planted and some are not. However, flowers cannot be planted in adjacent plots - they would compete for water and both would die.

Given a flowerbed (represented as an array containing 0 and 1, where 0 means empty and 1 means not empty), and a number n, return if n new flowers can be planted in it without violating the no-adjacent-flowers rule.

Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Note:
The input array won't violate no-adjacent-flowers rule.
The input array size is in the range of [1, 20000].
n is a non-negative integer which won't exceed the input array size.

https://leetcode.com/problems/can-place-flowers/
'''
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        while i < len(flowerbed) :
            if flowerbed[i] == 1 :
                i+=2 
            elif i+1 < len(flowerbed) and flowerbed[i+1] == 1 :
                i+=3
            else :
                i += 2
                n -= 1
        return n <= 0
        # i = 0
        # while n > 0 and i < len(flowerbed):
        #     if i == 0 and i+1 < len(flowerbed):
        #         if flowerbed[i+1] != 1 and flowerbed[i] != 1:
        #             flowerbed[i] = 1
        #             n -= 1
        #     elif i == len(flowerbed)-1:
        #         if flowerbed[i-1] != 1 and flowerbed[i] != 1:
        #             n -=1 
        #         break
        #     else:
        #         if flowerbed[i-1] != 1 and flowerbed[i+1] != 1 and flowerbed[i] != 1:
        #             flowerbed[i] = 1
        #             n -= 1
        #     i+=1
        #     # print(flowerbed, n)
        # return n <=0
