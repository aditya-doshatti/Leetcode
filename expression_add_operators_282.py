'''
282. Expression Add Operators
Hard

Given a string num that contains only digits and an integer target, return all possibilities to add the binary operators '+', '-', or '*' between the digits of num so that the resultant expression evaluates to the target value.

 

Example 1:

Input: num = "123", target = 6
Output: ["1*2*3","1+2+3"]

https://leetcode.com/problems/expression-add-operators/
'''
class Solution:
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':

        def helper(idx=0, path='', value=0, prev=None):            
            if idx == len(num) and value == target:
                retVal.append(path)
                return
            for i in range(idx+1, len(num) + 1):
                tmp = int(num[idx: i])
                if i == idx + 1 or (i > idx + 1 and num[idx] != '0'):
                    if prev is None :
                        helper(i, num[idx: i], tmp, tmp)
                    else:
                        helper(i, path+'+'+num[idx: i], value + tmp, tmp)
                        helper(i, path+'-'+num[idx: i], value - tmp, -tmp)
                        helper(i, path+'*'+num[idx: i], value - prev + prev*tmp, prev*tmp)
        retVal = []
        helper()
        return retVal
        # TLE
        oprs, retVal = ['+', '-', '*'], []
        def helper(curr, remain, target):
            # print(curr, remain)
            if not remain:
                curr = curr.rstrip('+').rstrip('-').rstrip('*')
                if eval(curr) == target:
                    retVal.append(curr)
            else:
                for i in range(1,len(remain)+1):
                    if i == 1 or (i > 1 and remain[0] != "0"):
                        for op in oprs:
                            helper(curr + op +remain[:i], remain[i:], target)
        for i in range(1, len(num)+1):
            if i == 1 or (i > 1 and num[0] != "0"):
                for op in oprs:
                    helper(num[:i], num[i:], target)
        return list(set(retVal))
                    
