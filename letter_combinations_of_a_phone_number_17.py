'''
17. Letter Combinations of a Phone Number
Medium

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

https://leetcode.com/problems/letter-combinations-of-a-phone-number/
'''
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        myDict = {1:['*'], 2: ['a','b','c'], 3:['d','e','f'],\
                  4:['g','h','i'], 5:['j','k','l'], 6:['m','n','o'],\
                  7:['p','q','r','s'], 8:['t','u','v'], 9:['w','x','y','z'], 0:[' ']}
        retVal =[]
        for ch in digits:
            ch = int(ch)
            curval = myDict[ch]
            val = curval[::]
            if len(retVal) == 0:
                while val:
                    retVal.append(val.pop())
            else:
                templist = []
                while val:
                    thisVal = val.pop()
                    for i in retVal:
                        i += thisVal
                        templist.append(i)
                if templist != []:
                    retVal = templist[::]
        return retVal
        
