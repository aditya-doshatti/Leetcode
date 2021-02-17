'''
784. Letter Case Permutation
Medium

Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.

Return a list of all possible strings we could create. You can return the output in any order.

 

Example 1:

Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

https://leetcode.com/problems/letter-case-permutation/
'''
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        retVal = [[]]
        for char in S:
            if char.isalpha():
                for i in range(len(retVal)):
                    retVal.append(retVal[i][:])
                    retVal[i].append(char.lower())
                    retVal[-1].append(char.upper())
            else:
                for val in retVal:
                    val.append(char)
        return map("".join, retVal)
