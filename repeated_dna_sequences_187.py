'''
187. Repeated DNA Sequences
Medium

All DNA is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T', for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

 

Example 1:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
Output: ["AAAAACCCCC","CCCCCAAAAA"]

https://leetcode.com/problems/repeated-dna-sequences/
'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        retVal, seen = set(), set()
        for i in range(len(s)-9):
            if s[i:i+10] in seen:
                retVal.add(s[i:i+10])
            else:
                seen.add(s[i:i+10])
        return retVal
