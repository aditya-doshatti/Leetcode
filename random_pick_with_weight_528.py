'''
528. Random Pick with Weight
Medium

Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which randomly picks an index in proportion to its weight.

Note:

1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.

Example 1:

Input: 
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]

https://leetcode.com/problems/random-pick-with-weight/
'''
# from fractions import gcd
# from functools import reduce

class Solution:
    def __init__(self, w:List[int]):
        self.sum = sum(w)
        self.w = [w[0]]
        for val in w[1:]:
            self.w.append(self.w[-1] + val)

    def pickIndex(self) -> int:
        N = random.uniform(0, self.sum)
        lo, hi = 0, len(self.w)
        while lo < hi:
            mid = lo + (hi - lo)//2
            if self.w[mid] < N:
                lo = mid + 1
            else:
                hi = mid
        return lo

    # def __init__(self, w: List[int]):
    #     gcdVal = reduce(gcd, w)
    #     self.dic = {}
    #     for i in range(len(w)):
    #         self.dic[i] = w[i]//gcdVal
    #     self.temp = OrderedDict(sorted(self.dic.items(), key = lambda t: t[1], reverse=True))
    #     # print(self.temp)

    # def pickIndex(self) -> int:
    #     N = random.uniform(0, self.sum)
    #     flag = 1
    #     index = -1
    #     while flag:
    #         index +=1 
    #         if N <= self.w[index]:
    #             flag = 0
    #     return index
            
    # def pickIndex(self) -> int:
    #     k = None
    #     for item in self.temp.items():
    #         k = item
    #         break
    #     # print(k)
    #     if k[1] == 0:
    #         del(self.temp[k[0]])
    #         if len(self.temp) == 0:
    #             self.temp = OrderedDict(sorted(self.dic.items(), key = lambda t: t[1], reverse=True))
    #         for item in self.temp.items():
    #             k = item
    #             break
    #         self.temp[k[0]] -= 1
    #         return k[0]
    #     else:
    #         self.temp[k[0]] -= 1
    #         return k[0]


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
