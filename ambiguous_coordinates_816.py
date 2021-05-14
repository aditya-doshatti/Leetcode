'''
816. Ambiguous Coordinates
Medium

We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)".  Then, we removed all commas, decimal points, and spaces, and ended up with the string s.  Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with less digits.  Also, a decimal point within a number never occurs without at least one digit occuring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order.  Also note that all coordinates in the final answer have exactly one space between them (occurring after the comma.)

Example 1:
Input: s = "(123)"
Output: ["(1, 23)", "(12, 3)", "(1.2, 3)", "(1, 2.3)"]

https://leetcode.com/problems/ambiguous-coordinates/
'''
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        results = set()
        isvalid = lambda x: len(str(int(x))) == len(x)

        def getvalidnums(s):
            nums = []
            if isvalid(s): nums.append(s)
            for i in range(1, len(s)):
                if isvalid(s[:i]) and isvalid(s[i:][::-1]) and s[i:] != '0':
                    nums.append(f'{s[:i]}.{s[i:]}')
            return nums

        for i in range(2, len(s)-1):
            lnums = getvalidnums(s[1:i])
            rnums = getvalidnums(s[i:-1])
            for x, y in product(lnums, rnums):
                results.add(f'({x}, {y})')

        return results
