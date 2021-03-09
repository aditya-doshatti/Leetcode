'''
1078. Occurrences After Bigram
Easy

Given words first and second, consider occurrences in some text of the form "first second third", where second comes immediately after first, and third comes immediately after second.

For each such occurrence, add "third" to the answer, and return the answer.

 

Example 1:

Input: text = "alice is a good girl she is a good student", first = "a", second = "good"
Output: ["girl","student"]

https://leetcode.com/problems/occurrences-after-bigram/
'''
class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        vals = text.split(" ")
        i = 0
        retVal = []
        while i < len(vals):
            if vals[i] == first:
                if i + 1 < len(vals) and vals[i + 1] == second:
                    if i + 2 < len(vals):
                        retVal.append(vals[i + 2])
                        i += 2
                        continue
            i += 1
        return retVal
