'''
1291. Sequential Digits
Medium

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.

 

Example 1:

Input: low = 100, high = 300
Output: [123,234]

https://leetcode.com/problems/sequential-digits/
'''
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        lookup = '123456789'
        begining = 0
        end = begining +1
        retVal = []
        while begining < 9:
            #print(begining, end, lookup[begining:end])
            temp =  int(lookup[begining:end])
            if low <= temp:
                if temp <= high:
                    bisect.insort(retVal, temp)
                else:
                    begining +=1
                    end = begining +1
            end += 1
            if end > 9:
                begining += 1
                end = begining +1
        return retVal
