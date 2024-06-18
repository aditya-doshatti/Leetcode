'''
1432. Max Difference You Can Get From Changing an Integer

Medium

You are given an integer num. You will apply the following steps exactly two times:

Pick a digit x (0 <= x <= 9).
Pick another digit y (0 <= y <= 9). The digit y can be equal to x.
Replace all the occurrences of x in the decimal representation of num by y.
The new integer cannot have any leading zeros, also the new integer cannot be 0.
Let a and b be the results of applying the operations to num the first and second times, respectively.

Return the max difference between a and b.

 

Example 1:

Input: num = 555
Output: 888
Explanation: The first time pick x = 5 and y = 9 and store the new integer in a.
The second time pick x = 5 and y = 1 and store the new integer in b.
We have now a = 999 and b = 111 and max difference = 888

https://leetcode.com/problems/max-difference-you-can-get-from-changing-an-integer/description/
'''
class Solution:
    def maxDiff(self, num: int) -> int:
        num = str(num)
        maxVal = num
        minVal = num
        for digit in num:
            if digit != '9':
                maxVal = maxVal.replace(digit, '9')
                break
        for digit in num:
            if digit != '1' and digit !='0':
                if digit == minVal[0]:
                    minVal = minVal.replace(digit, '1')
                else:
                    minVal = minVal.replace(digit, '0')
                break
        return int(maxVal)-int(minVal)
        '''
        maxVal, minVal = float('-inf'), float('inf')
        for i in range(10):
            if str(i) in str(num):
                maxVal = max(maxVal, int(str(num).replace(str(i), '9')))
                minVal = min(minVal, int(str(num).replace(str(i), '1')))
                if str(i) != str(num)[0]:
                    minVal = min(minVal, int(str(num).replace(str(i), '0')))
        return maxVal - minVal
        '''
